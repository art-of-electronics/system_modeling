clc; clear; close all;

a = 1;
b = 2.6;
c = 1;
d = 5;
r = 0.01;
s = 4;
xR = -8/5;
I = 3;

param.tmax = 350;
param.step = 0.001;
param.ic = [0 0 0];

param.options = simset('MaxStep', param.step);
load_system('HindmarshRose');
open_system('HindmarshRose');
sim('HindmarshRose', param.tmax, param.options);

plot3(simout.data(:, 1), simout.data(:, 2), simout.data(:, 3));
grid on;
