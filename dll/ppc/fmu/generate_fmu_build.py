#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import shlex
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
FMU_DIR = Path(__file__).resolve().parent
PPC_DIR = FMU_DIR.parent
BUILD_DIR = FMU_DIR / "build"
EXPORT_SCRIPT = FMU_DIR / "export_fmu.mos"
MAKEFILE_PATH = BUILD_DIR / "PPC_FMU.makefile"
TEMPLATE_PATH = PPC_DIR / "CMakeLists.fmu.in"
OUTPUT_CMAKE_PATH = PPC_DIR / "CMakeLists.txt"
OUTPUT_RESOURCE_RC_PATH = PPC_DIR / "PPC_resources.rc"
OUTPUT_RESOURCE_HEADER_PATH = PPC_DIR / "PPC_resources.h"
OUTPUT_VR_HEADER_PATH = PPC_DIR / "PPC_vr.h"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Clean dll/ppc/fmu/build, export the PPC FMU, and generate dll/ppc/CMakeLists.txt."
    )
    parser.add_argument(
        "--omc-cmd",
        required=True,
        help="Command used to run OpenModelica, for example: wine .../omc.exe",
    )
    parser.add_argument(
        "--smoke-test",
        action="store_true",
        help="Configure and build the generated root dll/ppc project after generation.",
    )
    parser.add_argument(
        "--smoke-build-dir",
        type=Path,
        default=BUILD_DIR / "cmake-smoke",
        help="Build directory for the CMake smoke test.",
    )
    return parser.parse_args()


def run(cmd: list[str], cwd: Path) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


def split_command(cmd: str) -> list[str]:
    return shlex.split(cmd, posix=os.name != "nt")


def run_shell(cmd: str, cwd: Path) -> None:
    cmd_parts = split_command(cmd)
    print("+", " ".join(cmd_parts))
    subprocess.run(cmd_parts, cwd=cwd, check=True)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def extract_sources_dir(makefile_text: str) -> str:
    normalized = makefile_text.replace("\\", "/")
    match = re.search(r"([A-Za-z0-9_.-]+\.fmutmp)/sources", normalized)
    if not match:
        raise RuntimeError(f"Could not find *.fmutmp/sources in {MAKEFILE_PATH}")
    return match.group(1) + "/sources"


def extract_fmu_hash(source_cmake_text: str, fallback_dirname: str) -> str:
    match = re.search(r"set\(FMU_NAME_HASH\s+([^)]+)\)", source_cmake_text)
    if match:
        return match.group(1).strip()
    return fallback_dirname.removesuffix(".fmutmp")


def extract_fmu_name(source_cmake_text: str, fallback_name: str = "PPC") -> str:
    match = re.search(r"set\(FMU_NAME\s+([^)]+)\)", source_cmake_text)
    if match:
        return match.group(1).strip()
    return fallback_name


def render_template(
    template_text: str,
    project_name: str,
    fmu_name: str,
    fmu_hash: str,
    fmu_sources_rel: str,
) -> str:
    replacements = {
        "@PROJECT_NAME@": project_name,
        "@FMU_NAME@": fmu_name,
        "@FMU_HASH@": fmu_hash,
        "@FMU_SOURCES_REL@": fmu_sources_rel.replace("\\", "/"),
    }
    rendered = template_text
    for needle, value in replacements.items():
        rendered = rendered.replace(needle, value)
    return rendered


def render_resource_rc(resource_files_rel: list[str]) -> str:
    lines = ["/* Generated file. Do not edit by hand. */", ""]
    for index, rel_path in enumerate(resource_files_rel, start=101):
        path = rel_path.replace("\\", "/")
        lines.append(f'{index} RCDATA "{path}"')
    lines.append("")
    return "\n".join(lines)


def render_resource_header(resource_names: list[str]) -> str:
    lines = [
        "/* Generated file. Do not edit by hand. */",
        "#ifndef PPC_RESOURCES_H",
        "#define PPC_RESOURCES_H",
        "",
        f"#define PPC_EMBEDDED_RESOURCE_COUNT {len(resource_names)}",
        "",
        "static const char * const PPC_EMBEDDED_RESOURCE_NAMES[PPC_EMBEDDED_RESOURCE_COUNT] = {",
    ]
    for name in resource_names:
        lines.append(f'    "{name.upper()}",')
    lines.extend(
        [
            "};",
            "",
            "static const int PPC_EMBEDDED_RESOURCE_IDS[PPC_EMBEDDED_RESOURCE_COUNT] = {",
        ]
    )
    for index, _ in enumerate(resource_names, start=101):
        lines.append(f"    {index},")
    lines.extend(["};", "", "#endif"])
    return "\n".join(lines) + "\n"


def sanitize_vr_name(name: str) -> str:
    sanitized = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_")
    return sanitized.upper()


def parse_model_variables(model_description_path: Path) -> list[tuple[str, str]]:
    root = ET.parse(model_description_path).getroot()
    variables: list[tuple[str, str]] = []
    model_variables = root.find("ModelVariables")
    if model_variables is None:
        return variables
    for scalar in model_variables.findall("ScalarVariable"):
        name = scalar.attrib.get("name")
        value_reference = scalar.attrib.get("valueReference")
        if name and value_reference:
            variables.append((name, value_reference))
    return variables


