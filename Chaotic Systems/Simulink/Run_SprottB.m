clc; clear; close all;

a = 0.4;
b = 1.2;
c = 1.0;

param.tmax = 300;
param.step = 0.01;
param.ic = [0.1 0.0 0.0];

param.options = simset('MaxStep', param.step);
load_system('SprottB');
open_system('SprottB');
sim('SprottB', param.tmax, param.options);

plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
