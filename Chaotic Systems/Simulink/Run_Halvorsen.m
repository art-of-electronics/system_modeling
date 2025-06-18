clc; clear; close all;

a = 1.4;

param.tmax = 50;
param.step = 0.001;
param.ic = [0.1 0.0 0.0];

param.options = simset('MaxStep', param.step);
load_system('Halvorsen');
open_system('Halvorsen');
sim('Halvorsen', param.tmax, param.options);

plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
