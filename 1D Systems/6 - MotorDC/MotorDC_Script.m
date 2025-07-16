function [Du] = MotorDC_Script(t, u)

global in;

% Input voltage
if t > 1
    Uin = in.U;
else
    Uin = 0;
end;

% Load
if t > 2
    Mt = in.Mt_val;
else
    Mt = 0;
end;

% DC motor model
Du = [u(2); (-in.B * u(2) + in.km * u(4) - Mt) / in.J; 
    u(4); (Uin - in.R * u(4) - in.ke * u(2)) / in.L];
end
