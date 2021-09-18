def rainbowRGB(n, frequency = .1, waveCenter = 128, waveWidth = 127, rPhase = 2, gPhase = 0, bPhase = 4):
    from math import sin

    r = int(sin(frequency * n + rPhase) * waveWidth + waveCenter)
    g = int(sin(frequency * n + gPhase) * waveWidth + waveCenter)
    b = int(sin(frequency * n + bPhase) * waveWidth + waveCenter)
    
    return (r, g, b)
