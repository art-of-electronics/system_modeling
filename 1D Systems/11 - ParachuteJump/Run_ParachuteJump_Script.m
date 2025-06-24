clc; clear; close all;

%% ===== Global parameters =====
global in;

%% ===== Graph parameters =====
graph.lt = 3; graph.fntsz = 15; graph.fnt = 'Times New Roman';

%% ===== Model parameters =====
in.m = 110;         % Mass of skydiver
in.c = [0.5 1.42];  % Reynolds excellence factor
in.A = [1.5 28];    % Area of skydiver without and with parachhute 
in.H = 5000;        % Initial jumo-out altitude
in.h0 = 2000;       % Parachute opening altitude

%% ===== Simulation parameters =====
param.tmax = [0 700];
param.ic = [0 0];
param.options = odeset('RelTol', 1e-4, 'AbsTol', 1e-4, 'Events', @GroundingEvent);

%% ===== Simulation =====
[out.time, out.Y] = ode45(@ParachuteJump_Script, param.tmax, param.ic, param.options);
out.Y(:, 3) = [diff(out.Y(:, 2))', 0]';

%% ===== Calculations =====
for i = 1 : size(out.time, 1)
    out.Y(i, 1) = in.H - out.Y(i, 1);           % Calculate falling
    out.Y(i, 2) = 3.6 * out.Y(i, 2);            % Convert m/s -> km/h
    out.Y(i, 3) = (9.81 - out.Y(i, 3)) / 9.81;  % Normalize G
end
clearvars i;

graph.ylabel{1} = 'Altitude [m]';
graph.ylabel{2} = 'Speed [km/h]';
graph.ylabel{3} = 'Acceleration [G]';
graph.title = sprintf('Parachute jump, skydiver m=%dkg', in.m);

%% ===== Plot =====
figure(1)
for i = 1 : 3
    subplot(3, 1, i)
    plot(out.time, out.Y(: , i), 'LineWidth', graph.lt)
    if i == 1
        title(graph.title);
    end
    set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
    xlim([0 out.time(end)]);
    grid on;
    xlabel('czas [s]');
    ylabel(graph.ylabel{i});
end
clearvars i;

%% ===== End =====
