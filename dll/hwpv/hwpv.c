// Copyright (C) 2024 Meltran, Inc

/*
This is an example of a power system model written in C, according to the IEEE/Cigre DLL Modeling Standard (API V2).

This hwpv model implements generalized block diagrams per https://pecblocks.readthedocs.io/en/latest/.

Tested only with the bal3_fhf.json model.

November 11, 2024, TEMc
*/

#include <stdio.h>
#include <jansson.h>
#include "IEEE_Cigre_DLLInterface.h"
char ErrorMessage[1000];

/* forward refs */
void print_json(json_t *root);
void print_json_aux(json_t *element, int indent);
void print_json_indent(int indent);
const char *json_plural(size_t count);
void print_json_object(json_t *element, int indent);
void print_json_array(json_t *element, int indent);
void print_json_string(json_t *element, int indent);
void print_json_integer(json_t *element, int indent);
void print_json_real(json_t *element, int indent);
void print_json_true(json_t *element, int indent);
void print_json_false(json_t *element, int indent);
void print_json_null(json_t *element, int indent);

void print_json(json_t *root) { print_json_aux(root, 0); }

void print_json_aux(json_t *element, int indent) {
  switch (json_typeof(element)) {
    case JSON_OBJECT:
      print_json_object(element, indent);
      break;
    case JSON_ARRAY:
      print_json_array(element, indent);
      break;
    case JSON_STRING:
      print_json_string(element, indent);
      break;
    case JSON_INTEGER:
      print_json_integer(element, indent);
      break;
    case JSON_REAL:
      print_json_real(element, indent);
      break;
    case JSON_TRUE:
      print_json_true(element, indent);
      break;
    case JSON_FALSE:
      print_json_false(element, indent);
      break;
    case JSON_NULL:
      print_json_null(element, indent);
      break;
    default:
      fprintf(stderr, "unrecognized JSON type %d\n", json_typeof(element));
  }
}

void print_json_indent(int indent) {
  int i;
  for (i = 0; i < indent; i++) {
    putchar(' ');
  }
}

const char *json_plural(size_t count) { return count == 1 ? "" : "s"; }

void print_json_object(json_t *element, int indent) {
  size_t size;
  const char *key;
  json_t *value;

  print_json_indent(indent);
  size = json_object_size(element);

  printf("JSON Object of %lld pair%s:\n", (long long)size, json_plural(size));
  json_object_foreach(element, key, value) {
    print_json_indent(indent + 2);
    printf("JSON Key: \"%s\"\n", key);
    print_json_aux(value, indent + 2);
  }
}

void print_json_array(json_t *element, int indent) {
  size_t i;
  size_t size = json_array_size(element);
  print_json_indent(indent);

  printf("JSON Array of %lld element%s:\n", (long long)size, json_plural(size));
  for (i = 0; i < size; i++) {
    print_json_aux(json_array_get(element, i), indent + 2);
  }
}

void print_json_string(json_t *element, int indent) {
  print_json_indent(indent);
  printf("JSON String: \"%s\"\n", json_string_value(element));
}

void print_json_integer(json_t *element, int indent) {
  print_json_indent(indent);
  printf("JSON Integer: \"%" JSON_INTEGER_FORMAT "\"\n", json_integer_value(element));
}

void print_json_real(json_t *element, int indent) {
  print_json_indent(indent);
  printf("JSON Real: %f\n", json_real_value(element));
}

void print_json_true(json_t *element, int indent) {
  (void)element;
  print_json_indent(indent);
  printf("JSON True\n");
}

void print_json_false(json_t *element, int indent) {
  (void)element;
  print_json_indent(indent);
  printf("JSON False\n");
}

void print_json_null(json_t *element, int indent) {
  (void)element;
  print_json_indent(indent);
  printf("JSON Null\n");
}

// ----------------------------------------------------------------------
// Trained HWPV model coefficients read from JSON file
//  1 - allocated in the DLL in Model_CheckParameters, 
//      keep pointer in a state variable (real64_T) provided by caller
//      TODO: verify the spec requires state variable allocation before
//            calling Model_CheckParameters. If not, use Model_Initialize
//  2 - freed in the DLL in Model_Terminate

typedef struct _MyH {
  int32_T nin;
  int32_T nout;
  int32_T na;
  int32_T nb;
  int32_T nk;
  real64_T ***a;     // index nout, nin, na
  real64_T ***b;     // index nout, nin, nb
  real64_T ***uhist; // index nout, nin, nb REVISIT
  real64_T ***yhist; // index nout, nin, na REVISIT
  real64_T *ysum;    // index nout
} MyH;

