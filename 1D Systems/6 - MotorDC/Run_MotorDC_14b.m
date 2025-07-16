clc; clear; close all;

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
param.tmax = 13;
param.step = 0.001;
param.options = simset('MaxStep', param.step);

%% ===== Simulation =====
load_system('Model_MotorDC_14b');
open_system('Model_MotorDC_14b');
sim('Model_MotorDC_14b', param.tmax, param.options);

%% ===== Calculations =====
out.time = simout.Time;
for i = 1 : size(in.Mt, 2)
    out.rpm{i} = simout.Data(:, i);
    out.phi1{i} = simout.Data(:, i + (1 * size(in.Mt, 2))); % Angular speed
    out.phi2{i} = simout.Data(:, i + (2 * size(in.Mt, 2))); % Angular acceleration
    out.q2{i} = simout.Data(:, i + (3 * size(in.Mt, 2)));   % Charge 2nd derivative
    out.q1{i} = simout.Data(:, i + (4 * size(in.Mt, 2)));   % Current
    
    graph.legend1{i} = sprintf('\\phi at Mt=%.1fNm', in.Mt(i));
    graph.legend2{i} = sprintf('I at Mt=%.1fNm', in.Mt(i));
end;

clearvars tout simout i

%% ===== Plot =====
figure(1)
subplot(2, 1, 1);
hold on;
for i = 1 : size(in.Mt, 2)
    plot(out.time, out.rpm{i}, 'LineWidth', graph.lt);
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
    plot(out.time, out.q1{i}, 'LineWidth', graph.lt);
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
