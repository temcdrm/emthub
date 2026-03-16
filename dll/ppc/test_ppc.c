#define DLL_NAME "PPC.dll"
#define TMAX 10.0
#define CSV_DIR ""
#define VBASE 400e3
#define SBASE 100e6
#define MBASE 100e6

#include <windows.h>
#include <stdio.h>
#include <string.h>

#include "IEEE_Cigre_DLLWrapper.h"

typedef struct _TestScenario {
  const char *name;
  const char *csv_name;
  int32_T FrqFlag;
  int32_T RefFlag;
  int32_T VcmpFlag;
  double qref_base;
} TestScenario;

static int find_signal_index (const IEEE_Cigre_DLLInterface_Signal *pSignals, int count, const char *name)
{
  for (int i = 0; i < count; ++i) {
    if (strcmp (pSignals[i].Name, name) == 0) {
      return i;
    }
  }
  return -1;
}

static int find_parameter_index (const IEEE_Cigre_DLLInterface_Model_Info *pInfo, const char *name)
{
  for (int i = 0; i < pInfo->NumParameters; ++i) {
    if (strcmp (pInfo->ParametersInfo[i].Name, name) == 0) {
      return i;
    }
  }
  return -1;
}

static void set_real_value (char *pBase, ArrayMap *pMap, int idx, double value)
{
  memcpy (pBase + pMap[idx].offset, &value, pMap[idx].size);
}

static void set_int32_value (char *pBase, ArrayMap *pMap, int idx, int32_T value)
{
  memcpy (pBase + pMap[idx].offset, &value, pMap[idx].size);
}

static void initialize_outputs (IEEE_Cigre_DLLInterface_Instance* pModel, ArrayMap *pMap, int nPorts)
{
  double pref = 0.0;
  double qext = 0.0;
  char *pData = (char *) pModel->ExternalOutputs;
  if (nPorts > 0) memcpy (pData + pMap[0].offset, &pref, pMap[0].size);
  if (nPorts > 1) memcpy (pData + pMap[1].offset, &qext, pMap[1].size);
}

static void configure_parameters (Wrapped_IEEE_Cigre_DLL *pWrap, const TestScenario *pScenario)
{
  char *pData = (char *) pWrap->pModel->Parameters;
  int idx = find_parameter_index (pWrap->pInfo, "S_b");
  if (idx >= 0) set_real_value (pData, pWrap->pParameterMap, idx, SBASE);
  idx = find_parameter_index (pWrap->pInfo, "M_b");
  if (idx >= 0) set_real_value (pData, pWrap->pParameterMap, idx, MBASE);
  idx = find_parameter_index (pWrap->pInfo, "V_b");
  if (idx >= 0) set_real_value (pData, pWrap->pParameterMap, idx, VBASE);
  idx = find_parameter_index (pWrap->pInfo, "p_0");
  if (idx >= 0) set_real_value (pData, pWrap->pParameterMap, idx, 0.80);
  idx = find_parameter_index (pWrap->pInfo, "q_0");
  if (idx >= 0) set_real_value (pData, pWrap->pParameterMap, idx, 0.05);
  idx = find_parameter_index (pWrap->pInfo, "FrqFlag");
  if (idx >= 0) set_int32_value (pData, pWrap->pParameterMap, idx, pScenario->FrqFlag);
  idx = find_parameter_index (pWrap->pInfo, "RefFlag");
  if (idx >= 0) set_int32_value (pData, pWrap->pParameterMap, idx, pScenario->RefFlag);
  idx = find_parameter_index (pWrap->pInfo, "VcmpFlag");
  if (idx >= 0) set_int32_value (pData, pWrap->pParameterMap, idx, pScenario->VcmpFlag);
}

