clc; clear; close all;

a = 36;
b = 3;
c = 20;

param.tmax = 10;
param.step = 0.001;
param.ic = [1 1 1];

param.options = simset('MaxStep', param.step);
load_system('Lu');
open_system('Lu');
sim('Lu', param.tmax, param.options);

plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
