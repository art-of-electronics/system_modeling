clc; clear; close all;

l = 1; % lambda

param.tmax = 150;
param.step = 0.001;
param.ic = [-0.0824, 0.245, 0.508, -0.0408];

param.options = simset('MaxStep', param.step);
load_system('HenonHeiles');
open_system('HenonHeiles');
sim('HenonHeiles', param.tmax, param.options);

figure(1)
plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
figure(2)
plot3(simout.data(:, 4), simout.data(:, 5), simout.data(:, 6));
grid on;
