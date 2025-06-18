clc; clear; close all;

p = 3.0;
o = 2.7;
r = 1.7;
c = 2.0;
e = 9.0;

param.tmax = 100;
param.step = 0.001;
param.ic = [1.0 1.0 0.0];

param.options = simset('MaxStep', param.step);
load_system('Dadras');
open_system('Dadras');
sim('Dadras', param.tmax, param.options);

plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