typedef struct _MyF {
  int32_T nin;
  int32_T nout;
  int32_T nhid;
  real64_T **n0w; // index nhid, nin
  real64_T **n2w; // index nout, nhid
  real64_T *n0b;  // index nhid
  real64_T *n2b;  // index nout
  real64_T *yhid; // index nhid
  real64_T *yout; // index nout
} MyF;

typedef struct _MyCoefficients {
  // training time step for H(z)
  real64_T t_step;
  // model dimensions
  int32_T na;
  int32_T nb;
  int32_T nk;
  int32_T nh1;
  int32_T nh2;
  int32_T nin;
  int32_T nout;
  // activation function must be tanh
  char *activation;
  // signal names
  char **col_u;
  char **col_y;
  char **col_t;
  // normalization factors, nin+nout, ordered as in col_u and col_y
  real64_T *pScales;
  real64_T *pOffsets;
  real64_T *pMins;
  real64_T *pMaxs;
  MyH *pH1;
  MyF *pF1;
  MyF *pF2;
  // normalized inputs
  real64_T *ub;
} MyCoefficients;

// ----------------------------------------------------------------------
// Structures defining inputs, outputs, parameters and program structure
// to be called by the DLLImport Tool
// ----------------------------------------------------------------------

typedef struct _MyModelInputs {
  real64_T T;
  real64_T G;
  real64_T Fc;
  real64_T Ud;
  real64_T Uq;
  real64_T Vd;
  real64_T Vq;
  real64_T GVrms;
  real64_T Ctl;
} MyModelInputs;

