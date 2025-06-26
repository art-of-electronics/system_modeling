function [Dphi] = Pendulum_Script(~, phi)

global in

Dphi  = [phi(2); -in.B * phi(2) - in.g / in.l * sin(phi(1))];
end
