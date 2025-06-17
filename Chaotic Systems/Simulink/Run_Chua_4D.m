clc; clear; close all;

A = 30;     % alpha
B = 50;     % beta
G = 0.32;   % gamma
a = 0.03;
c = -1.2;
s = 0.75;

param.tmax = 100;
param.step = 0.0001;
param.ic = [-0.5 -0.2 0 0];

param.options = simset('MaxStep', param.step);
load_system('Chua_4D');
open_system('Chua_4D');
sim('Chua_4D', param.tmax, param.options);

figure(1)
plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
figure(2)
plot(simout.Time, simout.data(:, 1), simout.Time, simout.data(:, 2), ...
    simout.Time, simout.data(:, 3), simout.Time, simout.data(:, 4));
grid on;
