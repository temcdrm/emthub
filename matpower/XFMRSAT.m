function mpc = XfmrSat
mpc.version = "2";
mpc.baseMVA = 100.0;

%% bus data
%	bus_i type Pd Qd Gs Bs area Vm Va baseKV zone Vmax Vmin
mpc.bus = [
     1  3     0.000     0.000     0.000     0.000   1  1.0000  0.0000 345.000   1  1.100  0.900;
     2  1     0.000     0.000     0.000     0.000   1  1.0000  0.0000 345.000   1  1.100  0.900;
     3  1     0.000     0.000     0.000     0.000   1  1.0000  0.0000 345.000   1  1.100  0.900;
     4  1     0.000     0.000     0.000     0.000   1  1.0000  0.0000 138.000   1  1.100  0.900;
     5  1     0.000     0.000   400.000     0.000   1  1.0000  0.0000 138.000   1  1.100  0.900;
];

%% generator data - SyncMachine+Solar+Wind
%	bus Pg Qg Qmax Qmin Vg mBase status Pmax Pmin Pc1 Pc2 Qc1min Qc1max Qc2min Qc2max ramp_agc ramp_10 ramp_30 ramp_q apf
mpc.gen = [
     1  400.000    0.000  400.000 -400.000 1.0000  800.000 1  800.000    0.000 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0;
];

%% branch data - BESLine+BESCompSeries+collected transformers
%	fbus tbus r x b rateA rateB rateC ratio angle status angmin angmax
mpc.branch = [
     1     2  0.016803  0.158370  2.490000  600.000 0.0 0.0 0.0 0.0 1 0.0 0.0;
     2     3 0.0 1.0e-6 0.0  600.000 0.0 0.0 0.0 0.0 1 0.0 0.0;
     4     5 0.0 1.0e-6 0.0  600.000 0.0 0.0 0.0 0.0 1 0.0 0.0;
     3     4  0.002000  0.016000 0.0  500.000  666.667  833.333 1.000000 0.0 1 0.0 0.0;
];

%%-----  OPF Data  -----%%
%% generator cost data
%	1 startup shutdown n x1 y1 ... xn yn
%	2 startup shutdown n c(n-1) ... c0
mpc.gencost = [
];

%% generator unit type (see GENTYPES)
% use WT, PV, HY, ST, CT, ST for corresponding GENFUELS
% WT and PV will use WECC dynamics; the others will use Gov/Exc/PSS dynamics
mpc.gentype = {
};

%% generator fuel type (see GENFUELS); use wind, solar, hydro, nuclear, ng, coal
mpc.genfuel = {
};

%% bus names
mpc.bus_name = {
  '1';
  '2';
  '3';
  '4';
  '5';
};
