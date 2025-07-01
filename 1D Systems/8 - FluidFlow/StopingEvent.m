function [value, isterminal, direction] = StopingEvent(~, h)
    
    value = real(h);        % When h == 0 (no water in tank)
    isterminal = 1;         % Stop the integration
    direction = -1;         % Only trigger when h is decreasing (falling)
end