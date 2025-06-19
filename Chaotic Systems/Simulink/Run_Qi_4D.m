clc; clear; close all;

a = 35;
b = 80;
c = 3;
d = 0.6;

param.tmax = 10;
param.step = 0.0001;
param.ic = [1, 1, 1, 1];

param.options = simset('MaxStep', param.step);
load_system('Qi_4D');
open_system('Qi_4D');
sim('Qi_4D', param.tmax, param.options);

figure(1)
plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
figure(2)
plot(simout.Time, simout.data(:, 1), simout.Time, simout.data(:, 2), ...
    simout.Time, simout.data(:, 3), simout.Time, simout.data(:, 4));
grid on;
