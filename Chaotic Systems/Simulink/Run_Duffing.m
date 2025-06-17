clc; clear; close all;

s = 0.2;
b = 100;
w = 1;
y = 1;
fi = 1.57;

param.tmax = 100;
param.step = 0.001;
param.ic = [1 0];

param.options = simset('MaxStep', param.step);
load_system('Duffing');
open_system('Duffing');
sim('Duffing', param.tmax, param.options);

plot(simout.data(:,2), simout.data(:,1));
grid on;