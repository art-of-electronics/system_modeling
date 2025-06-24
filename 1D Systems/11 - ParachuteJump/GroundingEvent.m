function [value, isterminal, direction] = GroundingEvent(~, y)
    global in
    
    value = in.H - y(1);    % When y(1) == 0 (ground level)
    isterminal = 1;         % Stop the integration
    direction = -1;         % Only trigger when y is decreasing (falling)
end