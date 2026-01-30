function mpc = XFMRSAT
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
     1     2  0.014659  0.148275  2.575146  600.000 0.0 0.0 0.0 0.0 1 0.0 0.0;
     2     3 0.0 1.0e-6 0.0  600.000 0.0 0.0 0.0 0.0 1 0.0 0.0;
     4     5 0.0 1.0e-6 0.0  600.000 0.0 0.0 0.0 0.0 1 0.0 0.0;
     3     4  0.002000  0.016000 0.0  500.000  666.667  833.333 1.000000 0.0 1 0.0 0.0;
];

%%-----  OPF Data  -----%%
%% generator cost data
%	1 startup shutdown n x1 y1 ... xn yn
%	2 startup shutdown n c(n-1) ... c0
mpc.gencost = [
  2 0 0 3 0.0060000 45.000 2230.000;
];

%% generator unit type (see GENTYPES)
% use WT, PV, HY, ST, CT, ST for corresponding GENFUELS
% WT and PV will use WECC dynamics; the others will use Gov/Exc/PSS dynamics
mpc.gentype = {
  'ST';
};

%% generator fuel type (see GENFUELS); use wind, solar, hydro, nuclear, ng, coal
mpc.genfuel = {
  'ng';
};

%% bus names
mpc.bus_name = {
  '1';
  '2';
  '3';
  '4';
  '5';
};

%% bus ids
mpc.bus_id = {
  'D3C50564-2BA5-4B81-AFF0-BB99CE54E804';
  '5A74B6F3-2B95-47DE-88FC-902A6643D37A';
  'FA16A3CC-2849-410E-91E7-88674CCA513D';
  '212BCE15-7CAE-4469-B001-5040D60466C6';
  '1FB3938E-D0BE-4AF9-8A2A-1EA4EA9C7B4E';
};

%% gen ids
mpc.gen_id = {
  '81D2A6A9-1FBB-440E-A92D-D71E703D650A';
};

%% branch ids
mpc.branch_id = {
  '68B79170-F5A8-481F-9792-6838B2D02849';
  '8952618F-8852-4420-9850-514793565B23';
  'AD792DFF-2C58-4BBF-8D75-2F72CFAB796B';
  '7507DEC9-7F4B-4C0C-ABC1-477372339EBF';
};

%% xfsec ids
mpc.xfsec_id = {
  '';
  '';
  '';
  'B4ED2857-F5D2-471F-9764-FC6799526E55';
};
