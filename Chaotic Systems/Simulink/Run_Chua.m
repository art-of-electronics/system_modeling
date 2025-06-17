clc; clear; close all;

a = 15.6;
b = 28;
m0 = -1.143;
m1 = -0.714;

param.tmax = 100;
param.step = 0.0001;
param.ic = [-0.5 -0.2 0];

param.options = simset('MaxStep', param.step);
load_system('Chua');
open_system('Chua');
sim('Chua', param.tmax, param.options);

plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