def render_vr_header(variables: list[tuple[str, str]]) -> str:
    lines = [
        "/* Generated file. Do not edit by hand. */",
        "#ifndef PPC_VR_H",
        "#define PPC_VR_H",
        "",
    ]
    seen: set[str] = set()
    for name, value_reference in variables:
        macro = f"VR_{sanitize_vr_name(name)}"
        if macro in seen:
            raise ValueError(f"Duplicate VR macro generated for variable {name}")
        seen.add(macro)
        lines.append(f"#define {macro} {value_reference}")
    lines.extend(["", "#endif", ""])
    return "\n".join(lines)


def find_resource_files(build_dir: Path, sources_rel: str) -> tuple[Path, list[Path]]:
    fmu_tmp_dir = build_dir / Path(sources_rel).parts[0]
    resources_dir = fmu_tmp_dir / "resources"
    if not resources_dir.exists():
        return resources_dir, []
    files = sorted(path for path in resources_dir.iterdir() if path.is_file())
    return resources_dir, files


def patch_msvc_zero_length_arrays(sources_dir: Path) -> list[Path]:
    patched_files: list[Path] = []
    pattern = re.compile(r"const int (columns|rows)\[0\] = \{\};")

    for path in sources_dir.rglob("*.c"):
        text = read_text(path)
        new_text = pattern.sub(r"const int \1[1] = {0};", text)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            patched_files.append(path)

    return patched_files


def main() -> int:
    args = parse_args()
    backup_dir = FMU_DIR / "build.backup"

    if backup_dir.exists():
        shutil.rmtree(backup_dir)
    if BUILD_DIR.exists():
        BUILD_DIR.rename(backup_dir)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)

    try:
        run_shell(f"{args.omc_cmd} {EXPORT_SCRIPT.name}", cwd=FMU_DIR)
    except Exception:
        shutil.rmtree(BUILD_DIR, ignore_errors=True)
        if backup_dir.exists():
            backup_dir.rename(BUILD_DIR)
        raise
    else:
        if backup_dir.exists():
            shutil.rmtree(backup_dir)

    if not MAKEFILE_PATH.exists():
        raise FileNotFoundError(
            f"Expected generated makefile at {MAKEFILE_PATH}. FMU export did not complete."
        )

    makefile_text = read_text(MAKEFILE_PATH)
    sources_rel = extract_sources_dir(makefile_text)
    sources_dir = (BUILD_DIR / sources_rel).resolve()
    source_cmake_path = sources_dir / "CMakeLists.txt"
    if not source_cmake_path.exists():
        raise FileNotFoundError(f"Expected extracted FMU CMake at {source_cmake_path}")

    source_cmake_text = read_text(source_cmake_path)
    fmu_hash = extract_fmu_hash(source_cmake_text, Path(sources_rel).parts[0])
    fmu_name = extract_fmu_name(source_cmake_text)
    model_description_path = (
        BUILD_DIR / Path(sources_rel).parts[0] / "modelDescription.xml"
    )
    model_variables = parse_model_variables(model_description_path)

    patched_files = patch_msvc_zero_length_arrays(sources_dir)
    for path in patched_files:
        print(f"Patched MSVC zero-length arrays in {path}")

    resources_dir, resource_files = find_resource_files(BUILD_DIR, sources_rel)
    resource_files_rel = [
        str(path.relative_to(PPC_DIR)).replace("\\", "/") for path in resource_files
    ]
    resource_names = [path.name for path in resource_files]
    OUTPUT_RESOURCE_RC_PATH.write_text(
        render_resource_rc(resource_files_rel), encoding="utf-8"
    )
    print(f"Wrote {OUTPUT_RESOURCE_RC_PATH}")
    OUTPUT_RESOURCE_HEADER_PATH.write_text(
        render_resource_header(resource_names), encoding="utf-8"
    )
    print(f"Wrote {OUTPUT_RESOURCE_HEADER_PATH}")
    OUTPUT_VR_HEADER_PATH.write_text(
        render_vr_header(model_variables), encoding="utf-8"
    )
    print(f"Wrote {OUTPUT_VR_HEADER_PATH}")

    template_text = read_text(TEMPLATE_PATH)
    output_text = render_template(
        template_text=template_text,
        project_name="PPC",
        fmu_name=fmu_name,
        fmu_hash=fmu_hash,
        fmu_sources_rel=str(Path("fmu") / "build" / sources_rel),
    )
    OUTPUT_CMAKE_PATH.write_text(output_text, encoding="utf-8")
    print(f"Wrote {OUTPUT_CMAKE_PATH}")

    if args.smoke_test:
        smoke_build_dir = args.smoke_build_dir.resolve()
        if smoke_build_dir.exists():
            shutil.rmtree(smoke_build_dir)
        run(
            [
                shutil.which("cmake") or "cmake",
                "-S",
                str(PPC_DIR),
                "-B",
                str(smoke_build_dir),
            ],
            cwd=REPO_ROOT,
        )
        run(
            [shutil.which("cmake") or "cmake", "--build", str(smoke_build_dir)],
            cwd=REPO_ROOT,
        )

    print(f"FMU sources dir: {sources_dir}")
    print(f"FMU hash target: {fmu_hash}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(f"Command failed with exit code {exc.returncode}", file=sys.stderr)
        raise
