clc; clear; close all;

a = 0.25;
b = 2;
c = 0.5;
d = 0.05;

param.tmax = 100;
param.step = 0.0001;
param.ic = [-10, -6, 0, 10];

param.options = simset('MaxStep', param.step);
load_system('Roessler_4D');
open_system('Roessler_4D');
sim('Roessler_4D', param.tmax, param.options);

figure(1)
plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
figure(2)
plot(simout.Time, simout.data(:, 1), simout.Time, simout.data(:, 2), ...
    simout.Time, simout.data(:, 3), simout.Time, simout.data(:, 4));
grid on;
