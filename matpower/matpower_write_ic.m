function write_ic = matpower_write_ic (mpc, fbus, fgen, fbranch)
% mpc should be loaded
    define_constants;

    fid=fopen(fbus, "w");
    fprintf (fid, "Bus, Vpu, Vdeg, CN id\n");
    n=size(mpc.bus)(1);
    for i=1:n
        fprintf (fid, "%d,%10.6f,%10.6f,%s\n", i, mpc.bus(i,VM), mpc.bus(i,VA), mpc.bus_id{i});
    endfor
    fclose(fid);

    fid=fopen(fgen, "w");
    fprintf (fid, "Bus, Pg, Qg, Type, CEQ id\n");
    n=size(mpc.gen)(1);
    for i=1:n
        fprintf (fid, "%d,%12.6f,%12.6f,%s,%s\n", mpc.gen(i,GEN_BUS), mpc.gen(i,PG), mpc.gen(i,QG), mpc.gentype{i}, mpc.gen_id{i});
    endfor
    fclose(fid);

    fid=fopen(fbranch, "w");
    fprintf (fid, "From, To, Ratio, Pfrom, Qfrom, Pto, Qto, CEQ/XfEnd id\n");
    n=size(mpc.branch)(1);
    for i=1:n
        fprintf (fid, "%d,%d,%6.4f,%12.6f,%12.6f,%12.6f,%12.6f,%s\n", mpc.branch(i,F_BUS), mpc.branch(i,T_BUS), mpc.branch(i,TAP), mpc.branch(i,PF), mpc.branch(i,QF), mpc.branch(i,PT), mpc.branch(i,QT), mpc.branch_id{i});
    endfor
    fclose(fid);
endfunction

