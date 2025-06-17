clc; clear; close all;

b = 0.19;

param.tmax = 500;
param.step = 0.01;
param.ic = [1.0, 0.8, 0.8];

param.options = simset('MaxStep', param.step);
load_system('Thomas');
open_system('Thomas');
sim('Thomas', param.tmax, param.options);

plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
