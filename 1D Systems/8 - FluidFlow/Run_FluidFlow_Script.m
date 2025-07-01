clc; clear; close all;

%% ===== Global parameters =====
global in;

%% ===== Graph parameters =====
graph.lt = 3; graph.fntsz = 15; graph.fnt = 'Consolas';

%% ===== Model parameters =====
in.g = 9.81;
% Tank diameters [m]
in.d = 0.03;
in.D = 1;
in.h0 = 5;
% Valve losses
in.ksi = [0.01 0.5];

%% ===== Simulation parameters =====
param.tmax = [0 2000];
param.ic = in.h0;
param.options = odeset('RelTol', 1e-4, 'AbsTol', 1e-4, 'Events', @StopingEvent);

%% ===== Simulation =====
for n = 1 : numel(in.ksi)
    in.ksiVal = in.ksi(n);
    [out.time{n}, out.H{n}] = ode45(@FluidFlow_Script, param.tmax, param.ic, param.options);
    graph.legend{n} = sprintf('loss=%.2f', in.ksi(n));
end;

%% ===== Plot =====
figure(1)
hold on;
for n = 1 : numel(graph.legend)
    plot(out.time{n}, real(out.H{n}), 'LineWidth', graph.lt);
end;
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
hold off;
grid on;
clearvars n;
title(sprintf('h=f(t), for h_{0}=%dm', in.h0));
xlabel('Time [s]');
ylabel('Water level [m]');
ylim([0, in.h0]);
legend(graph.legend, 'location', 'best');

%% ===== End =====