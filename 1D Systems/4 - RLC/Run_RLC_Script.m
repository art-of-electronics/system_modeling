clc; clear; close all;
%% ===== Global parameters =====
global in;
global freq;

%% ===== Graph parameters =====
graph.lt = 2; graph.fntsz = 15; graph.fnt = 'Consolas';

%% ===== Model parameters =====
RLC.R = [2.2 4.7 8.2];                % Resistance in ?
in.L = floor(10 * rand() + 1) * 1e-3; % Inductance in mH
in.C = floor(10 * rand() + 1) * 1e-6; % Capacitance in uF
in.ku = 3.3;                          % Input voltage in V

RLC.f0 = 1 / (2 * pi() * sqrt(in.L * in.C));
freq.fmin = 0.6 * RLC.f0; 
freq.fmax = 1.4 * RLC.f0; 
freq.tmax = 10;

%% ===== Simulation parameters =====
param.tmax = [0 freq.tmax];
param.ic = [0 0];
param.options = odeset('RelTol', 1e-2, 'AbsTol', 1e-2);

%% ===== Simulation =====
param.simtime = zeros(size(RLC.R, 2), 1);
for i = 1 : size(RLC.R, 2)
    in.R = RLC.R(i);
    tic;
    [F{i}, U.U{i}] = ode45(@RLC_Script, param.tmax, param.ic, param.options);
    param.simtime(i) = toc;
    fprintf('Loop %d time of performing calculations: %.3fs\n', i, param.simtime(i));
end;
clearvars i;

%% ===== Calculations =====
for i = 1 : size(RLC.R, 2)
    RLC.Q(i) = 1 / RLC.R(i) * sqrt(in.L / in.C);
    RLC.band_dB(i) = RLC.f0 / RLC.Q(i);
    RLC.zeta(i) = RLC.R(i) / 2 * sqrt(in.C / in.L);

    F{i}=(((freq.fmax - freq.fmin) / freq.tmax) * F{i}) + freq.fmin;
    U.Env{i} = mag2db(abs(hilbert(U.U{i}(:, 1))) / in.ku / RLC.Q(i));
    U.I{i} = abs(hilbert(in.C * (U.U{i}(:, 2))));

    graph.legend{1}{i} = sprintf('U=%.1fU_{in} @ R=%.1f\\Omega', RLC.Q(i), RLC.R(i));
    graph.legend{2}{i} = sprintf('\\Deltaf=%.1fHz @ R=%.1f\\Omega', RLC.band_dB(i), RLC.R(i));
    graph.legend{3}{i} = sprintf('i_{max}=%.2fA @ R=%.1f\\Omega; \\zeta=%.2f', max(U.I{i}(:,1)), RLC.R(i), RLC.zeta(i));
end;
clearvars i;
graph.legend{2}{size(RLC.R, 2) + 1} = '-3dB';
U.point3dB{1} = ones(size(F{1}, 1) ,1) .* (-3);

%% ===== Plot =====
figure(1)
hold on
for i = 1 : size(RLC.R, 2)
    plot(F{i} ,U.U{i}(:, 1), 'LineWidth', graph.lt);
end;
clearvars i;
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlim([freq.fmin freq.fmax]);
title(sprintf('Plot U(f_{0})=f(f) for f_{0}=%.1fHz', RLC.f0));
xlabel('Frequency [Hz]');
ylabel('Resonant Voltage Amplitude [V]');
legend(graph.legend{1}, 'location', 'best');
hold off

figure(2)
hold on
for i = 1 : size(RLC.R, 2)
    plot(F{i}, U.Env{i}(:, 1), 'LineWidth', graph.lt);
end;
clearvars i;
plot(F{1}, U.point3dB{1}, 'k', 'LineWidth', graph.lt);
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlim([freq.fmin freq.fmax]);
ylim([-40 10]);
title(sprintf('Plot Q=f(f) for f_{0}=%.1fHz', RLC.f0));
xlabel('Frequency [Hz]');
ylabel('Resonant Voltage Magnitude [dB]');
legend(graph.legend{2}, 'location', 'best');
hold off

figure(3)
hold on
for i = 1 : size(RLC.R, 2)
    plot(F{i}, U.I{i}(:, 1), 'LineWidth', graph.lt);
end;
clearvars i;
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
title(sprintf('Plot i=f(f) for f_{0}=%.1fHz', RLC.f0));
legend(graph.legend{3}, 'location','best');
xlabel('Frequency [Hz]');
xlim([freq.fmin freq.fmax]);
ylabel('Instantaneous Circuit Current [A]');
hold off

%% ===== End =====
% load handel;
% sound(y,Fs);
% clearvars Fs y;
fprintf(2, 'Total time of performing calculations: %.3fs\r\n', sum(param.simtime));
