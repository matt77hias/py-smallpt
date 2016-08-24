from math import sqrt, cos, sin
from math_tools import M_PI
from vector import Vector3

def uniform_sample_on_hemisphere(u1, u2):
    sin_theta = sqrt(max(0.0, 1.0 - u1 * u1))
    phi = 2.0 * M_PI * u2
    return Vector3(cos(phi) * sin_theta, sin(phi) * sin_theta, u1)
	
def cosine_weighted_sample_on_hemisphere(u1, u2):
    cos_theta = sqrt(1.0 - u1)
    sin_theta = sqrt(u1)
    phi = 2.0 * M_PI * u2
    return Vector3(cos(phi) * sin_theta, sin(phi) * sin_theta, cos_theta)