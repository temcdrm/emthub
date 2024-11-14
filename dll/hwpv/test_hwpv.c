// Copyright (C) 2024 Meltran, Inc

// see https://learn.microsoft.com/en-us/windows/win32/dlls/using-run-time-dynamic-linking

#define DLL_NAME "hwpv.dll"

#define JSON_FILE1 "C:\\src\\pecblocks\\examples\\hwpv\\bal3\\bal3_fhf.json"
#define JSON_FILE2 "C:\\src\\pecblocks\\examples\\hwpv\\ucf4t\\ucf4t_fhf.json"
#define JSON_FILE3 "C:\\src\\pecblocks\\examples\\hwpv\\unb3\\unb3_fhf.json"
#define JSON_FILE4 "C:\\src\\pecblocks\\examples\\hwpv\\osg4\\osg4_fhf.json"

#define TMAX 8.0
// relative output path for execution from the build directory, e.g., release\test or debug\test
#define CSV_NAME "hwpv.csv"

#include <windows.h> 
#include <stdio.h>
#include <math.h>

#include "IEEE_Cigre_DLLWrapper.h"
 
void initialize_outputs (IEEE_Cigre_DLLInterface_Instance* pModel, ArrayMap *pMap, int nPorts)
{
  double EFD = 1.0;
  char *pData = (char *) pModel->ExternalOutputs;
  memcpy (pData + pMap[0].offset, &EFD, pMap[0].size);
}

// interpolated inputs

typedef struct {
  double *x;
  double *y;
  double *m;
  int n;
} interp_table;

interp_table T_table;
interp_table G_table;
interp_table Fc_table;
interp_table Rg_table;
interp_table Ud_table;
interp_table Uq_table;
interp_table Ctl_table;

void print_one_table (interp_table *pTbl, const char *lbl)
{
  printf("Stimulus Lookup Table %s i, x, y, m\n", lbl);
  for (int i=0; i < pTbl->n; i++) {
    printf("%4d %13g %13g %13g\n", i, pTbl->x[i], pTbl->y[i], i < pTbl->n-1 ? pTbl->m[i] : 0.0);
  }
}

void initialize_one_table (interp_table *pTbl, int n, double x[], double y[])
{
  pTbl->n = n;
  pTbl->x = malloc (sizeof (double) * n);
  pTbl->y = malloc (sizeof (double) * n);
  pTbl->m = malloc (sizeof (double) * (n-1));
  for (int i=0; i < n; i++) {
    pTbl->x[i] = x[i];
    pTbl->y[i] = y[i];
    if (i>0) {
      pTbl->m[i-1] = (y[i] - y[i-1]) / (x[i] - x[i-1]);
    }
  }
}

void initialize_tables ()
{
  double xT[] = {0.0, 1000.0};
  double yT[] = {35.0, 35.0};
  if (sizeof(xT) != sizeof (yT)) {
    printf("**** ERROR: unequal number of points in lookup table for T\n");
    exit (EXIT_FAILURE);
  }
  initialize_one_table (&T_table, sizeof(xT) / sizeof(xT[0]), xT, yT);

  double xG[] = {0.0, 1.0, 2.0, 1000.0};
  double yG[] = {0.0, 0.0, 950.0, 950.0};
  if (sizeof(xG) != sizeof (yG)) {
    printf("**** ERROR: unequal number of points in lookup table for G\n");
    exit (EXIT_FAILURE);
  }
  initialize_one_table (&G_table, sizeof(xG) / sizeof(xG[0]), xG, yG);

  double xFc[] = {0.0, 1000.0};
  double yFc[] = {60.0, 60.0};
  if (sizeof(xFc) != sizeof (yFc)) {
    printf("**** ERROR: unequal number of points in lookup table for Fc\n");
    exit (EXIT_FAILURE);
  }
  initialize_one_table (&Fc_table, sizeof(xFc) / sizeof(xFc[0]), xFc, yFc);

  double xUd[] = {0.0, 1000.0};
  double yUd[] = {1.0, 1.0};
  if (sizeof(xUd) != sizeof (yUd)) {
    printf("**** ERROR: unequal number of points in lookup table for Ud\n");
    exit (EXIT_FAILURE);
  }
  initialize_one_table (&Ud_table, sizeof(xUd) / sizeof(xUd[0]), xUd, yUd);

  double xUq[] = {0.0, 1000.0};
  double yUq[] = {0.0, 0.0};
  if (sizeof(xUq) != sizeof (yUq)) {
    printf("**** ERROR: unequal number of points in lookup table for Uq\n");
    exit (EXIT_FAILURE);
  }
  initialize_one_table (&Uq_table, sizeof(xUq) / sizeof(xUq[0]), xUq, yUq);

  double xCtl[] = {0.0, 2.5, 2.51, 1000.0};
  double yCtl[] = {0.0, 0.0, 1.0, 1.0};
  if (sizeof(xCtl) != sizeof (yCtl)) {
    printf("**** ERROR: unequal number of points in lookup table for Ctl\n");
    exit (EXIT_FAILURE);
  }
  initialize_one_table (&Ctl_table, sizeof(xCtl) / sizeof(xCtl[0]), xCtl, yCtl);

  double xRg[] = {0.0, 5.0, 5.001, 1000.0};
  double yRg[] = {2.3, 2.3, 3.0, 3.0};
  if (sizeof(xRg) != sizeof (yRg)) {
    printf("**** ERROR: unequal number of points in lookup table for Rg\n");
    exit (EXIT_FAILURE);
  }
  initialize_one_table (&Rg_table, sizeof(xRg) / sizeof(xRg[0]), xRg, yRg);

  print_one_table (&T_table, "T");
  print_one_table (&G_table, "G");
  print_one_table (&Fc_table, "Fc");
  print_one_table (&Ud_table, "Ud");
  print_one_table (&Uq_table, "Uq");
  print_one_table (&Ctl_table, "Ctl");
  print_one_table (&Rg_table, "Rg");
}

