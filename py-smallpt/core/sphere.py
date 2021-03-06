from math import sqrt
from vector import Vector3

class Sphere(object):

    EPSILON_SPHERE = 1e-4

    class Reflection_t(object):
        DIFFUSE, SPECULAR, REFRACTIVE = range(3)

    def __init__(self, r, p, e = Vector3(), f = Vector3(), reflection_t = Reflection_t.DIFFUSE):
        self.r = float(r)
        self.p = p.__copy__()
        self.e = e.__copy__()
        self.f = f.__copy__()
        self.reflection_t = reflection_t

    def intersect(self, ray):
        # (o + t*d - p) . (o + t*d - p) - r*r = 0
        # <=> (d . d) * t^2 + 2 * d . (o - p) * t + (o - p) . (o - p) - r*r = 0
        # 
        # Discriminant check
        # (2 * d . (o - p))^2 - 4 * (d . d) * ((o - p) . (o - p) - r*r) <? 0
        # <=> (d . (o - p))^2 - (d . d) * ((o - p) . (o - p) - r*r) <? 0
        # <=> (d . op)^2 - 1 * (op . op - r*r) <? 0
        # <=> b^2 - (op . op) + r*r <? 0
        # <=> D <? 0
        #
        # Solutions
        # t = (- 2 * d . (o - p) +- 2 * sqrt(D)) / (2 * (d . d))
        # <=> t = dop +- sqrt(D)

        op = self.p - ray.o
        dop = ray.d.dot(op)
        D = dop * dop - op.dot(op) + self.r * self.r

        if D < 0:
            return False

        sqrtD = sqrt(D)

        tmin = dop - sqrtD
        if (ray.tmin < tmin and tmin < ray.tmax):
            ray.tmax = tmin
            return True

        tmax = dop + sqrtD
        if (ray.tmin < tmax and tmax < ray.tmax):
            ray.tmax = tmax
            return True
        
        return False