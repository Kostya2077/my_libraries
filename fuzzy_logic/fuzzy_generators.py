from libraries.fuzzy_logic.fuzzy_function import *

class FuzzyLineGenerator:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def generate(self, x):
        return fuzzyLineFunction(x, self.x1, self.y1, self.x2, self.y2)

    def __call__(self, *args, **kwargs):
        return fuzzyLineFunction(args[0], self.x1, self.y1, self.x2, self.y2)


class FuzzyTriangleGenerator:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def generate(self, x):
        return fuzzyTriangleFunction(x, self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)

    def __call__(self, *args, **kwargs):
        return fuzzyTriangleFunction(args[0], self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)


class FuzzyParabolicTriangleGenerator:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def generate(self, x):
        return fuzzyParabolicTriangle(x, self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)

    def __call__(self, *args, **kwargs):
        return fuzzyParabolicTriangle(args[0], self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)


class FuzzyParabolicPickGenerator:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def generate(self, x):
        return fuzzyParabolicPick(x, self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)

    def __call__(self, *args, **kwargs):
        return fuzzyParabolicPick(args[0], self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)


class FuzzyHalfParabolicGenerator:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def generate(self, x):
        return fuzzyHalfParabolicFunction(x, self.x1, self.y1, self.x2, self.y2)

    def __call__(self, *args, **kwargs):
        return fuzzyHalfParabolicFunction(args[0], self.x1, self.y1, self.x2, self.y2)


class FuzzyTrapezoidGenerator:

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def generate(self, x):
        return fuzzyTrapezoidFunction(x, self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4)

    def __call__(self, *args, **kwargs):
        return fuzzyTrapezoidFunction(args[0], self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4)



class FuzzyLeftBellGenerator:

    def __init__(self, x_c, y_c, y = 0, a = 1, b = 1):
        self.x_c = x_c
        self.y_c = y_c
        self.y = y
        self.a = a
        self.b = b

    def generate(self, x):
        return fuzzyLeftHalfBell(x, self.x_c, self.y_c, self.y, self.a, self.b)

    def __call__(self, *args, **kwargs):
        return fuzzyLeftHalfBell(args[0], self.x_c, self.y_c, self.y, self.a, self.b)



class FuzzyRightBellGenerator:

    def __init__(self, x_c, y_c, y = 0, a = 1, b = 1):
        self.x_c = x_c
        self.y_c = y_c
        self.y = y
        self.a = a
        self.b = b

    def generate(self, x):
        return fuzzyRightHalfBell(x, self.x_c, self.y_c, self.y, self.a, self.b)

    def __call__(self, *args, **kwargs):
        return fuzzyRightHalfBell(args[0], self.x_c, self.y_c, self.y, self.a, self.b)



class FuzzyBellGenerator:

    def __init__(self, x_c, y_c, y = 0, a = 1, b = 1):
        self.x_c = x_c
        self.y_c = y_c
        self.y = y
        self.a = a
        self.b = b

    def generate(self, x):
        return fuzzyBell(x, self.x_c, self.y_c, self.y, self.a, self.b)

    def __call__(self, *args, **kwargs):
        return fuzzyBell(args[0], self.x_c, self.y_c, self.y, self.a, self.b)


