clc; clear; close all;

a = 33;
b = 3;
c = 25;

param.tmax = 20;
param.step = 0.001;
param.ic = [1.0 0.5 0.5];

param.options = simset('MaxStep', param.step);
load_system('Chen');
open_system('Chen');
sim('Chen', param.tmax, param.options);

plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
