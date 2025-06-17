clc; clear; close all;

a = 0.38;
b = 0.2;
c = 5.7;

param.tmax = 100;
param.step = 0.001;
param.ic = [-10 -6 0];

param.options = simset('MaxStep', param.step);
load_system('Roessler');
open_system('Roessler');
sim('Roessler', param.tmax, param.options);

plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