void free_one_table (interp_table *pTbl)
{
  free (pTbl->x);
  free (pTbl->y);
  free (pTbl->m);
}

void free_tables ()
{
  free_one_table (&T_table);
  free_one_table (&G_table);
  free_one_table (&Fc_table);
  free_one_table (&Ud_table);
  free_one_table (&Uq_table);
  free_one_table (&Rg_table);
}

double interpolate (interp_table *pTbl, double t)
{
  int i = pTbl->n - 1;
  while (t < pTbl->x[i]) {
    --i;
  }
  return pTbl->y[i] + (t - pTbl->x[i]) * pTbl->m[i];
}

// inputs Vd=R*Id and Vq=R*Iq
void update_inputs (IEEE_Cigre_DLLInterface_Instance* pModel, ArrayMap *pMap, double t, double Vd, double Vq)
{
  double T = interpolate (&T_table, t);
  double G = interpolate (&G_table, t);
  double Fc = interpolate (&Fc_table, t);
  double Ud = interpolate (&Ud_table, t);
  double Uq = interpolate (&Uq_table, t);
  double Ctl = interpolate (&Ctl_table, t);
  double GVrms = 0.001 * G * sqrt (1.5 * (Vd*Vd + Vq*Vq));

  char *pData = (char *) pModel->ExternalInputs;
  memcpy (pData + pMap[0].offset, &T, pMap[0].size);
  memcpy (pData + pMap[1].offset, &G, pMap[1].size);
  memcpy (pData + pMap[2].offset, &Fc, pMap[2].size);
  memcpy (pData + pMap[3].offset, &Ud, pMap[3].size);
  memcpy (pData + pMap[4].offset, &Uq, pMap[4].size);
  memcpy (pData + pMap[5].offset, &Vd, pMap[5].size);
  memcpy (pData + pMap[6].offset, &Vq, pMap[6].size);
  memcpy (pData + pMap[7].offset, &GVrms, pMap[7].size);
  memcpy (pData + pMap[8].offset, &Ctl, pMap[8].size);
}

// need Id and Iq for injection into the simulated grid
void extract_outputs (IEEE_Cigre_DLLInterface_Instance* pModel, ArrayMap *pMap, double *pId, double *pIq)
{
  char *pData = (char *) pModel->ExternalOutputs;
  double Vdc = 0.0;
  double Idc = 0.0;
  memcpy (&Vdc, pData + pMap[0].offset, pMap[0].size);
  memcpy (&Idc, pData + pMap[1].offset, pMap[1].size);
  memcpy (pId, pData + pMap[2].offset, pMap[2].size);
  memcpy (pIq, pData + pMap[3].offset, pMap[3].size);
}

int main( void ) 
{
  show_struct_alignment_requirements ();
  Wrapped_IEEE_Cigre_DLL *pWrap = CreateFirstDLLModel (DLL_NAME);
  if (NULL != pWrap) {
    // overwrite default JSON file with an actual one, knowing this is parameter 0
    union EditValueU val;
    val.Char_Ptr = JSON_FILE1;
    edit_dll_value ((char *)pWrap->pModel->Parameters, 
                      pWrap->pParameterMap[0].offset, 
                      pWrap->pParameterMap[0].dtype, 
                      pWrap->pParameterMap[0].size,
                      val);
    PrintDLLModelParameters (pWrap);
    // initialize the model
    if (NULL != pWrap->Model_FirstCall) {
      pWrap->Model_FirstCall (pWrap->pModel);
    }
    printf("calling CheckParameters\n");
    pWrap->Model_CheckParameters (pWrap->pModel);
    check_messages ("Model_CheckParameters", pWrap->pModel);

    // initialize time-stepping
    initialize_tables ();
    printf("calling Initialize\n");
    initialize_outputs (pWrap->pModel, pWrap->pOutputMap, pWrap->pInfo->NumOutputPorts);
    pWrap->Model_Initialize (pWrap->pModel);
    check_messages ("Model_Initialize", pWrap->pModel);

    // time step loop, matching the DLL's desired time step
    double dt = pWrap->pInfo->FixedStepBaseSampleTime;
    printf("Looping with dt=%g, tmax=%g\n", dt, TMAX);
    double t = 0.0;
    printf("opening %s\n", CSV_NAME);
    FILE *fp = fopen (CSV_NAME, "w");
    write_csv_header (fp, pWrap->pInfo);
    double tstop = TMAX + 0.5 * dt;
    double Rg = interpolate (&Rg_table, t);
    double Id = 0.0;
    double Iq = 0.0;
    double Vd = 0.0;
    double Vq = 0.0;
    while (t <= tstop) {
      // update the inputs for this next DLL step
      pWrap->pModel->Time = t;
      Vd = Rg * Id;
      Vq = Rg * Iq;
      update_inputs (pWrap->pModel, pWrap->pInputMap, t, Vd, Vq);
      pWrap->Model_Outputs (pWrap->pModel);
      extract_outputs (pWrap->pModel, pWrap->pOutputMap, &Id, &Iq);
      write_csv_values (fp, pWrap->pModel, pWrap->pInfo, pWrap->pInputMap, pWrap->pOutputMap, t);
      check_messages ("Model_Outputs", pWrap->pModel);
      t += dt;
    }
    fclose (fp);
    FreeFirstDLLModel (pWrap);
    free_tables ();
  }
  return 0;
}
