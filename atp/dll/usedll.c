#undef RC_INVOKED
#define _WINGDI_H
#define _WINUSER_H
#define _WINNLS_H
#define _WINVER_H
#define _WINNETWK_H
#define _WINREG_H
#define _WINSVC_H
#define WIN32_LEAN_AND_MEAN
#include <windows.h>

#define MINDELTAT 1.0e-10

typedef int (*DLLFUNC)(double[]);

double cfundll_(double argv[])
{
	/* argv[0] = Time */
	/* argv[1] = StopTime */

	static HINSTANCE hDLL=NULL;
	static DLLFUNC   DllFunc=NULL;
	static int nval=0;
	int end;

	if(argv[0]<=0.0&&DllFunc==NULL){
    printf("\nTry to load DLL.\n");
		if( (hDLL=LoadLibrary("DLLfunc.dll"))!=NULL){
      printf("  LoadLibrary succeeded.\n");
			DllFunc=(DLLFUNC)GetProcAddress(hDLL,"cdllfun_");
			printf("  GetProcAddress succeeded on cdllfun_.\n");
		}
	}
	if( DllFunc!=NULL ){
		if(argv[0]>=argv[1]-MINDELTAT) end=1;
		else end=0;
		nval = (DllFunc)(argv);
		if(end==1){
			FreeLibrary(hDLL);
			DllFunc=NULL;
			hDLL   =NULL;
			printf("\nDLL is unloaded\n");
		}
	}
	return nval;
}
