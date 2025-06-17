clc; clear; close all;

a = 0.95;   % aplha
b = 0.7;    % beta
g = 0.65;   % gamma
s = 3.5;    % sigma
e = 0.15;   % epsilon

param.tmax = 200;
param.step = 0.001;
param.ic = [-1 -1 -1];

param.options = simset('MaxStep', param.step);
load_system('Aizawa');
open_system('Aizawa');
sim('Aizawa', param.tmax, param.options);

plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
