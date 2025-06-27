clc; clear; close all;

%% ===== Graph parameters =====
graph.lt = 2; graph.fntsz = 15; graph.fnt = 'Consolas';

%% ===== Model parameters =====
in.Q = 4000; % Heater power [W]
% Temperatures [deg C]
in.T0 = -10;
in.Tfinal = 20;
% Room dimensionsimensions [m]
in.x = 5; 
in.y = 5; 
in.z = 3;
% Air thermodynamic parameters
in.Cp = 1005; % Specific heat [J/kgK]
in.rho = 1.2; % Density [kg/m3]

in.V = prod([in.x in.y in.z]);
in.Cv = in.Cp * in.rho * in.V;

%% ===== Simulation parameters =====
param.tmax = 3600; 
param.tstart = 600; 
param.step = 1;

load_system('Model_SimpleThermal_14b');
open_system('Model_SimpleThermal_14b');

%% ===== Simulation =====
in.qN = [0.6 * in.Q in.Q 1.4 * in.Q 2 * in.Q]; % Different heater power [W]
in.Kc = in.qN / (in.Tfinal - in.T0);
in.Tw = in.T0;

param.options = simset('MaxStep', param.step);
sim('Model_SimpleThermal_14b', param.tmax, param.options);

%% ===== Calculations =====
out.time = simout.Time / 60;
for n = 1 : size(in.qN, 2)
    out.q(:, n) = simout.Data(:, n);
    graph.legend{n} = sprintf('q%d=%.1fkW', n, (in.qN(n) / 1000));
end;
clearvars n tout simout;

%% ===== Plot =====
figure(1)
hold on;
for n = 1 : size(graph.legend, 2)
    plot(out.time, out.q(:, n), 'LineWidth', graph.lt);
end;
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
hold off;
grid on;
clearvars n;
title(sprintf('T_{W}=f(q), for t_{0}=%1.f\\circC', in.T0));
xlabel('Time [min]');
ylabel('Temperature T_{w} [\circC]');
legend(graph.legend, 'location', 'best');

%% ===== End =====
