class Ray(object):

    def __init__(self, o, d, tmin = 0.0, tmax = float('inf'), depth = 0):
        self.o = o.__copy__()
        self.d = d.__copy__()
        self.tmin = tmin
        self.tmax = tmax
        self.depth = depth

    def __call__(self, t):
        return self.o + self.d * t

    def __str__(self):
        return 'o: ' + str(self.o) + '\n' + 'd: ' + str(self.d) + '\n'