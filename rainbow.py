def rainbowRGB(n, frequency = .1, waveCenter = 128, waveWidth = 127):
    from math import sin

    r = int(sin(frequency * n + 2) * waveWidth + waveCenter)
    g = int(sin(frequency * n + 0) * waveWidth + waveCenter)
    b = int(sin(frequency * n + 4) * waveWidth + waveCenter)
    
    return (r, g, b)