IEEE_Cigre_DLLInterface_Signal InputSignals[] = {
  [0] = {
    .Name = "T",
    .Description = "Panel temperature",
    .Unit = "C",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [1] = {
    .Name = "G",
    .Description = "Solar irradiance",
    .Unit = "W/m2",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [2] = {
    .Name = "Fc",
    .Description = "Frequency control",
    .Unit = "Hz",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [3] = {
    .Name = "Ud",
    .Description = "d-axis voltage control",
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [4] = {
    .Name = "Uq",
    .Description = "q-axis voltage control",
    .Unit = "pu",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [5] = {
    .Name = "Vd",
    .Description = "d-axis terminal voltage",
    .Unit = "V",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [6] = {
    .Name = "Vq",
    .Description = "q-axis terminal voltage",
    .Unit = "V",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [7] = {
    .Name = "GVrms",
    .Description = "Product of G and AC terminal voltage",
    .Unit = "V*kW/m2",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [8] = {
    .Name = "Ctl",
    .Description = "State 0=start,1=grid formed,2=grid following",
    .Unit = "",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  }
};

typedef struct _MyModelOutputs {
  real64_T Vdc;
  real64_T Idc;
  real64_T Id;
  real64_T Iq;
} MyModelOutputs;

IEEE_Cigre_DLLInterface_Signal OutputSignals[] = {
  [0] = {
    .Name = "Vdc",
    .Description = "DC Bus Voltage",
    .Unit = "V",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [1] = {
    .Name = "Idc",
    .Description = "DC Current",
    .Unit = "A",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [2] = {
    .Name = "Id",
    .Description = "AC d-axis Current Injection",
    .Unit = "A",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  },
  [3] = {
    .Name = "Iq",
    .Description = "AC q-axis Current Injection",
    .Unit = "A",
    .DataType = IEEE_Cigre_DLLInterface_DataType_real64_T,
    .Width = 1
  }
};

typedef struct _MyModelParameters {
  char_T *pFileName;
} MyModelParameters;

// Define Parameters
IEEE_Cigre_DLLInterface_Parameter Parameters[] = {
  [0] = {
    .Name = "JSONfile",
    .Description = "JSON file with trained model",
    .Unit = "",
    .DataType = IEEE_Cigre_DLLInterface_DataType_c_string_T,
    .FixedValue = 1,  // 0 for parameters which can be modified at any time, 1 for parameters which need to be defined at T0 but cannot be changed.
    .DefaultValue.Char_Ptr = "bal3_fhf.json" // no minimum or maximum value
  }
};

IEEE_Cigre_DLLInterface_Model_Info Model_Info = {
  .DLLInterfaceVersion = { 0, 0, 0, 8 },
  .ModelName = "hwpv",
  .ModelVersion = "0.0.0.8",
  .ModelDescription = "hwpv; generalized block diagram models",
  .GeneralInformation = "General Information",
  .ModelCreated = "November 11, 2024",
  .ModelCreator = "temc",
  .ModelLastModifiedDate = "November 11, 2024",
  .ModelLastModifiedBy = "temc",
  .ModelModifiedComment = "Version 0.0.0.8 for IEEE/Cigre DLL API V2",
  .ModelModifiedHistory = "History of Changes: V0.0.0.8 Initial model for API V1",
  .FixedStepBaseSampleTime = 0.002,                   // Time Step sampling time (sec) VARIABLE

  // Inputs
  .NumInputPorts = 9,
  .InputPortsInfo = InputSignals,

  // Outputs
  .NumOutputPorts = 4,
  .OutputPortsInfo = OutputSignals,

  // Parameters
  .NumParameters = 1,
  .ParametersInfo = Parameters,

  // Number of State Variables - this DLL will create its own internal storage
  .NumIntStates = 4,    // store a pointer in the memory for these?!
  .NumFloatStates = 0,
  .NumDoubleStates = 0
};

// ----------------------------------------------------------------
// Subroutines that can be called by the main power system program
// ----------------------------------------------------------------
__declspec(dllexport) const IEEE_Cigre_DLLInterface_Model_Info* __cdecl Model_GetInfo() {
  /* Returns Model Information
  */
  return &Model_Info;
};

char **make_string_array (json_t *pJson)
{
  int n = json_array_size (pJson);
  char **ret = malloc (sizeof (char *) * n);
  for (int i=0; i < n; i++) {
    json_t *jval = json_array_get (pJson, i);
    const char *cstr = json_string_value (jval);
    ret[i] = malloc (strlen(cstr)+1);
    strcpy (ret[i], cstr);
  }
  return ret;
}

MyF *load_F_block (json_t *pJson)
{
  MyF *pF = malloc (sizeof (*pF));
  pF->nin = pF->nout = pF->nhid = 0;
  pF->n0w = pF->n2w = NULL;
  pF->n0b = pF->n2b = pF->yhid = pF->yout = NULL;
  const char *key;
  json_t *val;
  json_object_foreach (pJson, key, val) {
    if (0 == strcmp(key, "n_in")) {
      pF->nin = json_integer_value (val);
    } else if (0 == strcmp(key, "n_hid")) {
      pF->nhid = json_integer_value (val);
    } else if (0 == strcmp(key, "n_out")) {
      pF->nout = json_integer_value (val);
      pF->n0w = malloc (sizeof (real64_T *) * pF->nhid);
      for (int i=0; i < pF->nhid; i++) {
        pF->n0w[i] = malloc (sizeof (real64_T) * pF->nin);
      }
      pF->n2w = malloc (sizeof (real64_T *) * pF->nout);
      for (int i=0; i < pF->nout; i++) {
        pF->n2w[i] = malloc (sizeof (real64_T) * pF->nhid);
      }
      pF->n0b = malloc (sizeof (real64_T) * pF->nhid);
      pF->n2b = malloc (sizeof (real64_T) * pF->nout);
      pF->yhid = malloc (sizeof (real64_T) * pF->nhid);
      pF->yout = malloc (sizeof (real64_T) * pF->nout);
    } else if (0 == strcmp(key, "net.0.weight")) {
      for (int i=0; i < pF->nhid; i++) {
        json_t *row = json_array_get (val, i);
        for (int j=0; j < pF->nin; j++) {
          pF->n0w[i][j] = json_real_value (json_array_get (row, j));
        }
      }
    } else if (0 == strcmp(key, "net.2.weight")) {
      for (int i=0; i < pF->nout; i++) {
        json_t *row = json_array_get (val, i);
        for (int j=0; j < pF->nhid; j++) {
          pF->n2w[i][j] = json_real_value (json_array_get (row, j));
        }
      }
    } else if (0 == strcmp(key, "net.0.bias")) {
      for (int i=0; i < pF->nhid; i++) {
        pF->n0b[i] = json_real_value (json_array_get (val, i));
      }
    } else if (0 == strcmp(key, "net.2.bias")) {
      for (int i=0; i < pF->nout; i++) {
        pF->n2b[i] = json_real_value (json_array_get (val, i));
      }
    }
  }
  return pF;
}

void evaluate_F_block (MyF *pF, real64_T *u)
{
  for (int i = 0; i < pF->nhid; i++) {
    pF->yhid[i] = pF->n0b[i];
    for (int j = 0; j < pF->nin; j++) {
      pF->yhid[i] += pF->n0w[i][j] * u[j];
    }
    pF->yhid[i] = tanh (pF->yhid[i]);
  }
  for (int i = 0; i < pF->nout; i++) {
    pF->yout[i] = pF->n2b[i];
    for (int j = 0; j < pF->nhid; j++) {
      pF->yout[i] += pF->n2w[i][j] * pF->yhid[j];
    }
  }
}

MyH *load_H_block (json_t *pJson)
{
  char buf[100];
  int row, col;
  MyH *pH = malloc (sizeof (*pH));
  pH->nin = pH->nout = pH->na = pH->nb = pH->nk = 0;
  pH->a = pH->b = pH->uhist = pH->yhist = NULL;
  pH->ysum = NULL;
  const char *key;
  json_t *val;
  json_object_foreach (pJson, key, val) {
    if (0 == strcmp(key, "n_in")) {
      pH->nin = json_integer_value (val);
    } else if (0 == strcmp(key, "n_out")) {
      pH->nout = json_integer_value (val);
    } else if (0 == strcmp(key, "n_a")) {
      pH->na = json_integer_value (val);
    } else if (0 == strcmp(key, "n_b")) {
      pH->nb = json_integer_value (val);
    } else if (0 == strcmp(key, "n_k")) {
      pH->nk = json_integer_value (val);
      pH->a = malloc (sizeof (real64_T **) * pH->nout);
      pH->b = malloc (sizeof (real64_T **) * pH->nout);
      pH->uhist = malloc (sizeof (real64_T **) * pH->nout);
      pH->yhist = malloc (sizeof (real64_T **) * pH->nout);
      pH->ysum = malloc (sizeof (real64_T) * pH->nout);
      for (int i = 0; i < pH->nout; i++) {
        pH->a[i] = malloc (sizeof (real64_T *) * pH->nin);
        pH->b[i] = malloc (sizeof (real64_T *) * pH->nin);
        pH->uhist[i] = malloc (sizeof (real64_T *) * pH->nin);
        pH->yhist[i] = malloc (sizeof (real64_T *) * pH->nin);
        for (int j = 0; j < pH->nin; j++) {
          pH->a[i][j] = malloc (sizeof (real64_T) * pH->na);
          pH->yhist[i][j] = malloc (sizeof (real64_T) * pH->na);
          memset (pH->yhist[i][j], 0, sizeof (real64_T) * pH->na);
          pH->b[i][j] = malloc (sizeof (real64_T) * pH->nb);
          pH->uhist[i][j] = malloc (sizeof (real64_T) * pH->nb);
          memset (pH->uhist[i][j], 0, sizeof (real64_T) * pH->nb);
        }
      }
    } else if (0 == strncmp (key, "a_", 2)) {
      sscanf (key, "%[^_]_%d_%d", buf, &row, &col);
      //printf("   found %s and parsed %s[%d,%d] size %zd\n", key, buf, row, col, json_array_size(val));
      for (int i=0; i < pH->na; i++) {
        pH->a[row][col][i] = json_real_value (json_array_get (val, i));
      }
    } else if (0 == strncmp (key, "b_", 2)) {
      sscanf (key, "%[^_]_%d_%d", buf, &row, &col);
      //printf("   found %s and parsed %s[%d,%d] size %zd\n", key, buf, row, col, json_array_size(val));
      for (int i=0; i < pH->nb; i++) {
        pH->b[row][col][i] = json_real_value (json_array_get (val, i));
      }
    }
  }
  return pH;
}

void evaluate_H_block (MyH *pH, real64_T *u)
{
//for (int i = 0; i < pH->nout; i++) {
//  for (int j = 0; j < pH->nin; j++) {
//    pH->ysum[i] = u[j];
//  }
//}
//return;
  for (int i = 0; i < pH->nout; i++) {
    pH->ysum[i] = 0.0;
    for (int j = 0; j < pH->nin; j++) {
      // local convenience pointers
      real64_T *uh = pH->uhist[i][j];
      real64_T *yh = pH->yhist[i][j];
      real64_T *a = pH->a[i][j];
      real64_T *b = pH->b[i][j];
      // shift the input history one point, add the latest input
      for (int k = pH->nb-1; k > 0; k--) {
        uh[k] = uh[k-1];
      }
      uh[0] = u[j];
      // evaluate H(z) for this input-output channel pair
      real64_T ynew = 0.0;
      for (int k = 0; k < pH->nb; k++) {
        ynew += b[k] * uh[k];
      }
      for (int k = 0; k < pH->na; k++) {
        ynew -= a[k] * yh[k];
      }
      // shift the output history one point, add the latest output
      for (int k = pH->na-1; k > 0; k--) {
        yh[k] = yh[k-1];
      }
//    if (fabs(yh[0] - ynew) > 1.0e-5) {
//      printf("evaluate_H_block [%d][%d] changes ynew from %g to %g\n", i, j, yh[0], ynew);
//      printf(" k            ub            uh             b            yh             a\n");
//      for (int k=0; k < pH->na; k++) {
//        printf("%2d %13g %13g %13g %13g %13g\n", k, u[k], uh[k], b[k], yh[k], a[k]);
//      }
//      //exit (EXIT_FAILURE);
//    }
      yh[0] = ynew;
      // accumulate contributions from inputs to outputs
      pH->ysum[i] += ynew;
    }
  }
}

void initialize_H_history (MyH *pH, real64_T *u)
{
  for (int i = 0; i < pH->nout; i++) {
    for (int j = 0; j < pH->nin; j++) {
      // local convenience pointers
      real64_T *uh = pH->uhist[i][j];
      real64_T *yh = pH->yhist[i][j];
      real64_T *a = pH->a[i][j];
      real64_T *b = pH->b[i][j];
      real64_T denominator = 1.0;
      real64_T numerator = 0.0;
      for (int k = 0; k < pH->nb; k++) {
        uh[k] = u[j];
        numerator += b[k];
      }
      for (int k = 0; k < pH->na; k++) {
        denominator += a[k];
      }
      real64_T ynew = u[j] * numerator / denominator;
      for (int k = 0; k < pH->na; k++) {
        yh[k] = ynew;
      }
      //printf("initialize_H_block [%d][%d] ynew=%g\n", i, j, ynew);
      //printf(" k            ub            uh             b            yh             a\n");
      //for (int k=0; k < pH->na; k++) {
      //  printf("%2d %13g %13g %13g %13g %13g\n", k, u[k], uh[k], b[k], yh[k], a[k]);
      //}
      // exit (EXIT_FAILURE);
    }
  }
}

void load_normalization_factors (MyCoefficients *pCoeff, json_t *pJson)
{
//  print_json_indent(indent);
  int n = json_object_size (pJson);
  pCoeff->pOffsets = malloc (sizeof (real64_T) * n);
  pCoeff->pScales = malloc (sizeof (real64_T) * n);
  pCoeff->pMins = malloc (sizeof (real64_T) * n);
  pCoeff->pMaxs = malloc (sizeof (real64_T) * n);

  const char *key1, *key2;
  json_t *val1, *val2;

  int i = 0;
  json_object_foreach (pJson, key1, val1) {
    json_object_foreach (val1, key2, val2) {
      if (0 == strcmp(key2, "scale")) {
        pCoeff->pScales[i] = json_real_value (val2);
      } else if (0 == strcmp(key2, "offset")) {
        pCoeff->pOffsets[i] = json_real_value (val2);
      } else if (0 == strcmp(key2, "max")) {
        pCoeff->pMaxs[i] = json_real_value (val2);
      } else if (0 == strcmp(key2, "min")) {
        pCoeff->pMins[i] = json_real_value (val2);
      }
    }
    i++;
  }
}

MyCoefficients *get_coefficient_pointer (int32_T *pVals)
{
  unsigned long long part0 = ((unsigned long long) pVals[0] << 48) & 0xFFFF000000000000;
  unsigned long long part1 = ((unsigned long long) pVals[1] << 32) & 0x0000FFFF00000000;
  unsigned long long part2 = ((unsigned long long) pVals[2] << 16) & 0x00000000FFFF0000;
  unsigned long long part3 = (unsigned long long) pVals[3] & 0x000000000000FFFF;
  unsigned long long address = part0 | part1 | part2 | part3;
//  printf("get_coefficient_pointer: %lld, %lld, %lld, %lld yields %p\n", part0, part1, part2, part3, (void *)address);
  return (MyCoefficients *) address;
}

void set_coefficient_pointer (MyCoefficients *ptr, int32_T *pVals)
{
  unsigned long long address = (unsigned long long) ptr;
  pVals[0] = (address >> 48) & 0xFFFF;
  pVals[1] = (address >> 32) & 0xFFFF;
  pVals[2] = (address >> 16) & 0xFFFF;
  pVals[3] = address & 0xFFFF;
//  printf("set_coefficient_pointer: %d, %d, %d, %d from %p\n", pVals[0], pVals[1], pVals[2], pVals[3], ptr);
}

// ----------------------------------------------------------------
__declspec(dllexport) int32_T __cdecl Model_CheckParameters(IEEE_Cigre_DLLInterface_Instance* instance) {
  /*   Checks the parameters on the given range
     Arguments: Instance specific model structure containing Inputs, Parameters and Outputs
     Return:  Integer status 0 (normal), 1 if messages are written, 2 for errors.  See IEEE_Cigre_DLLInterface_types.h
  */
  // Parameter checks done by the program
  // Note - standard min/max checks should be done by the higher level GUI/Program
  MyModelParameters* parameters = (MyModelParameters*)instance->Parameters;
  MyCoefficients *pCoeff = NULL;

  char_T *pFileName = parameters->pFileName;
  json_error_t json_error;
  json_t *pJson = json_load_file (pFileName, 0, &json_error);
  if (NULL == pJson) {
    printf(" failed to read trained model from %s\n", pFileName);
  } else {
//    print_json (pJson);
    pCoeff = malloc (sizeof (*pCoeff));
    pCoeff->activation=NULL;
    pCoeff->col_u=NULL;
    pCoeff->col_y=NULL;
    pCoeff->col_t=NULL;
    pCoeff->pScales=NULL;
    pCoeff->pOffsets=NULL;
    pCoeff->pMins=NULL;
    pCoeff->pMaxs=NULL;
    pCoeff->ub=NULL;

    const char *key;
    json_t *value;
    json_object_foreach (pJson, key, value) {
      if (0 == strcmp (key, "t_step")) {
        pCoeff->t_step = json_real_value (value);
      } else if (0 == strcmp (key, "na")) {
        pCoeff->na = json_integer_value (value);
      } else if (0 == strcmp (key, "nb")) {
        pCoeff->nb = json_integer_value (value);
      } else if (0 == strcmp (key, "nk")) {
        pCoeff->nk = json_integer_value (value);
      } else if (0 == strcmp (key, "nh1")) {
        pCoeff->nh1 = json_integer_value (value);
      } else if (0 == strcmp (key, "nh2")) {
        pCoeff->nh2 = json_integer_value (value);
      } else if (0 == strcmp (key, "activation")) {
        const char *cstr = json_string_value (value);
        pCoeff->activation = malloc (strlen(cstr)+1);
        strcpy (pCoeff->activation, cstr);
      } else if (0 == strcmp (key, "COL_T")) {
        pCoeff->col_t = make_string_array (value);
      } else if (0 == strcmp (key, "COL_Y")) {
        pCoeff->nout = json_array_size(value);
        pCoeff->col_y = make_string_array (value);
      } else if (0 == strcmp (key, "COL_U")) {
        pCoeff->nin = json_array_size(value);
        pCoeff->ub = malloc (sizeof(real64_T) * pCoeff->nin);
        pCoeff->col_u = make_string_array (value);
      } else if (0 == strcmp (key, "normfacs")) {
        load_normalization_factors (pCoeff, value);
      } else if (0 == strcmp (key, "F1")) {
        pCoeff->pF1 = load_F_block (value);
      } else if (0 == strcmp (key, "F2")) {
        pCoeff->pF2 = load_F_block (value);
      } else if (0 == strcmp (key, "H1")) {
        pCoeff->pH1 = load_H_block (value);
      }
    }
    json_decref (pJson);
    printf("Parsed nin=%d, nout=%d, t_step=%g, na=%d, nb=%d, nk=%d, nh1=%d, nh2=%d, activation=%s\n", 
           pCoeff->nin, pCoeff->nout, pCoeff->t_step, pCoeff->na, pCoeff->nb, pCoeff->nk, pCoeff->nh1, pCoeff->nh2, pCoeff->activation);
    printf("  col_t=%s\n", pCoeff->col_t[0]);
    printf("Inputs: scale, offset, min, max\n");
    for (int i = 0; i < pCoeff->nin; i++) {
      printf("  col_u[%d]=%6s %13g %13g %13g %13g\n", i, pCoeff->col_u[i], pCoeff->pScales[i], pCoeff->pOffsets[i], pCoeff->pMins[i], pCoeff->pMaxs[i]);
    }
    printf("Outputs: scale, offset, min, max\n");
    for (int i = 0; i < pCoeff->nout; i++) {
      int j = i + pCoeff->nin;
      printf("  col_y[%d]=%6s %13g %13g %13g %13g\n", i, pCoeff->col_y[i], pCoeff->pScales[j], pCoeff->pOffsets[j], pCoeff->pMins[j], pCoeff->pMaxs[j]);
    }
    printf("F1: nin=%d, nout=%d, nhid=%d\n", pCoeff->pF1->nin, pCoeff->pF1->nout, pCoeff->pF1->nhid);
//  for (int i=0; i < pCoeff->pF1->nhid; i++) {
//    printf("n0w[%d]\n", i);
//    for (int j=0; j < pCoeff->pF1->nin; j++) {
//      printf("  %d=%g\n", j, pCoeff->pF1->n0w[i][j]);
//    }
//  }
    printf("H1: nin=%d, nout=%d, na=%d, nb=%d, nk=%d\n", pCoeff->pH1->nin, pCoeff->pH1->nout, pCoeff->pH1->na, pCoeff->pH1->nb, pCoeff->pH1->nk);
//  for (int i = 0; i < pCoeff->pH1->na; i++) {
//    printf("  a_0_0[%d]=%g\n", i, pCoeff->pH1->a[0][0][i]);
//  }
//  for (int i = 0; i < pCoeff->pH1->nb; i++) {
//    printf("  b_0_0[%d]=%g\n", i, pCoeff->pH1->b[0][0][i]);
//  }
    printf("F2: nin=%d, nout=%d, nhid=%d\n", pCoeff->pF2->nin, pCoeff->pF2->nout, pCoeff->pF2->nhid);
    set_coefficient_pointer (pCoeff, instance->IntStates);
  }

  real64_T delt = Model_Info.FixedStepBaseSampleTime;

  ErrorMessage[0] = '\0';
//if (TE < 2.0*delt) {
//  // write error message
//  sprintf_s(ErrorMessage, sizeof(ErrorMessage), "SCRX9 Error - Parameter TE is: %f, but has been reset to be 2 times the time step: %f .\n", TE, delt);
//  parameters->TE = 2.0*delt;
//}
//if (TB < 2.0*delt) {
//  // write error message
//  sprintf_s(ErrorMessage, sizeof(ErrorMessage), "SCRX9 Error - Parameter TB is: %f, but has been reset to be 2 times the time step: %f .\n", TB, delt);
//  parameters->TB = 2.0*delt;
//}
  instance->LastGeneralMessage = ErrorMessage;
  return IEEE_Cigre_DLLInterface_Return_OK;
};

// ----------------------------------------------------------------
__declspec(dllexport) int32_T __cdecl Model_Initialize(IEEE_Cigre_DLLInterface_Instance* instance) {
  /*   Initializes the system by resetting the internal states
     Arguments: Instance specific model structure containing Inputs, Parameters and Outputs
     Return:  Integer status 0 (normal), 1 if messages are written, 2 for errors.  See IEEE_Cigre_DLLInterface_types.h
  */
  //
  // Note that the initial conditions for all models are determined by the main calling program
  // and are passed to this routine via the instance->ExternalOutputs vector.
  // instance->ExternalOutputs is normally the output of this routine, but in the first time step
  // the main program must set the instance->ExternalOutputs to initial values.
  //
  MyModelParameters* parameters = (MyModelParameters*)instance->Parameters;
  real64_T delt = Model_Info.FixedStepBaseSampleTime;
  real64_T *inputs = (real64_T *)instance->ExternalInputs;
  real64_T *outputs = (real64_T *)instance->ExternalOutputs;
  printf("IntStates %d %d %d %d\n", instance->IntStates[0], instance->IntStates[1], instance->IntStates[2], instance->IntStates[3]);
  MyCoefficients *pCoeff = get_coefficient_pointer (instance->IntStates);
  printf("Restored t_step=%g from %p\n", pCoeff->t_step, pCoeff);

  ErrorMessage[0] = '\0';

  instance->LastGeneralMessage = ErrorMessage;
  return IEEE_Cigre_DLLInterface_Return_OK;
};

// ----------------------------------------------------------------
__declspec(dllexport) int32_T __cdecl Model_Outputs(IEEE_Cigre_DLLInterface_Instance* instance) {
  /*   Calculates output equation
     Arguments: Instance specific model structure containing Inputs, Parameters and Outputs
     Return:  Integer status 0 (normal), 1 if messages are written, 2 for errors.  See IEEE_Cigre_DLLInterface_types.h
  */
  ErrorMessage[0] = '\0';

  MyModelParameters* parameters = (MyModelParameters*)instance->Parameters;
  real64_T delt = Model_Info.FixedStepBaseSampleTime;
  real64_T *inputs = (real64_T *)instance->ExternalInputs;
  real64_T *outputs = (real64_T *)instance->ExternalOutputs;
  MyCoefficients *pCoeff = get_coefficient_pointer (instance->IntStates);

  // normalize the input vector
  for (int i = 0; i < pCoeff->nin; i++) {
    pCoeff->ub[i] = (inputs[i] - pCoeff->pOffsets[i]) / pCoeff->pScales[i];
  }

  // evaluate F1
  evaluate_F_block (pCoeff->pF1, pCoeff->ub);

  // evaluate H1
  if (instance->Time <= 0.0) {
    initialize_H_history (pCoeff->pH1, pCoeff->pF1->yout);
  }
  evaluate_H_block (pCoeff->pH1, pCoeff->pF1->yout);

  // evaluate F2
  evaluate_F_block (pCoeff->pF2, pCoeff->pH1->ysum);

  // de-normalize the output vector
  for (int i = 0; i < pCoeff->nout; i++) {
    outputs[i] = pCoeff->pF2->yout[i] * pCoeff->pScales[i+pCoeff->nin] + pCoeff->pOffsets[i+pCoeff->nin];
  }

  instance->LastGeneralMessage = ErrorMessage;
  return IEEE_Cigre_DLLInterface_Return_OK;
};

void free_F_block (MyF *pF)
{
  for (int i=0; i < pF->nhid; i++) {
    free (pF->n0w[i]);
  }
  for (int i=0; i < pF->nout; i++) {
    free (pF->n2w[i]);
  }
  free (pF->n0w);
  free (pF->n2w);
  free (pF->n0b);
  free (pF->n2b);
  free (pF->yhid);
  free (pF->yout);
  free (pF);
}

void free_H_block (MyH *pH)
{
  for (int i=0; i < pH->nout; i++) {
    for (int j=0; j < pH->nin; j++) {
      free (pH->a[i][j]);
      free (pH->b[i][j]);
      free (pH->uhist[i][j]);
      free (pH->yhist[i][j]);
    }
    free (pH->a[i]);
    free (pH->b[i]);
    free (pH->uhist[i]);
    free (pH->yhist[i]);
  }
  free (pH->a);
  free (pH->b);
  free (pH->uhist);
  free (pH->yhist);
  free (pH->ysum);
  free (pH);
}

// ----------------------------------------------------------------
__declspec(dllexport) int32_T __cdecl Model_Terminate(IEEE_Cigre_DLLInterface_Instance* instance) {
  /*   Destroys any objects allocated by the model code 
  */
  MyCoefficients *pCoeff = get_coefficient_pointer (instance->IntStates);

  free (pCoeff->activation);

  for (int i=0; i<pCoeff->nin; i++) {
    free (pCoeff->col_u[i]);
  }
  for (int i=0; i<pCoeff->nout; i++) {
    free (pCoeff->col_y[i]);
  }
  for (int i=0; i<1; i++) {
    free (pCoeff->col_t[i]);
  }
  free (pCoeff->col_u);
  free (pCoeff->col_y);
  free (pCoeff->col_t);

  free (pCoeff->pOffsets);
  free (pCoeff->pScales);
  free (pCoeff->pMins);
  free (pCoeff->pMaxs);

  free (pCoeff->ub);

  free_H_block (pCoeff->pH1);
  free_F_block (pCoeff->pF1);
  free_F_block (pCoeff->pF2);

  free (pCoeff);

  ErrorMessage[0] = '\0';
  instance->LastGeneralMessage = ErrorMessage;

  return IEEE_Cigre_DLLInterface_Return_OK;
};

// ----------------------------------------------------------------
__declspec(dllexport) int32_T __cdecl Model_PrintInfo() {
  /* Prints Model Information once
  */
  int Printed = 0;
  if (!Printed) {
    printf("Cigre/IEEE DLL Standard\n");
    printf("Model name:       %s\n", Model_Info.ModelName);
    printf("Model version:      %s\n", Model_Info.ModelVersion);
    printf("Model description:    %s\n", Model_Info.ModelDescription);
    printf("Model general info:   %s\n", Model_Info.GeneralInformation);
    printf("Model created on:     %s\n", Model_Info.ModelCreated);
    printf("Model created by:     %s\n", Model_Info.ModelCreator);
    printf("Model last modified:  %s\n", Model_Info.ModelLastModifiedDate);
    printf("Model last modified by: %s\n", Model_Info.ModelLastModifiedBy);
    printf("Model modified comment: %s\n", Model_Info.ModelModifiedComment);
    printf("Model modified history: %s\n", Model_Info.ModelModifiedHistory);
    printf("Time Step Sampling Time (sec): %0.5g\n", Model_Info.FixedStepBaseSampleTime);
    switch (Model_Info.EMT_RMS_Mode) {
      case 1:
        printf("EMT/RMS mode:       EMT\n");
        break;
      case 2:
        printf("EMT/RMS mode:       RMS\n");
        break;
      case 3:
        printf("EMT/RMS mode:       EMT and RMS\n");
        break;
      default:
        printf("EMT/RMS mode:       <not available>\n");
    }
    printf("Number of inputs:     %d\n", Model_Info.NumInputPorts);
    printf("Input description:\n");
    for (int k = 0; k < Model_Info.NumInputPorts; k++) {
      printf("  %s\n", Model_Info.InputPortsInfo[k].Name);
    }
    printf("Number of outputs:    %d\n", Model_Info.NumOutputPorts);
    printf("Output description:\n");
    for (int k = 0; k < Model_Info.NumOutputPorts; k++) {
      printf("  %s\n", Model_Info.OutputPortsInfo[k].Name);
    }

    printf("Number of parameters:   %d\n", Model_Info.NumParameters);
    printf("Parameter description:");
    for (int k = 0; k < Model_Info.NumParameters; k++) {
      printf("  %s\n", Model_Info.ParametersInfo[k].Name);
    }

    printf("Number of int  state variables:   %d\n", Model_Info.NumIntStates);
    printf("Number of float  state variables:   %d\n", Model_Info.NumFloatStates);
    printf("Number of double state variables:   %d\n", Model_Info.NumDoubleStates);
    printf("\n");
    fflush(stdout);
  }
  Printed = 1;

  return IEEE_Cigre_DLLInterface_Return_OK;
};
