clc; clear; close all;
%% ===== Graph parameters =====
graph.lt = 3; graph.fntsz = 15; graph.fnt = 'Times New Roman';

%% ===== Model parameters =====
in.m = 25;  % Mass
in.B = 5;   % Damping
in.k = 5;   % Spring stiffness
in.F = 20;  % Force

in.Mu = 0.004;  % Dry friction
in.c = 0.2;     % Viscous friction
in.g = 9.81;    % Gravitational force

%% ===== Simulation parameters =====
param.tmax = 70;    % Time
param.step = 0.01;  % Simulation step
param.ic = [0 0];   % Initial conditions
param.options = simset('MaxStep', param.step);

%% ===== Simulation =====
load_system('Model_1DoF_14b');
open_system('Model_1DoF_14b');
sim('Model_1DoF_14b', param.tmax, param.options);

%% ===== Calculations =====
out.time = simout.Time;
out.x = simout.Data(:, 3);
out.v = simout.Data(:, 2);
out.a = simout.Data(:, 1);
clearvars simout tout;

graph.title{1} = sprintf('Plot a,\\vartheta,x=f(t) for  m=%.1f, B=%.1f, k=%.1f', in.m, in.B, in.k);
graph.legend{1} = 'x=f(t)';
graph.legend{2} = '\vartheta=f(t)';
graph.legend{3} = 'a=f(t)';

%% ===== Plot =====
figure(1)
plot(out.time, out.x, out.time, out.v, out.time, out.a, 'LineWidth', graph.lt);
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('Time [s]');
ylabel('$$\frac{d^{2}x}{dt^{2}}[\frac{m}{s^{2}}], \frac{dx}{dt}[\frac{m}{s}], x[m]$$', 'Interpreter', 'latex');
title(graph.title);
legend(graph.legend, 'location', 'best');

figure(2)
subplot(1, 2, 1);
plot(out.v, out.a, 'LineWidth', graph.lt);
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('$$\frac{dx}{dt}$$', 'Interpreter', 'latex');
ylabel('$$\frac{d^{2}x}{dt^{2}}$$', 'Interpreter', 'latex');
title('Phase portrait a=f(\vartheta)')
subplot(1, 2, 2);
plot(out.x, out.v, 'LineWidth', graph.lt);
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('$$x$$', 'Interpreter', 'latex');
ylabel('$$\frac{dx}{dt}$$', 'Interpreter', 'latex');
title('Phase portrait \vartheta=f(x)');

%% ===== End =====
