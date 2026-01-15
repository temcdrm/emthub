function mva = matpower_default_line_rating (kv)
    if (kv <= 121.0)
        mva = 131.0;
    elseif (kv <= 145.0)
        mva = 157.0;
    elseif (kv <= 242.0)
        mva = 600.0;
    elseif (kv <= 362.0)
        mva = 1084.0;
    else
        mva = 1800.0;
    endif
endfunction

