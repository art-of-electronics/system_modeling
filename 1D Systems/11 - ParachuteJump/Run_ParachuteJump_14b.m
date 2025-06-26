clc; clear; close all;
%% ===== Graph parameters =====
graph.lt = 3; graph.fntsz = 15; graph.fnt = 'Times New Roman';

%% ===== Model parameters =====
in.m = 110;         % Mass of skydiver
in.c = [0.5 1.42];  % Reynolds excellence factor
in.A = [1.5 28];    % Area of skydiver without and with parachhute 
in.H = 5000;        % Initial jumo-out altitude
in.h0 = 2000;       % Parachute opening altitude

in.g = 9.81;        % Gravitational force
in.rho = 1.2;       % Air density
in.p = 1.01 * 1e5;  % Air pressure
in.h0 = in.H - in.h0;
in.k = in.c .* in.A;

%% ===== Simulation parameters =====
param.tmax = 1000;  % Time
param.step = 0.01;  % Simulation step
param.ic = [0 0];   % Initial conditions
param.options = simset('MaxStep', param.step);

%% ===== Simulation =====
load_system('Model_ParachuteJump_14b');
open_system('Model_ParachuteJump_14b');
sim('Model_ParachuteJump_14b', param.tmax, param.options);

%% ===== Calculations =====
out.time = simout.Time;
out.y = simout.Data(:, 3);
out.v = simout.Data(:, 2);
out.a = simout.Data(:, 1);
clearvars simout tout;

out.a2 = (9.81 - [diff(out.v)', 0]) / 9.81;
graph.title = sprintf('Parachute jump, skydiver m=%dkg', in.m);

%% ===== Plot =====
figure(1)
subplot(3, 1, 1)
plot(out.time, out.y, 'LineWidth', graph.lt);
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('Time [s]');
ylabel('Altitude [m]');
title(graph.title);
subplot(3, 1, 2)
plot(out.time, out.v, 'LineWidth', graph.lt);
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('Time [s]');
ylabel('Speed [km/h]');
subplot(3, 1, 3)
plot(out.time, out.a2, 'LineWidth', graph.lt);
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('Time [s]');
ylabel('Acceleration [G]');

%% ===== End =====
