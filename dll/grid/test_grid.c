// Copyright (C) 2024-26 Meltran, Inc

#define TMAX 0.2
#define DT 1.0e-5
#define VBASE 600.0
#define SBASE 1.0e6
#define XPU 0.20
#define RPU 0.01
#define VANG 11.54  // inverter terminal leads source by this many degrees, want 1 = sin(deg)/Xpu

#define CSV_NAME "grid.csv"

#define _USE_MATH_DEFINES
#include <stdio.h> 
#include <math.h>

int main( void ) 
{
  double t = 0.0, dt = DT;
  double omega = 120.0 * M_PI;
  double Zbase = VBASE * VBASE / SBASE;
  double res = Zbase * RPU;
  double x = Zbase * XPU;
  double ind = x / omega;
  double Vmag = VBASE * sqrt (2.0 / 3.0);
  double rad120 = 120.0 * M_PI / 180.0;
  double radAng = VANG * M_PI / 180.0;
  double Vsa, Vsb, Vsc, Vta, Vtb, Vtc, Ia, Ib, Ic, P;
  double Ha = 0.0, Hb = 0.0, Hc = 0.0; // trapezoidal integration history currents
  double rl_y, rl_zi, rl_yi; // RL adjustments

  // RL integration adjustments
  rl_y = 1.0 / (res + 2.0 * ind / dt);
  rl_zi = 1.0 - 2.0 * res * rl_y;
  rl_yi = 2.0 * rl_y * (1.0 - res * rl_y);

  printf("Looping with dt=%g, tmax=%g, tau=%g\n", dt, TMAX, ind/res);
  printf("opening %s\n", CSV_NAME);
  FILE *fp = fopen (CSV_NAME, "w");
  fprintf (fp, "t,Vsa,Vsb,Vsc,Vta,Vtb,Vtc,Ia,Ib,Ic,P\n");
  double tstop = TMAX + 0.5 * dt;

  while (t <= tstop) {
    // infinite bus source voltages behind the impedance
    Vsa = Vmag * sin (omega*t);
    Vsb = Vmag * sin (omega*t - rad120);
    Vsc = Vmag * sin (omega*t + rad120);
    // inverter average source voltages to be created by the DLL
    Vta = Vmag * sin (omega*t + radAng);
    Vtb = Vmag * sin (omega*t + radAng - rad120);
    Vtc = Vmag * sin (omega*t + radAng + rad120);
    // SMIB impedance currents at this time step
    Ia = Ha + rl_y * (Vta - Vsa);
    Ib = Hb + rl_y * (Vtb - Vsb);
    Ic = Hc + rl_y * (Vtc - Vsc);
    // updating the history terms
    Ha = rl_zi * Ha + rl_yi * (Vta - Vsa);
    Hb = rl_zi * Hb + rl_yi * (Vtb - Vsb);
    Hc = rl_zi * Hc + rl_yi * (Vtc - Vsc);
    // inverter output power
    P = Ia*Vta + Ib*Vtb + Ic*Vtc;

    fprintf (fp, "%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g\n", t, Vsa, Vsb, Vsc, Vta, Vtb, Vtc, Ia, Ib, Ic, P);
    t += dt;
  }

  fclose (fp);
  return 0;
}
