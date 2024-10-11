// From https://learn.microsoft.com/en-us/windows/win32/dlls/using-run-time-dynamic-linking
 
#include <windows.h> 
#include <stdio.h> 
 
typedef int (__cdecl *MYPROC)(void); 
 
int main( void ) 
{ 
  HINSTANCE hinstLib; 
  MYPROC ProcAdd; 
  BOOL fFreeResult, fRunTimeLinkSuccess = FALSE;
 
  hinstLib = LoadLibrary(TEXT("GFM_GFL_IBR.dll")); 
  if (hinstLib != NULL) { 
    ProcAdd = (MYPROC) GetProcAddress(hinstLib, "Model_PrintInfo"); 
    if (NULL != ProcAdd) {
      fRunTimeLinkSuccess = TRUE;
      (ProcAdd) (); 
    }
    fFreeResult = FreeLibrary(hinstLib); 
  } 

  if (!fRunTimeLinkSuccess) {
    printf ("Unable to call Model_PrintInfo from the DLL.\n");
  }
  return 0;
}
