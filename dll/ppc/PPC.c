/*
Manual IEEE/CIGRE wrapper around the exported PPC FMU.

 The wrapper interface mirrors the FMU modelDescription.xml interface:
- inputs: Freq, Freq_ref, Plant_pref, Pmeas, Qmeas, Qref, Vmeas
- outputs: Pref, Qext
- parameters: exported FMU parameters

Boolean FMU parameters are represented as int32_T (0/1), since this
IEEE/CIGRE interface header does not define a boolean parameter datatype.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "IEEE_Cigre_DLLInterface.h"
#include "PPC_FMU.h"
#include "PPC_vr.h"

#if defined(_WIN32)
#include <windows.h>
#include "PPC_resources.h"
#define DLL_EXPORT __declspec(dllexport)
#define DLL_CALL __cdecl
#define PPC_SNPRINTF snprintf
#else
#define DLL_EXPORT __attribute__((visibility("default")))
#define DLL_CALL
#define PPC_SNPRINTF snprintf
#endif

#define CONTROLLER_TIMESTEP 0.02 //seconds

typedef struct _MyModelInputs {
    real64_T Freq;
    real64_T Freq_ref;
    real64_T Plant_pref;
    real64_T Pmeas;
    real64_T Qmeas;
    real64_T Qref;
    real64_T Vmeas;
} MyModelInputs;

typedef struct _MyModelOutputs {
    real64_T Pref;
    real64_T Qext;
} MyModelOutputs;

typedef struct _MyModelParameters {
    real64_T Ddn;
    real64_T Dup;
    real64_T Kc;
    real64_T Ki;
    real64_T Kig;
    real64_T Kp;
    real64_T Kpg;
    real64_T M_b;
    real64_T Pmax;
    real64_T Pmin;
    real64_T Qmin;
    real64_T Rc;
    real64_T S_b;
    real64_T Tft;
    real64_T Tfv;
    real64_T V_b;
    real64_T Vfrz;
    real64_T Xc;
    real64_T dbd1;
    real64_T dbd2;
    real64_T emax;
    real64_T emin;
    real64_T fdbd1;
    real64_T fdbd2;
    real64_T femax;
    real64_T femin;
    real64_T fn;
    real64_T p_0;
    real64_T q_0;
    int32_T FrqFlag;
    int32_T RefFlag;
    int32_T VcmpFlag;
} MyModelParameters;

static IEEE_Cigre_DLLInterface_Signal InputSignals[] = {
    {.Name = "Freq", .Description = "Measured frequency in pu on system frequency base fn", .Unit = "pu(fn)", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .Width = 1},
    {.Name = "Freq_ref", .Description = "Frequency reference in pu on system frequency base fn", .Unit = "pu(fn)", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .Width = 1},
    {.Name = "Plant_pref", .Description = "Plant active power reference in pu on machine base M_b", .Unit = "pu(M_b)", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .Width = 1},
    {.Name = "Pmeas", .Description = "Measured active power in pu on system base S_b", .Unit = "pu(S_b)", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .Width = 1},
    {.Name = "Qmeas", .Description = "Measured reactive power in pu on system base S_b", .Unit = "pu(S_b)", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .Width = 1},
    {.Name = "Qref", .Description = "Reactive power reference in pu on machine base M_b", .Unit = "pu(M_b)", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .Width = 1},
    {.Name = "Vmeas", .Description = "Measured RMS voltage magnitude in pu on voltage base V_b", .Unit = "pu(V_b)", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .Width = 1},
};

static IEEE_Cigre_DLLInterface_Signal OutputSignals[] = {
    {.Name = "Pref", .Description = "Active power command in pu on machine base M_b", .Unit = "pu(M_b)", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .Width = 1},
    {.Name = "Qext", .Description = "Reactive power command in pu on machine base M_b", .Unit = "pu(M_b)", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .Width = 1},
};

static IEEE_Cigre_DLLInterface_Parameter Parameters[] = {
    {.Name = "Ddn", .GroupName = "PPC", .Description = "Reciprocal droop over-frequency", .Unit = "pu", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 20.0, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "Dup", .GroupName = "PPC", .Description = "Reciprocal droop under-frequency", .Unit = "pu", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 0.0, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "Kc", .GroupName = "PPC", .Description = "Reactive current compensation gain", .Unit = "1", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 0.02, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "Ki", .GroupName = "PPC", .Description = "Reactive PI integral gain", .Unit = "1", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 5.0, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "Kig", .GroupName = "PPC", .Description = "Power PI integral gain", .Unit = "1", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 0.05, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "Kp", .GroupName = "PPC", .Description = "Reactive PI proportional gain", .Unit = "1", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 18.0, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "Kpg", .GroupName = "PPC", .Description = "Power PI proportional gain", .Unit = "1", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 0.1, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "M_b", .GroupName = "PPC", .Description = "Machine base power", .Unit = "VA", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 1.0e8, .MinValue.Real64_Val = 0.0, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "Pmax", .GroupName = "PPC", .Description = "Maximum active power command in pu on machine base M_b", .Unit = "pu(M_b)", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 999.0, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "Pmin", .GroupName = "PPC", .Description = "Minimum active power command in pu on machine base M_b", .Unit = "pu(M_b)", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = -999.0, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "Qmin", .GroupName = "PPC", .Description = "Minimum reactive power command in pu on machine base M_b", .Unit = "pu(M_b)", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = -0.436, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "Rc", .GroupName = "PPC", .Description = "Line drop compensation resistance", .Unit = "pu", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 0.0025, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "S_b", .GroupName = "PPC", .Description = "System base power", .Unit = "VA", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 1.0e8, .MinValue.Real64_Val = 0.0, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "Tft", .GroupName = "PPC", .Description = "Lead time constant", .Unit = "s", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 0.0, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "Tfv", .GroupName = "PPC", .Description = "Lag time constant", .Unit = "s", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 0.075, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "V_b", .GroupName = "PPC", .Description = "Base voltage", .Unit = "V", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 4.0e5, .MinValue.Real64_Val = 0.0, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "Vfrz", .GroupName = "PPC", .Description = "Voltage freeze threshold", .Unit = "pu", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 0.0, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "Xc", .GroupName = "PPC", .Description = "Line drop compensation reactance", .Unit = "pu", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 0.0025, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "dbd1", .GroupName = "PPC", .Description = "Reactive deadband lower threshold", .Unit = "pu", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 0.0, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "dbd2", .GroupName = "PPC", .Description = "Reactive deadband upper threshold", .Unit = "pu", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 0.0, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "emax", .GroupName = "PPC", .Description = "Deadband output upper limit", .Unit = "pu", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 0.1, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "emin", .GroupName = "PPC", .Description = "Deadband output lower limit", .Unit = "pu", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = -0.1, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "fdbd1", .GroupName = "PPC", .Description = "Frequency deadband lower threshold", .Unit = "pu", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 0.0, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "fdbd2", .GroupName = "PPC", .Description = "Frequency deadband upper threshold", .Unit = "pu", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 0.0, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "femax", .GroupName = "PPC", .Description = "Frequency error upper limit", .Unit = "pu", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 999.0, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "femin", .GroupName = "PPC", .Description = "Frequency error lower limit", .Unit = "pu", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = -999.0, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "fn", .GroupName = "PPC", .Description = "System base frequency", .Unit = "Hz", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 50.0, .MinValue.Real64_Val = 0.0, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "p_0", .GroupName = "PPC", .Description = "Initial plant active-power operating point in pu on machine base M_b for controller state initialization", .Unit = "pu(M_b)", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 0.8, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "q_0", .GroupName = "PPC", .Description = "Initial plant reactive-power operating point in pu on machine base M_b for controller state initialization", .Unit = "pu(M_b)", .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T, .FixedValue = 0, .DefaultValue.Real64_Val = 0.0, .MinValue.Real64_Val = -1.0e60, .MaxValue.Real64_Val = 1.0e60},
    {.Name = "FrqFlag", .GroupName = "PPC", .Description = "Frequency control enable flag", .Unit = "0/1", .DataType = IEEE_Cigre_DLLInterface_DataType_int32_T, .FixedValue = 0, .DefaultValue.Int32_Val = 1, .MinValue.Int32_Val = 0, .MaxValue.Int32_Val = 1},
    {.Name = "RefFlag", .GroupName = "PPC", .Description = "Voltage versus reactive control flag", .Unit = "0/1", .DataType = IEEE_Cigre_DLLInterface_DataType_int32_T, .FixedValue = 0, .DefaultValue.Int32_Val = 1, .MinValue.Int32_Val = 0, .MaxValue.Int32_Val = 1},
    {.Name = "VcmpFlag", .GroupName = "PPC", .Description = "Line compensation flag", .Unit = "0/1", .DataType = IEEE_Cigre_DLLInterface_DataType_int32_T, .FixedValue = 0, .DefaultValue.Int32_Val = 1, .MinValue.Int32_Val = 0, .MaxValue.Int32_Val = 1},
};

static const IEEE_Cigre_DLLInterface_Model_Info Model_Info = {
    .DLLInterfaceVersion = {2, 0, 0, 0},
    .ModelName = "PPC",
    .ModelVersion = "manual FMU wrapper",
    .ModelDescription = "IEEE/CIGRE wrapper around the exported PPC FMU",
    .GeneralInformation = "Inputs, outputs, and parameters aligned to PPC modelDescription.xml",
    .ModelCreated = __DATE__ " " __TIME__,
    .ModelCreator = "manual",
    .ModelLastModifiedDate = __DATE__ " " __TIME__,
    .ModelLastModifiedBy = "manual",
    .ModelModifiedComment = "Hand-maintained FMU wrapper",
    .ModelModifiedHistory = "Updated to mirror exported FMU interface",
    .EMT_RMS_Mode = 3,
    .FixedStepBaseSampleTime = CONTROLLER_TIMESTEP,
    .NumInputPorts = (int32_T)(sizeof(InputSignals) / sizeof(InputSignals[0])),
    .InputPortsInfo = InputSignals,
    .NumOutputPorts = (int32_T)(sizeof(OutputSignals) / sizeof(OutputSignals[0])),
    .OutputPortsInfo = OutputSignals,
    .NumParameters = (int32_T)(sizeof(Parameters) / sizeof(Parameters[0])),
    .ParametersInfo = Parameters,
    .NumIntStates = 0,
    .NumFloatStates = 0,
    .NumDoubleStates = 0
};

static char ErrorMessage[1024];
static fmi2Component PPC_FMU_COMPONENT = NULL;
#if defined(_WIN32)
static char PPC_RESOURCE_DIR[MAX_PATH];
static char PPC_RESOURCE_URI[MAX_PATH * 2];
static int PPC_RESOURCE_READY = 0;
static HMODULE PPC_DLL_MODULE = NULL;
#endif

static void ppc_logger(
    fmi2ComponentEnvironment env,
    fmi2String instanceName,
    fmi2Status status,
    fmi2String category,
    fmi2String message,
    ...)
{
    (void)env;
    (void)status;
    (void)category;
    if (instanceName != NULL && message != NULL) {
        PPC_SNPRINTF(ErrorMessage, sizeof(ErrorMessage), "[%s] %s", instanceName, message);
    }
}

static int32_T map_fmi_status(fmi2Status status)
{
    if (status == fmi2OK || status == fmi2Warning) {
        return (status == fmi2Warning) ? IEEE_Cigre_DLLInterface_Return_Message : IEEE_Cigre_DLLInterface_Return_OK;
    }
    return IEEE_Cigre_DLLInterface_Return_Error;
}

static fmi2Status ppc_set_real(fmi2ValueReference vr, fmi2Real value)
{
    return fmi2SetReal(PPC_FMU_COMPONENT, &vr, 1, &value);
}

static fmi2Status ppc_set_boolean(fmi2ValueReference vr, int32_T value)
{
    fmi2Boolean boolean_value = value ? fmi2True : fmi2False;
    return fmi2SetBoolean(PPC_FMU_COMPONENT, &vr, 1, &boolean_value);
}

static fmi2Status ppc_get_real(fmi2ValueReference vr, fmi2Real *value)
{
    return fmi2GetReal(PPC_FMU_COMPONENT, &vr, 1, value);
}

#if defined(_WIN32)
BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved)
{
    (void)lpReserved;
    if (fdwReason == DLL_PROCESS_ATTACH) {
        PPC_DLL_MODULE = hinstDLL;
    }
    return TRUE;
}

static int ppc_extract_embedded_resource(HMODULE module, int resource_id, const char *resource_name, const char *output_dir)
{
    char output_path[MAX_PATH];
    HRSRC resource_handle;
    HGLOBAL loaded_resource;
    DWORD resource_size;
    const void *resource_data;
    FILE *fp;

    PPC_SNPRINTF(output_path, sizeof(output_path), "%s\\%s", output_dir, resource_name);

    resource_handle = FindResourceA(module, MAKEINTRESOURCEA(resource_id), RT_RCDATA);
    if (resource_handle == NULL) {
        PPC_SNPRINTF(ErrorMessage, sizeof(ErrorMessage), "Missing embedded resource %s", resource_name);
        return 0;
    }

    loaded_resource = LoadResource(module, resource_handle);
    if (loaded_resource == NULL) {
        PPC_SNPRINTF(ErrorMessage, sizeof(ErrorMessage), "Failed to load embedded resource %s", resource_name);
        return 0;
    }

    resource_size = SizeofResource(module, resource_handle);
    resource_data = LockResource(loaded_resource);
    if (resource_data == NULL) {
        PPC_SNPRINTF(ErrorMessage, sizeof(ErrorMessage), "Failed to lock embedded resource %s", resource_name);
        return 0;
    }

    fp = fopen(output_path, "wb");
    if (fp == NULL) {
        PPC_SNPRINTF(ErrorMessage, sizeof(ErrorMessage), "Failed to create %s", output_path);
        return 0;
    }

    if (resource_size > 0 && fwrite(resource_data, 1, resource_size, fp) != resource_size) {
        fclose(fp);
        PPC_SNPRINTF(ErrorMessage, sizeof(ErrorMessage), "Failed to write %s", output_path);
        return 0;
    }

    fclose(fp);
    return 1;
}

static int ppc_prepare_resource_dir(void)
{
    DWORD temp_len;
    DWORD error_code;
    HMODULE module;
    size_t i;
    char temp_path[MAX_PATH];
    char *uri_path;

    if (PPC_RESOURCE_READY) {
        return 1;
    }

    temp_len = GetTempPathA((DWORD)sizeof(temp_path), temp_path);
    if (temp_len == 0 || temp_len >= sizeof(temp_path)) {
        PPC_SNPRINTF(ErrorMessage, sizeof(ErrorMessage), "Failed to get temp path");
        return 0;
    }

    PPC_SNPRINTF(
        PPC_RESOURCE_DIR,
        sizeof(PPC_RESOURCE_DIR),
        "%sPPC_fmu_%lu",
        temp_path,
        (unsigned long)GetCurrentProcessId());

    if (!CreateDirectoryA(PPC_RESOURCE_DIR, NULL)) {
        error_code = GetLastError();
        if (error_code != ERROR_ALREADY_EXISTS) {
            PPC_SNPRINTF(ErrorMessage, sizeof(ErrorMessage), "Failed to create temp resource dir %s", PPC_RESOURCE_DIR);
            return 0;
        }
    }

    module = PPC_DLL_MODULE;
    if (module == NULL) {
        PPC_SNPRINTF(ErrorMessage, sizeof(ErrorMessage), "Failed to resolve PPC module handle");
        return 0;
    }

    for (i = 0; i < PPC_EMBEDDED_RESOURCE_COUNT; ++i) {
        if (!ppc_extract_embedded_resource(module, PPC_EMBEDDED_RESOURCE_IDS[i], PPC_EMBEDDED_RESOURCE_NAMES[i], PPC_RESOURCE_DIR)) {
            return 0;
        }
    }

    PPC_SNPRINTF(PPC_RESOURCE_URI, sizeof(PPC_RESOURCE_URI), "file:///%s", PPC_RESOURCE_DIR);
    uri_path = PPC_RESOURCE_URI + strlen("file:///");
    for (; *uri_path != '\0'; ++uri_path) {
        if (*uri_path == '\\') {
            *uri_path = '/';
        }
    }

    PPC_RESOURCE_READY = 1;
    return 1;
}

static void ppc_cleanup_resource_dir(void)
{
    size_t i;
    char output_path[MAX_PATH];

    if (!PPC_RESOURCE_READY) {
        return;
    }

    for (i = 0; i < PPC_EMBEDDED_RESOURCE_COUNT; ++i) {
        PPC_SNPRINTF(output_path, sizeof(output_path), "%s\\%s", PPC_RESOURCE_DIR, PPC_EMBEDDED_RESOURCE_NAMES[i]);
        DeleteFileA(output_path);
    }

    RemoveDirectoryA(PPC_RESOURCE_DIR);
    PPC_RESOURCE_DIR[0] = '\0';
    PPC_RESOURCE_URI[0] = '\0';
    PPC_RESOURCE_READY = 0;
}
#endif

static int32_T ensure_fmu_created(void)
{
    fmi2CallbackFunctions callbacks;
    const char *resource_uri = "";

    if (PPC_FMU_COMPONENT != NULL) {
        return IEEE_Cigre_DLLInterface_Return_OK;
    }

    callbacks.logger = ppc_logger;
    callbacks.allocateMemory = calloc;
    callbacks.freeMemory = free;
    callbacks.stepFinished = NULL;
    callbacks.componentEnvironment = NULL;

#if defined(_WIN32)
    if (!ppc_prepare_resource_dir()) {
        return IEEE_Cigre_DLLInterface_Return_Error;
    }
    resource_uri = PPC_RESOURCE_URI;
#endif

    PPC_FMU_COMPONENT = fmi2Instantiate("PPC", fmi2CoSimulation, MODEL_GUID, resource_uri, &callbacks, fmi2False, fmi2False);
    if (PPC_FMU_COMPONENT == NULL) {
        PPC_SNPRINTF(ErrorMessage, sizeof(ErrorMessage), "Failed to instantiate FMU");
#if defined(_WIN32)
        ppc_cleanup_resource_dir();
#endif
        return IEEE_Cigre_DLLInterface_Return_Error;
    }
    return IEEE_Cigre_DLLInterface_Return_OK;
}

static fmi2Status apply_parameters(const MyModelParameters *parameters)
{
    fmi2Status status = fmi2OK;

    status = ppc_set_real(VR_DDN, parameters->Ddn); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_DUP, parameters->Dup); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_KC, parameters->Kc); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_KI, parameters->Ki); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_KIG, parameters->Kig); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_KP, parameters->Kp); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_KPG, parameters->Kpg); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_M_B, parameters->M_b); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_PMAX, parameters->Pmax); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_PMIN, parameters->Pmin); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_QMIN, parameters->Qmin); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_RC, parameters->Rc); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_S_B, parameters->S_b); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_TFT, parameters->Tft); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_TFV, parameters->Tfv); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_V_B, parameters->V_b); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_VFRZ, parameters->Vfrz); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_XC, parameters->Xc); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_DBD1, parameters->dbd1); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_DBD2, parameters->dbd2); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_EMAX, parameters->emax); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_EMIN, parameters->emin); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_FDBD1, parameters->fdbd1); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_FDBD2, parameters->fdbd2); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_FEMAX, parameters->femax); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_FEMIN, parameters->femin); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_FN, parameters->fn); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_P_0, parameters->p_0); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_Q_0, parameters->q_0); if (status > fmi2Warning) return status;
    status = ppc_set_boolean(VR_FRQFLAG, parameters->FrqFlag); if (status > fmi2Warning) return status;
    status = ppc_set_boolean(VR_REFFLAG, parameters->RefFlag); if (status > fmi2Warning) return status;
    status = ppc_set_boolean(VR_VCMPFLAG, parameters->VcmpFlag); if (status > fmi2Warning) return status;

    return status;
}

static fmi2Status apply_inputs(const MyModelInputs *inputs)
{
    fmi2Status status = fmi2OK;

    status = ppc_set_real(VR_FREQ, inputs->Freq); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_FREQ_REF, inputs->Freq_ref); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_PLANT_PREF, inputs->Plant_pref); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_PMEAS, inputs->Pmeas); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_QMEAS, inputs->Qmeas); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_QREF, inputs->Qref); if (status > fmi2Warning) return status;
    status = ppc_set_real(VR_VMEAS, inputs->Vmeas); if (status > fmi2Warning) return status;

    return status;
}

DLL_EXPORT const IEEE_Cigre_DLLInterface_Model_Info *DLL_CALL Model_GetInfo(void)
{
    return &Model_Info;
}

DLL_EXPORT int32_T DLL_CALL Model_CheckParameters(IEEE_Cigre_DLLInterface_Instance *instance)
{
    MyModelParameters *parameters = (MyModelParameters *)instance->Parameters;
    ErrorMessage[0] = '\0';

    parameters->FrqFlag = parameters->FrqFlag ? 1 : 0;
    parameters->RefFlag = parameters->RefFlag ? 1 : 0;
    parameters->VcmpFlag = parameters->VcmpFlag ? 1 : 0;
    instance->LastGeneralMessage = ErrorMessage;
    return IEEE_Cigre_DLLInterface_Return_OK;
}

DLL_EXPORT int32_T DLL_CALL Model_FirstCall(IEEE_Cigre_DLLInterface_Instance *instance)
{
    (void)instance;
    ErrorMessage[0] = '\0';
    return ensure_fmu_created();
}

DLL_EXPORT int32_T DLL_CALL Model_Initialize(IEEE_Cigre_DLLInterface_Instance *instance)
{
    const MyModelInputs *inputs = (const MyModelInputs *)instance->ExternalInputs;
    const MyModelParameters *parameters = (const MyModelParameters *)instance->Parameters;
    MyModelOutputs *outputs = (MyModelOutputs *)instance->ExternalOutputs;
    fmi2Status status;

    ErrorMessage[0] = '\0';
    outputs->Pref = 0.0;
    outputs->Qext = 0.0;

    if (ensure_fmu_created() != IEEE_Cigre_DLLInterface_Return_OK) {
        instance->LastErrorMessage = ErrorMessage;
        return IEEE_Cigre_DLLInterface_Return_Error;
    }

    status = fmi2Reset(PPC_FMU_COMPONENT);
    if (status > fmi2Warning) return map_fmi_status(status);

    status = fmi2SetupExperiment(PPC_FMU_COMPONENT, fmi2False, 0.0, 0.0, fmi2False, 0.0);
    if (status > fmi2Warning) return map_fmi_status(status);

    status = fmi2EnterInitializationMode(PPC_FMU_COMPONENT);
    if (status > fmi2Warning) return map_fmi_status(status);

    status = apply_parameters(parameters);
    if (status > fmi2Warning) return map_fmi_status(status);

    status = apply_inputs(inputs);
    if (status > fmi2Warning) return map_fmi_status(status);

    status = fmi2ExitInitializationMode(PPC_FMU_COMPONENT);
    if (status > fmi2Warning) return map_fmi_status(status);

    instance->LastGeneralMessage = ErrorMessage;
    return IEEE_Cigre_DLLInterface_Return_OK;
}

DLL_EXPORT int32_T DLL_CALL Model_Outputs(IEEE_Cigre_DLLInterface_Instance *instance)
{
    const MyModelInputs *inputs = (const MyModelInputs *)instance->ExternalInputs;
    MyModelOutputs *outputs = (MyModelOutputs *)instance->ExternalOutputs;
    fmi2Real pref = 0.0;
    fmi2Real qext = 0.0;
    fmi2Status status;

    ErrorMessage[0] = '\0';

    if (ensure_fmu_created() != IEEE_Cigre_DLLInterface_Return_OK) {
        instance->LastErrorMessage = ErrorMessage;
        return IEEE_Cigre_DLLInterface_Return_Error;
    }

    status = apply_inputs(inputs);
    if (status > fmi2Warning) return map_fmi_status(status);

    status = fmi2DoStep(PPC_FMU_COMPONENT, instance->Time, Model_Info.FixedStepBaseSampleTime, fmi2True);
    if (status > fmi2Warning) {
        instance->LastErrorMessage = ErrorMessage;
        return map_fmi_status(status);
    }

    status = ppc_get_real(VR_PREF, &pref);
    if (status > fmi2Warning) return map_fmi_status(status);

    status = ppc_get_real(VR_QEXT, &qext);
    if (status > fmi2Warning) return map_fmi_status(status);

    outputs->Pref = pref;
    outputs->Qext = qext;
    instance->LastGeneralMessage = ErrorMessage;
    return IEEE_Cigre_DLLInterface_Return_OK;
}

DLL_EXPORT int32_T DLL_CALL Model_Terminate(IEEE_Cigre_DLLInterface_Instance *instance)
{
    ErrorMessage[0] = '\0';
    if (PPC_FMU_COMPONENT != NULL) {
        fmi2Terminate(PPC_FMU_COMPONENT);
        fmi2FreeInstance(PPC_FMU_COMPONENT);
        PPC_FMU_COMPONENT = NULL;
    }
#if defined(_WIN32)
    ppc_cleanup_resource_dir();
#endif
    instance->LastGeneralMessage = ErrorMessage;
    return IEEE_Cigre_DLLInterface_Return_OK;
}

DLL_EXPORT int32_T DLL_CALL Model_PrintInfo(void)
{
    printf("Cigre/IEEE DLL Standard\n");
    printf("Model name:             %s\n", Model_Info.ModelName);
    printf("Model description:      %s\n", Model_Info.ModelDescription);
    printf("Model version:          %s\n", Model_Info.ModelVersion);
    printf("Inputs:                 %d\n", Model_Info.NumInputPorts);
    printf("Outputs:                %d\n", Model_Info.NumOutputPorts);
    printf("Parameters:             %d\n", Model_Info.NumParameters);
    return IEEE_Cigre_DLLInterface_Return_OK;
}
