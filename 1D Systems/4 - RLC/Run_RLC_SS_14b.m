clc; clear; close all;
%% ===== Graph parameters =====
graph.lt = 2; graph.fntsz = 15; graph.fnt = 'Hellvetica';

%% ===== Model parameters =====
in.R = 1;							  % Resistance
in.L = floor(10 * rand() + 1) * 1e-3; % Inductance in mH
in.C = floor(10 * rand() + 1) * 1e-6; % Capacitance in uF
in.U = 10;                            % Input voltage in V

RLC.f0 = 1 / (2 * pi() * sqrt(in.L * in.C));
freq.fmin = 0.6 * RLC.f0;
freq.fmax = 1.4 * RLC.f0;

%% ===== Simulation parameters =====
param.tmax = 10;
param.step = 0.0001;
param.ic = [0 0];

%% ===== Simulation =====
param.options = simset('MaxStep', param.step);
load_system('Model_RLC_SS_14b');
open_system('Model_RLC_SS_14b');
sim('Model_RLC_SS_14b', param.tmax, param.options);

%% ===== End =====
