clc; clear; close all;

y = 1;
b = 2;
tau = 5;
n = 10;

param.tmax = 200;
param.step = 0.001;
param.ic = 0.2;

param.options = simset('MaxStep', param.step);
load_system('MackeyGlass');
open_system('MackeyGlass');
sim('MackeyGlass', param.tmax, param.options);

figure(1)
plot(simout.data(:, 1), simout.data(:, 2));
figure(2)
plot(simout.Time, simout.data(:, 1), simout.Time, simout.data(:, 2));
grid on;
