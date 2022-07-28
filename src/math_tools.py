from math import pow

M_PI = 3.14159265358979323846

def clamp(x, low = 0.0, high = 1.0):
    if x > high:
        return high
    if x < low:
        return low
    return x

def to_byte(x, gamma = 2.2):
    return int(clamp(255.0 * pow(x, 1.0 / gamma), 0.0, 255.0))