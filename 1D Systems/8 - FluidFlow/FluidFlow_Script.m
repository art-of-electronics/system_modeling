function [Dh] = FluidFlow_Script(~, h)

global in;

Dh = -(in.d / in.D)^2 * sqrt((2 * in.g * h) / (1 + in.ksiVal));
end