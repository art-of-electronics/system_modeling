clc; clear; close all;

a = 0.05;   % aplha
g = 0.09;   % gamma

param.tmax = 70;
param.step = 0.01;
param.ic = [0.1 -0.1 0.1];

param.options = simset('MaxStep', param.step);
load_system('RabinovichFabrikant');
open_system('RabinovichFabrikant');
sim('RabinovichFabrikant', param.tmax, param.options);

plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
