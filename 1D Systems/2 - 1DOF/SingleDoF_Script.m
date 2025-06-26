function [Dx] = SingleDoF_Script(t, x)

global in
g = 9.81;

if (t > 1)
    step = in.F;
else
    step = 0;
end

friction = in.mi * in.m * g * sign(x(2)) + in.c * x(2);

Dx  = [x(2); (step - in.B * x(2) - in.k * x(1) - friction) / in.m];
end
