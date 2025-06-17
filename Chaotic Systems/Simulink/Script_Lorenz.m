clear; close all;

sigma = 9.99;
r = 28;
b = 8/3;

dy = @(t, y) [sigma * (y(2) - y(1));
    -y(1) * y(3) + r * y(1) - y(2);
    y(1) * y(2) - b * y(3)];

[t, y] = ode45(dy, [-100 100], [0 0.5 1]);

plot3(y(:, 1), y(:, 2), y(:, 3));