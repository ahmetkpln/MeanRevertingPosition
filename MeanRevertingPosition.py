def MeanRevertingPosition(signal, upper, lower):
    position = [0 for i in range(len(signal))]
    for i in range(1, len(signal)):
        if position[i-1] == 0:
            if signal[i-1] > upper[i-1]: position[i] = -1
            if signal[i-1] < lower[i-1]: position[i] = 1
        elif position[i-1] == -1:
            if signal[i-1] > lower[i-1]: position[i] = -1
            if signal[i-1] < lower[i-1]: position[i] = 1            
        elif position[i-1] == 1:
            if signal[i-1] < upper[i-1]: position[i] = 1
            if signal[i-1] > upper[i-1]: position[i] = -1            
        else:
            position[i] = position[i-1]
    return position
