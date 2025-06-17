clc; clear; close all;

param.tmax = 100;
param.step = 0.01;
param.ic = [0.1 0.1 0.1];

param.options = simset('MaxStep', param.step);
load_system('Nose_Hoover');
open_system('Nose_Hoover');
sim('Nose_Hoover', param.tmax, param.options);

plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
