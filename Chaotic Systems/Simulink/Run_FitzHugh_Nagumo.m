clc; clear; close all;

a = 0.7;
b = 0.8;
e = 0.1;

A = 0.8;
omega = 0.7;

param.tmax = 300;
param.step = 0.001;
param.ic = [1 0];

param.options = simset('MaxStep', param.step);
load_system('FitzHugh_Nagumo');
open_system('FitzHugh_Nagumo');
sim('FitzHugh_Nagumo', param.tmax, param.options);

plot(simout.data(:,1), simout.data(:,2));
grid on;