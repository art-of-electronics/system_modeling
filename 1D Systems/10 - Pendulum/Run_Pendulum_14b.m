clc; close all; clear;

%% ===== Graph parameters =====
graph.lt = 2; graph.fntsz = 15; graph.fnt = 'Hellvetica';

%% ===== Model parameters =====
in.l = 0.247;
in.deg = 10; % Pendulum swing initial angle
in.g = 9.81;
in.damping = [0.05 0.1 0.3];

in.rad = in.deg * pi() / 180;
in.w0 = sqrt(in.g / in.l);
in.B = [0, 2 * in.w0 * in.damping(1), 2 * in.w0 * in.damping(2), 2 * in.w0 * in.damping(3)];

%% ===== Simulation parameters =====
param.tmax = 10;    % Time
param.step = 0.01;  % Simulation step
param.options = simset('MaxStep', param.step);

%% ===== Simulation =====
load_system('Model_Pendulum_14b');
open_system('Model_Pendulum_14b');
sim('Model_Pendulum_14b', param.tmax, param.options);

%% ===== Calculations =====
out.time = simout.Time;

for n = 1 : size(in.B, 2)
    out.angle(:, n) = simout.Data(:, n);
    out.speed(:, n) = simout.Data(:, n + size(in.B, 2));
    out.accel(:, n) = simout.Data(:, n + 2 * size(in.B, 2));
end;

out.zero = zeros(1, size(out.time, 1));

clearvars simout tout;

% Phase portrait limits
graph.lim_x(1) = round(max(out.angle(:, 1)), 1);
graph.lim_x(2) = round(min(out.angle(:, 1)), 1);
graph.lim_y(1) = round(max(out.speed(:, 1)) * 10) / 10; 
graph.lim_y(2) = -graph.lim_y(1);

graph.legend{size(in.B, 2), 1} = '';
graph.legend{1} = 'No damping';
for n = 2 : size(in.B, 2)
    graph.legend{n} = sprintf('Damping B=%.2f', in.B(n));
end;

%% ===== Plot =====
figure(1)
hold on
for n = 1 : size(in.B, 2)
    plot(out.time, out.angle(:, n), 'LineWidth', graph.lt);
end;
clearvars n;
plot(out.time, out.zero, 'k');
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('Time [s]');
ylabel('Pendulum swing [\circ]');
title(sprintf('Motion of a pendulum of length l=%.3f[m]', in.l));
legend(graph.legend, 'location', 'best');
hold off

figure(2);
for n = 1 : size(in.B, 2)
    subplot(2, 2, n);
    plot(out.angle(:, n), out.speed(:, n), 'LineWidth', graph.lt);
    set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
    xlabel('$$\varphi$$', 'Interpreter', 'latex');
    xlim([graph.lim_x(2) graph.lim_x(1)]);
    ylabel('$$\frac{d\varphi}{dt}$$', 'Interpreter', 'latex');
    ylim([graph.lim_y(2) graph.lim_y(1)]);
    title(sprintf('Phase portrait - %s', graph.legend{n}));
end;
clearvars n;

%% ===== End =====
