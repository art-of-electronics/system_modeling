clc; clear; close all;

%% ===== Global parameters =====
global in

%% ===== Graph parameters =====
graph.lt = 2; graph.fntsz = 12; graph.fnt = 'Consolas';

%% ===== Model parameters =====
in.m = 25;
in.B = 5;
in.k = 5;
in.F = 20;

% Friction
in.mi = 0.004;
in.c = 0.2;

%% ===== Simulation parameters =====
param.tmax = [0 70];
param.ic = [0 0];
param.options = odeset('RelTol', 1e-4, 'AbsTol', 1e-4);

%% ===== Simulation =====
[T, X] = ode45(@SingleDoF_Script, param.tmax, param.ic, param.options);

%% ===== Calculations =====
out.time = T(:, 1);
out.x = X(:, 1);
out.v = X(:, 2);
out.a = diff(X(:, 2));
clearvars T X;

graph.title{1} = sprintf('Plot a, \\vartheta, x=f(t)  for  m=%.1f, k=%.1f', in.m, in.k);
graph.legend{1} = 'x=f(t)';
graph.legend{2} = '\vartheta=f(t)';
graph.legend{3} = 'a=f(t)';

%% ===== Plot =====
figure(1)
plot(out.time, out.x, out.time, out.v, out.time(1:end-1), out.a, 'LineWidth', graph.lt);
set(gca, 'FontSize',graph.fntsz, 'FontName',graph.fnt);
xlabel('Time [s]');
ylabel('$$\frac{d^{2}x}{dt^{2}}[\frac{m}{s^{2}}], \frac{dx}{dt}[\frac{m}{s}], x[m]$$', 'Interpreter', 'latex');
title(graph.title);
legend(graph.legend, 'location', 'best');

figure(2)
subplot(1, 2, 1);
plot(out.v(1:end-1), out.a, 'LineWidth', graph.lt);
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
fprintf(2, 'End! \n');
