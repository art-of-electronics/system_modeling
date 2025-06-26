function [Du] = RLC_Script(t, u)

global in;
global freq;

% Delta f step
k = (freq.fmax - freq.fmin) / freq.tmax;                  
% Chirp signal
Uw = cos((2 * pi() * (k / 2) .* t .* t) + (2 * pi() * freq.fmin .* t));
% RLC model
Du = [u(2); (in.ku * Uw - in.R * in.C * u(2) - u(1)) / (in.L * in.C)];
end
