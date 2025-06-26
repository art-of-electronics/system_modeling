clc; clear; close all;

%% ===== Graph parameters =====
global in;

%% ===== Graph parameters =====
graph.lt = 2; graph.fntsz = 15; graph.fnt = 'Arial Bold';

%% ===== Model parameters =====
in.m(1) = 5;
in.B(1) = 2;
in.k(1) = 2;
in.m(2) = 25;
in.B(2) = 8.4;
in.k(2) = 8.4;
in.F = 20;

%% ===== Simulation parameters =====
param.tmax = [0 35];
param.ic = [0 0 0 0];
param.options = odeset('RelTol', 1e-6, 'AbsTol', 1e-6);

%% ===== Simulation =====
[T, Y] = ode45(@DualDoF_m1_Script, param.tmax, param.ic, param.options);

%% ===== Calculations =====
out.time = T;
out.y(:, 1) = Y(:, 1);
out.y(:, 2) = Y(:, 3);
out.v(:, 1) = Y(:, 2);
out.v(:, 2) = Y(:, 4);
out.a(:, 1) = [diff(Y(:, 2)); 0];
out.a(:, 2) = [diff(Y(:, 4)); 0];
clearvars T Y;

out.Z0 = zeros(size(out.time, 1), 1);

graph.legend{1}=sprintf('m_{1}=%.1f, B_{1}=%.1f, k_{1}=%.1f', in.m(1), in.B(1), in.k(1));
graph.legend{2}=sprintf('m_{2}=%.1f, B_{2}=%.1f, k_{2}=%.1f', in.m(2), in.B(2), in.k(2));

%% ===== Plot =====
figure(1)
subplot(2, 1, 1);
plot(out.time, out.y, out.time, out.Z0, 'k', 'LineWidth', graph.lt);
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('Simulation time [s]');
ylabel('Mass displacement [m]');
title('Plot y=f(t)');
legend(graph.legend);
subplot(2, 1, 2);
plot(out.time, out.a, out.time, out.Z0, 'k', 'LineWidth', graph.lt);
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('Simulation time [s]');
ylabel('Mass acceleration [m/s^{2}]');
title('Plot a=f(t)');
legend(graph.legend);

figure(2) 
subplot(2, 2, 1);
plot(out.v(:, 1), out.a(:, 1), 'LineWidth', graph.lt);
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('$$\frac{dy}{dt}$$', 'Interpreter', 'latex');
ylabel('$$\frac{d^{2}y}{dt^{2}}$$', 'Interpreter', 'latex');
title('Phase portrait a=f(v) of subsystem 1');
subplot(2, 2, 2);
plot(out.y(:, 1), out.v(:, 1), 'LineWidth', graph.lt);
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('$$y$$', 'Interpreter', 'latex');
ylabel('$$\frac{dy}{dt}$$', 'Interpreter', 'latex');
title('Phase portrait v=f(y) of sub system 1');
subplot(2, 2, 3);
plot(out.v(:, 2), out.a(:, 2), 'LineWidth', graph.lt); 
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('$$\frac{dy}{dt}$$','Interpreter','latex');
ylabel('$$\frac{d^{2}y}{dt^{2}}$$', 'Interpreter', 'latex');
title('Phase portrait a=f(v) of subsystem 2');
subplot(2, 2, 4);
plot(out.y(:, 2), out.v(:, 2), 'LineWidth', graph.lt);
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('$$y$$', 'Interpreter', 'latex');
ylabel('$$\frac{dy}{dt}$$', 'Interpreter', 'latex');
title('Phase portrait v=f(y) of subsystem 2');

%% ===== End =====
