function [Dy] = DualDoF_m2_Script(t, y)

global in

w = 10;
F = in.F * sin(w .* t);

subsystem(1) = (-in.B(1) * y(2) - in.k(1) * y(1) + in.B (1) * y(4) + in.k(1) * y(3)) / in.m(1);
subsystem(2) = (F -(sum(in.B)) * y(4) - (sum(in.k)) * y(3) + in.B(1) * y(2) + in.k(1) * y(1)) / in.m(2);

Dy = [y(2); subsystem(1); y(4); subsystem(2)];
end