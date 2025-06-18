clc; clear; close all;

a = -5.5;
b = 3.5;
c = -1;

param.tmax = 100;
param.step = 0.001;
param.ic = [1.0 1.0 0.0];

param.options = simset('MaxStep', param.step);
load_system('Arneodo');
open_system('Arneodo');
sim('Arneodo', param.tmax, param.options);

plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
