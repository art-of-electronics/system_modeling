clc; clear; close all;

q = 8 * 1e-4;
f = 1.05;
d = 4 * 1e-3;   % delta
e = 0.3;        % epsilon

param.tmax = 50;
param.step = 0.01;
param.ic = [0.05 0.05 0.05];

param.options = simset('MaxStep', param.step);
load_system('Belousov_Zhabotinsky');
open_system('Belousov_Zhabotinsky');
sim('Belousov_Zhabotinsky', param.tmax, param.options);

plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
