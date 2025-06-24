function [Dy] = ParachuteJump_Script(~,y)

global in;

g0 = 9.8;
rho0 = 1.2;
p0 = 1.01 * 1e5;

% Opening of parachute
if ((in.H - y(1)) > in.h0)
    c = in.c(1);
    A = in.A(1);
else
    c = in.c(2);
    A = in.A(2);
end

% Parachte jump model
g_y = g0 - 3.086 * (in.H - y(1)) * 1e-5;
rho_y = rho0 * ((p0 - 13 * (in.H - y(1))) / p0);

Dy = [y(2); g_y - c * A * (rho_y .* y(2) .* y(2) / (2 * in.m))];
end