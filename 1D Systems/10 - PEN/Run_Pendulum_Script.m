clc; close all; clear;

%% ===== Global parameters =====
global in

%% ===== Graph parameters =====
graph.lt = 2; graph.fntsz = 15; graph.fnt = 'Hellvetica';

%% ===== Model parameters =====
in.l = 0.247;
in.deg = 10; % Pendulum swing initial angle
in.g = 9.81;
in.damping = [0.05 0.1 0.3];

in.rad = in.deg * pi() / 180;
in.w0 = sqrt(in.g / in.l);
in.Bfactor = [0 2 * in.w0 * in.damping(1), 2 * in.w0 * in.damping(2), 2 * in.w0 * in.damping(3)];

%% ===== Simulation parameters =====
param.tmax = [0 10];
param.ic = [in.rad 0];

%% ===== Simulation =====
param.options = odeset('RelTol', 1e-6, 'AbsTol', 1e-6);

param.simtime = zeros(size(in.Bfactor, 2), 1);
for n = 1 : size(in.Bfactor, 2)
    in.B = in.Bfactor(n);
    tic;
    [T{n},PHI{n}] = ode45(@Pendulum_Script, param.tmax, param.ic, param.options);
    param.simtime(n) = toc;
    fprintf('Loop %d time of performing calculations: %.3fs\n', n, param.simtime(n));
end;
clearvars n;

%% ===== Calculations =====
for n = 1 : size(in.Bfactor, 2)
    out.time{n} = T{n}(:, 1);
    %out.angle{n} = (PHI{n}(:, 1) * 180 / pi());
    out.angle{n} = PHI{n}(:, 1);
    out.speed{n} = PHI{n}(:, 2);
    out.accel{n} = diff(PHI{n}(:, 2));
end;
out.zero = zeros(1, size(out.time{1}, 1));

clearvars T PHI;

% Phase portrait limits
graph.lim_x(1) = round(max(out.angle{1}), 1);
graph.lim_x(2) = round(min(out.angle{1}), 1);
graph.lim_y(1) = round(max(out.speed{1}) * 10) / 10; 
graph.lim_y(2) = -graph.lim_y(1);

graph.legend{size(in.Bfactor, 2), 1} = '';
graph.legend{1} = 'No damping';
for n = 2 : size(in.Bfactor, 2)
    graph.legend{n} = sprintf('Damping B=%.2f', in.Bfactor(n));
end;
clearvars n;

%% ===== Plot =====
figure(1)
hold on
for n = 1 : size(in.Bfactor, 2)
    plot(out.time{n}, out.angle{n} * 180 / pi(), 'LineWidth', graph.lt);
end;
clearvars n;
plot(out.time{1}, out.zero, 'k');
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('Time [s]');
ylabel('Pendulum swing [\circ]');
title(sprintf('Motion of a pendulum of length l=%.3f[m]', in.l));
legend(graph.legend, 'location', 'best');
hold off

figure(2);
for n = 1 : size(in.Bfactor, 2)
    subplot(2, 2, n);
    plot(out.angle{n}, out.speed{n}, 'LineWidth', graph.lt);
    set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
    xlabel('$$\varphi$$', 'Interpreter', 'latex');
    xlim([graph.lim_x(2) graph.lim_x(1)]);
    ylabel('$$\frac{d\varphi}{dt}$$', 'Interpreter', 'latex');
    ylim([graph.lim_y(2) graph.lim_y(1)]);
    title(sprintf('Phase portrait - %s', graph.legend{n}));
end;
clearvars n;

%% ===== End =====
