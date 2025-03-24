import math

class Circle:
    def __init__(self, radius):
        self.r = radius

    def area(self):
        return math.pi * (self.r * self.r)
    area = property(area)

    # equivalent to ...
    # @property
    # def area(self):
    #     return math.pi * (self.r * self.r)
