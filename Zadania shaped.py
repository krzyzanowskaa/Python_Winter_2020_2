class Shape:
    def __init__(self, a=10, b=6, c=7):
        self.set_params(a, b, c)

    def set_params(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_a(self):
        return self.a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self.a) + " by " + str(self.b)  + "] at " + str(hex(id(self)))


class Rectangle(Shape):
    def calc_surface(self):
        return self.a*self.b

    def swap_sides(self):
        a = self.a
        b = self.b
        self._a = b
        self.b = a

import math

class Circle(Shape):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, 0)
        #self.a = a

    def calc_surface(self):
        return math.pi * self.a**2

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self.a) + "] at " + str(hex(id(self)))

class Triangle(Shape):
    def calc_surface(self):
        z = (self.a + self.b + self.c)/2
        return math.sqrt(z*(z-self.a)*(z-self.b)* (z-self.c))

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self.a) + " by " + str(self.b) + " by " + str(self.c) + "] at " + str(hex(id(self)))

class EquilateralTriangle(Shape):
    @property
    def calc_surface(self):
        s = (3 * self.a)/2
        return math.sqrt(s*(s-self.a)*(s-self.a)*(s-self.a))

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self.a) + " by " + str(self.a) + " by " + str(self.a) + "] at " + str(hex(id(self)))

r = Rectangle(5, 6)
print(r)
#r._a = 600
print(r.calc_surface())
r.swap_sides()
print(r)

c = Circle(7)
print(c)
print(c.calc_surface())

t = Triangle(10, 6, 7)
print(t)
print(t.calc_surface())

e = EquilateralTriangle(5)
print(e)
print(e.calc_surface)