function [DT] = SimpleThermal_Script(t, T)

global in;

if (t > in.t_start)
    Q = in.Qin;
else
    Q = 0;
end
 
DT = (Q - (T - in.Tw) * in.Kc) / in.Cv;
DT = DT(:);
end