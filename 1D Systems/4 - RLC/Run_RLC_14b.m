clc; clear; close all;
%% ===== Graph parameters =====
graph.lt = 2; graph.fntsz = 15; graph.fnt = 'Hellvetica';

%% ===== Model parameters =====
in.R = [1 2.2 3.3 4.7 6.8 8.2 10 48]; % Resistance 
in.L = floor(10 * rand() + 1) * 1e-3; % Inductance in mH
in.C = floor(10 * rand() + 1) * 1e-6; % Capacitance in uF
in.U = 10;                            % Input voltage in V

RLC.f0 = 1 / (2 * pi() * sqrt(in.L * in.C));
freq.fmin = 0.6 * RLC.f0;
freq.fmax = 1.4 * RLC.f0;

in.RC = in.R * in.C;
in.LC = in.L * in.C;

%% ===== Simulation parameters =====
param.tmax = 10;
param.step = 0.0001;
param.ic = [0 0];

%% ===== Simulation =====
param.options = simset('MaxStep', param.step);
load_system('Model_RLC_14b');
open_system('Model_RLC_14b');
tic;
sim('Model_RLC_14b', param.tmax, param.options);
param.simtime = toc;

%% ===== Calculations =====
F = (((freq.fmax - freq.fmin) / param.tmax) * simout.Time) + freq.fmin;

for i = 1 : size(in.R, 2)
    RLC.Q(i) = (1 / in.R(i)) * sqrt(in.L / in.C);
    RLC.band_dB(i) = RLC.f0 / RLC.Q(i);
    RLC.zeta(i) = in.R(i) / 2 * sqrt(in.C / in.L);
    U.U(:, i) = simout.Data(:, i);
    U.I(:, i) = abs(hilbert(in.C * simout.Data(:, i + size(in.R, 2))));
    U.Env(:, i) = mag2db(abs(hilbert(U.U(:, i))) / RLC.Q(i) / in.U);
    graph.legend{1}{i} = sprintf('U=%.2fU_{in} @ R=%.1f\\Omega', max(U.U(:, i)) / in.U, in.R(i));
    graph.legend{2}{i} = sprintf('\\Deltaf=%.1fHz @ R=%.1f\\Omega', RLC.band_dB(i), in.R(i));
    graph.legend{3}{i} = sprintf('i_{max}=%.2fA @ R=%.1f\\Omega; \\zeta=%.2f', max(U.I(:, i)), in.R(i), RLC.zeta(i));
end;
U.point3dB = ones(size(F, 1), 1) .* (-3);
graph.legend{2}{size(in.R, 2) + 1} = '-3dB';
clearvars i tout simout;

%% ===== Plot =====
figure(1)
hold on
for i = 1 : size(in.R, 2)
    plot(F, U.U(:, i), 'LineWidth', graph.lt);
end;
clearvars i;
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
title(sprintf('Plot U(f_{0})=f(f) for f_{0}=%.1fHz', RLC.f0));
xlabel('Frequency [Hz]');
xlim([freq.fmin freq.fmax]);
ylabel('Resonant Voltage Amplitude [V]');
legend(graph.legend{1}, 'location', 'best');
hold off

figure(2)
hold on
for i = 1 : size(in.R, 2)
    plot(F, U.Env(:, i), 'LineWidth', graph.lt);
end;
clearvars i;
plot(F, U.point3dB, 'k', 'LineWidth', graph.lt);
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
title(sprintf('Plot Q=f(f) for f_{0}=%.1fHz', RLC.f0));
legend(graph.legend{2}, 'location', 'best');
xlabel('Frequency [Hz]');
xlim([freq.fmin freq.fmax]);
ylabel('Resonant Voltage Magnitude [dB]');
hold off

figure(3)
hold on
for i = 1 : size(in.R, 2)
    plot(F, U.I(:, i), 'LineWidth', graph.lt);
end;
clearvars i;
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
title(sprintf('Plot i=f(f) for f_{0}=%.1fHz', RLC.f0));
legend(graph.legend{3}, 'location', 'best');
xlabel('Frequency [Hz]');
xlim([freq.fmin freq.fmax]);
ylabel('Instantaneous Circuit Current [A]');
hold off

%% ===== End =====
fprintf(2, 'Total time of performing calculations: %.3fs\n', param.simtime);
