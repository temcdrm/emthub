function opf_flows = matpower_opf_flows (mpc, scale, fname)
% mpc should be loaded
    define_constants;
    % scale load, run the opf
    mpc = scale_load (scale, mpc);
    mpc = toggle_softlims(mpc,'on');
    rate = mpc.branch(:, RATE_A);
    mpc.branch(:, RATE_A) = 0;
    res = runopf(mpc);

    % determine the original bus numbers
    fbus = res.branch(:,F_BUS);
    tbus = res.branch(:,T_BUS);
    fraw = mpc.bus_name(fbus);
    traw = mpc.bus_name(tbus);
    n = length(fbus);
    fout = zeros(n,1);
    tout = zeros(n,1);
    for i=1:n
        fout(i) = str2num (fraw{i});
        tout(i) = str2num (traw{i});
    endfor

    % output the line flows at both ends, with original bus numbers and ratings
    p = res.branch(:,PF);
    q = res.branch(:,QF);
    s = sqrt(p.*p+q.*q);
    mbr = [fout,tout,fbus,tbus,rate,s,p,q,res.branch(:,PT),res.branch(:,QT)];
    csvwrite(fname,mbr);
    opf_flows = mbr;
endfunction

