function [Du] = RLC_Script(t,u)

    global in;
    global freq;

    k = (freq.fmax - freq.fmin)/freq.tmax;                  % Delta f step
    Uw = cos((2*pi()*(k/2).*t.*t) + (2*pi()*freq.fmin.*t)); % Chirp signal
    Du = [u(2); (in.ku*Uw-in.R*in.C*u(2)-u(1))/(in.L*in.C)];% RLC model
end
