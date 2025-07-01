clc; clear; close all;

%% ===== Graph parameters =====
graph.lt = 3; graph.fntsz = 15; graph.fnt = 'Consolas';

%% ===== Model parameters =====
in.g = 9.81;
% Tank diameters [m]
in.d = 0.05;
in.D = 1;
in.h0 = 5;
% Valve losses
in.ksi = [0.01 0.5];

%% ===== Simulation parameters =====
param.tmax = 2000;  
param.step = 0.1;
param.ic = in.h0;   % Initial conditions
param.options = simset('MaxStep', param.step);

%% ===== Simulation =====

load_system('Model_FluidFlow_14b');
open_system('Model_FluidFlow_14b');

simout_sim = cell(1, numel(in.ksi));
for n = 1 : numel(in.ksi)
    in.ksiVal = in.ksi(n);
    sim('Model_FluidFlow_14b', param.tmax, param.options);
    simout_sim{n} = simout; 
end;

%% ===== Calculations =====
for n = 1 : numel(in.ksi)
    out.time{n} = simout_sim{n}.Time;
    out.h{n} = simout_sim{n}.Data;
    graph.legend{n} = sprintf('loss=%.2f', in.ksi(n));
end;
clearvars n tout simout simout_sim;

%% ===== Plot =====
figure(1)
hold on;
for n = 1 : numel(graph.legend)
    plot(out.time{n}, out.h{n}, 'LineWidth', graph.lt);
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
