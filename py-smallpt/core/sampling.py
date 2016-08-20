from math import sqrt, cos, sin
from math_tools import M_PI
from vector import Vector3

def uniform_sample_on_hemisphere(u1, u2):
    r = sqrt(max(0.0, 1.0 - u1 * u1))
    phi = 2.0 * M_PI * u2
    return Vector3(r * cos(phi), r * sin(phi), u1)