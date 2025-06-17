clc; clear; close all;

mu = 7;

param.tmax = 100;
param.step = 0.01;
param.ic = [0.0, 0.1];

param.options = simset('MaxStep', param.step);
load_system('VanDerPol');
open_system('VanDerPol');
sim('VanDerPol', param.tmax, param.options);

plot(simout.data(:,2), simout.data(:,1));
grid on;
