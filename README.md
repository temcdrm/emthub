# EMTHub&reg;

Software and data schemas for standards-based model building and 
validation to perform electromagnetic transient (EMT) studies of electric 
utility power systems. The focus is on inverter-based resources (IBR), 
e.g., wind, solar, and storage, in electric utility systems. 

Use the Green Code button to download.

- End users may now follow the installation described in the next section.
- Developers may now use `git clone https://github.com/temcdrm/emthub.git` from a local directory.

## Users

Python is required.

- Install [Python](https://www.python.org/).
- Invoke `pip install emthub --upgrade`.

## Examples

### Common Information Model (CIM) Profile

These examples support IEEE P3743.

- [CIM](cim): CIM extensions, profile, examples, and input raw files.
- [MATPOWER](matpower): Scripts that establish initial conditions for some EMT examples.
- [ATP Systems](atp/data): Example EMT input files for the Alternative Transients Program (ATP).

### IEEE/Cigre Dynamic Link Library (DLL) Interface

These examples support IEEE P3597.

- [DLL](dll): source files to build DLLs and test them in Python scripts.
- [ATP DLL](atp/dll): running DLL examples in ATP.

### Alternative Transients Program (ATP)

Some examples require a license to run them in ATP. See [ATP Web Site](https://atp-emtp.org/) for more information, and to apply for an ATP license.

## Developers

Use `pip install -e .` to install the Python emthub package from your git clone.

Queries are performed using the built-in Python packages _rdflib_ and/or _sqlite3_. In developing new SPARQL queries,
the optional [Blazegraph](https://github.com/blazegraph/database/releases) triple-store is often convenient because it enables interactive SPARQL in a Web browser.
However, Blazegraph does require a local Java installation. 

To deploy the project on PyPi, staring in the directory of your git clone, where `setup.py` is located:

- Make sure that the version number in `setup.cfg` and `src\emthub\version.py` is new.
- Invoke `rd /s /q dist` on Windows (would be `rm -rf dist` on Linux or Mac OS X)
- `python -m build`
- `twine check dist/*` should not show any errors
- `twine upload -r testpypi dist/*` requires project credentials for pecblocks on test.pypi.org (Note: this will reject if version already exists, also note that testpypi is a separate register to pypi)
- `pip install -i https://test.pypi.org/simple/ emthub==0.0.3` for local testing of the deployable package, example version 0.0.3 (Note: consider doing this in a separate Python test environment)
- `twine upload dist/*` for final deployment

Copyright &copy; 2024-25, Meltran, Inc

