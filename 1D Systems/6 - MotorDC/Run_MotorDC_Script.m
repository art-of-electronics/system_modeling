clc; clear; close all;

%% ===== Global parameters =====
global in;

%% ===== Graph parameters =====
graph.lt = 3; graph.fntsz = 15; graph.fnt = 'Consolas';

%% ===== Model parameters =====
% Voltage
in.U = 400; % Input voltage [V]

% Electrical parameters
in.R = 0.7; % Winding Resistance [Ohm]
in.L = 0.05; % Winding inductance [H]
in.Mt = [0 35 50]; % Loading torque [Nm]

% Mechanical parameters
in.r1 = 0.1; % Rotor inner diameter [m]
in.r2 = 0.15; % Rotor outer diameter [m]
in.h = 0.1; % Rotor length [m]
in.rho = 8700; % Rotor material density [kg/m3]

in.B = 0.01; % Shaft bearings friction
in.J = (pi() * in.rho * (in.r2^4 - in.r1^4) * in.h) / 2; % Rotor inertia

% Motor constants
in.kv = 130; % Kv rating
in.ke = (in.kv / 1000) * (60 / (2 * pi())); % Electrical constant [Vs/rad]
in.km = in.ke; % Mechanical constant [Nm/A]

%% ===== Simulation parameters =====
param.tmax = [0 13];
param.ic = [0 0 0 0];
param.options = odeset('RelTol', 1e-3, 'AbsTol', 1e-3);

%% ===== Simulation =====
param.simtime = zeros(size(in.Mt, 2), 1);
for i = 1 : size(in.Mt, 2)
    in.Mt_val = in.Mt(i);
    tic;
    [out.time{i}, Data{i}] = ode45(@MotorDC_Script, param.tmax, param.ic, param.options);
    param.simtime(i) = toc;
    fprintf('Loop %d time of performing calculations: %.3fs\n', i, param.simtime(i));
end;
clearvars i;

%% ===== Calculations =====
%out.time = simout.Time;
for i = 1 : size(in.Mt, 2)
    out.phi0{i} = Data{i}(:, 1);            % Angular displacement
    out.phi1{i} = Data{i}(:, 2);            % Angular speed
    out.phi2{i} = [diff(out.phi1{i}); 0];   % Angular acceleration
    out.q0{i} = Data{i}(:, 3);              % Charge
    out.q1{i} = Data{i}(:, 4);              % Current
    out.q2{i} = [diff(out.q1{i}); 0];       % Charge 2nd derivative
    out.rpm{i} = out.phi1{:, i} * 60 / (2 * pi);
    
    graph.legend1{i} = sprintf('\\phi at Mt=%.1fNm', in.Mt(i));
    graph.legend2{i} = sprintf('I at Mt=%.1fNm', in.Mt(i));
end;

clearvars Data i

%% ===== Plot =====
figure(1)
subplot(2, 1, 1);
hold on;
for i = 1 : size(in.Mt, 2)
    plot(out.time{i}, out.rpm{i}, 'LineWidth', graph.lt);
end;
hold off;
grid on;
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('Time [s]');
ylabel(sprintf('Shaft RPM \\phi[min^{-1}]'));
title(sprintf('\\phi=f(M_{t}) for DC motor: R=%.1f\\Omega, L=%.1fmH', in.R, in.L * 1000));
legend(graph.legend1, 'location', 'best');
subplot(2, 1, 2);
hold on;
for i = 1 : size(in.Mt, 2)
    plot(out.time{i}, out.q1{i}, 'LineWidth', graph.lt);
end;
hold off;
grid on;
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('Time [s]');
ylabel('Winding current [A]');
title(sprintf('I=f(M_{t}) for DC motor: R=%.1f\\Omega, L=%.1fmH', in.R, in.L * 1000));
legend(graph.legend2, 'location', 'best');
clearvars i

figure(2)
subplot(2, 2, 1);
plot(out.phi1{1}, out.phi2{1}, 'LineWidth', graph.lt);
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('$$\frac{d\varphi}{dt}$$', 'Interpreter', 'latex');
ylabel('$$\frac{d^{2}\varphi}{dt^{2}}$$', 'Interpreter', 'latex');
title('Mechanical - no load');
subplot(2, 2, 3);
plot(out.phi1{end}, out.phi2{end}, 'LineWidth', graph.lt);
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('$$\frac{d\varphi}{dt}$$', 'Interpreter', 'latex');
ylabel('$$\frac{d^{2}\varphi}{dt^{2}}$$', 'Interpreter', 'latex');
title('Mechanical - under load');
subplot(2, 2, 2);
plot(out.q1{1}, out.q2{1}, 'LineWidth', graph.lt);
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('$$i$$', 'Interpreter', 'latex');
ylabel('$$\frac{di}{dt}$$', 'Interpreter', 'latex');
title('Electrical - no load');
subplot(2, 2, 4);
plot(out.q1{end}, out.q2{end}, 'LineWidth', graph.lt);
set(gca, 'FontSize', graph.fntsz, 'FontName', graph.fnt);
xlabel('$$i$$', 'Interpreter', 'latex');
ylabel('$$\frac{di}{dt}$$', 'Interpreter', 'latex');
title('Electrical - under load');
s = suptitle('Phase portrait of DC motor submodels');
set(s, 'FontSize', graph.fntsz, 'FontName', graph.fnt, 'FontWeight', 'bold');
clearvars s

%% ===== End =====
