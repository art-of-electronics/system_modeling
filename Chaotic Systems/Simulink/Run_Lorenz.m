clc; clear; close all;

s = 10;
b = 8/3;
r = 100;

param.tmax = 200;
param.step = 0.001;
param.ic = [0 0.5 0.8];

param.options = simset('MaxStep', param.step);
load_system('Lorenz');
open_system('Lorenz');
sim('Lorenz', param.tmax, param.options);

plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