static void update_inputs (Wrapped_IEEE_Cigre_DLL *pWrap, const TestScenario *pScenario, double t)
{
  double freq = 1.0;
  double freq_ref = 1.0;
  double plant_pref = 0.80;
  double pmeas = 0.80;
  double qmeas = 0.05;
  double qref = pScenario->qref_base;
  double vmeas = 1.0;

  if (pScenario->FrqFlag && t >= 2.0) {
    freq = 1.05;
  }
  if (!pScenario->FrqFlag && pScenario->RefFlag && !pScenario->VcmpFlag && t >= 2.0) {
    vmeas = 1.05;
  }
  if (!pScenario->FrqFlag && !pScenario->RefFlag && t >= 2.0) {
    qmeas = 1.05;
  }

  char *pData = (char *) pWrap->pModel->ExternalInputs;
  int idx = find_signal_index (pWrap->pInfo->InputPortsInfo, pWrap->pInfo->NumInputPorts, "Freq");
  if (idx >= 0) set_real_value (pData, pWrap->pInputMap, idx, freq);
  idx = find_signal_index (pWrap->pInfo->InputPortsInfo, pWrap->pInfo->NumInputPorts, "Freq_ref");
  if (idx >= 0) set_real_value (pData, pWrap->pInputMap, idx, freq_ref);
  idx = find_signal_index (pWrap->pInfo->InputPortsInfo, pWrap->pInfo->NumInputPorts, "Plant_pref");
  if (idx >= 0) set_real_value (pData, pWrap->pInputMap, idx, plant_pref);
  idx = find_signal_index (pWrap->pInfo->InputPortsInfo, pWrap->pInfo->NumInputPorts, "Pmeas");
  if (idx >= 0) set_real_value (pData, pWrap->pInputMap, idx, pmeas);
  idx = find_signal_index (pWrap->pInfo->InputPortsInfo, pWrap->pInfo->NumInputPorts, "Qmeas");
  if (idx >= 0) set_real_value (pData, pWrap->pInputMap, idx, qmeas);
  idx = find_signal_index (pWrap->pInfo->InputPortsInfo, pWrap->pInfo->NumInputPorts, "Qref");
  if (idx >= 0) set_real_value (pData, pWrap->pInputMap, idx, qref);
  idx = find_signal_index (pWrap->pInfo->InputPortsInfo, pWrap->pInfo->NumInputPorts, "Vmeas");
  if (idx >= 0) set_real_value (pData, pWrap->pInputMap, idx, vmeas);
}

static double extract_outputs (IEEE_Cigre_DLLInterface_Instance* pModel, ArrayMap *pMap, int nPorts)
{
  char *pData = (char *) pModel->ExternalOutputs;
  double pref = 0.0;
  if (nPorts > 0) {
    memcpy (&pref, pData + pMap[0].offset, pMap[0].size);
  }
  return pref;
}

int main( void )
{
  static const TestScenario scenarios[] = {
    {"freq_step", CSV_DIR "PPC_freq_step.csv", 1, 0, 1, 0.05},
    {"voltage_step", CSV_DIR "PPC_voltage_step.csv", 0, 1, 0, 0.0},
    {"qmeas_step", CSV_DIR "PPC_qmeas_step.csv", 0, 0, 1, 0.05},
  };

  show_struct_alignment_requirements ();

  for (int s = 0; s < (int)(sizeof(scenarios) / sizeof(scenarios[0])); ++s) {
    const TestScenario *pScenario = &scenarios[s];
    Wrapped_IEEE_Cigre_DLL *pWrap = CreateFirstDLLModel (DLL_NAME);
    if (NULL == pWrap) {
      return 1;
    }

    printf("running scenario %s (FrqFlag=%d RefFlag=%d VcmpFlag=%d)\n",
           pScenario->name, pScenario->FrqFlag, pScenario->RefFlag, pScenario->VcmpFlag);

    configure_parameters (pWrap, pScenario);

    if (NULL != pWrap->Model_FirstCall) {
      pWrap->Model_FirstCall (pWrap->pModel);
    }
    printf("calling CheckParameters\n");
    pWrap->Model_CheckParameters (pWrap->pModel);
    check_messages ("Model_CheckParameters", pWrap->pModel);

    printf("calling Initialize\n");
    initialize_outputs (pWrap->pModel, pWrap->pOutputMap, pWrap->pInfo->NumOutputPorts);
    update_inputs (pWrap, pScenario, 0.0);
    pWrap->Model_Initialize (pWrap->pModel);
    check_messages ("Model_Initialize", pWrap->pModel);

    double dt = pWrap->pInfo->FixedStepBaseSampleTime;
    double t = 0.0;
    double tstop = TMAX + 0.5 * dt;
    printf("opening %s\n", pScenario->csv_name);
    FILE *fp = fopen (pScenario->csv_name, "w");
    write_csv_header (fp, pWrap->pInfo);
    while (t <= tstop) {
      pWrap->pModel->Time = t;
      update_inputs (pWrap, pScenario, t);
      pWrap->Model_Outputs (pWrap->pModel);
      (void) extract_outputs (pWrap->pModel, pWrap->pOutputMap, pWrap->pInfo->NumOutputPorts);
      write_csv_values (fp, pWrap->pModel, pWrap->pInfo, pWrap->pInputMap, pWrap->pOutputMap, t);
      check_messages ("Model_Outputs", pWrap->pModel);
      t += dt;
    }
    fclose (fp);
    FreeFirstDLLModel (pWrap);
  }

  return 0;
}
