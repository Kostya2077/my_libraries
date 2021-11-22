import math


class FuzzyAbstract:

    def __init__(self, value):
        if isinstance(value, FuzzyAbstract):
            self.value = value.value
        else:
            self.value = float(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value <= 0.0:
            self.__value = 0.0
        elif value >= 1.0:
            self.__value = 1.0
        else:
            self.__value = value

    def __repr__(self):
        return str(self.__value)

    def toBool(self, threshold = 0.5):
        if self.__value < threshold:
            return False
        else:
            return True

    def toInt(self, threshold = 0.5):
        if self.__value < threshold:
            return 0
        else:
            return 1


    def __neg__(self):
        return FuzzyMinMax(1.0 - self.__value)

    def Not(self):
        return FuzzyMinMax(1.0 - self.__value)


    def __eq__(self, other):
        if isinstance(other, FuzzyAbstract):
            return self.__value == other.__value
        elif isinstance(other, bool):
            return self.toBool() == other
        elif isinstance(other, int):
            return self.toInt() == other
        else:
            return self.__value == other


    def __ne__(self, other):
        if isinstance(other, FuzzyAbstract):
            return self.__value != other.__value
        elif isinstance(other, bool):
            return self.toBool() != other
        elif isinstance(other, int):
            return self.toInt() != other
        else:
            return self.__value != other



    def __lt__(self, other):
        if isinstance(other, FuzzyAbstract):
            return self.__value < other.__value
        else:
            return self.__value < float(other)



    def __le__(self, other):
        if isinstance(other, FuzzyAbstract):
            return self.__value <= other.__value
        else:
            return self.__value <= float(other)



    def __gt__(self, other):
        if isinstance(other, FuzzyAbstract):
            return self.__value > other.__value
        else:
            return self.__value > float(other)


    def __ge__(self, other):
        if isinstance(other, FuzzyAbstract):
            return self.__value >= other.__value
        else:
            return self.__value >= float(other)




class FuzzyMinMax(FuzzyAbstract):
    def __init__(self, value):
        super().__init__(value)

    def __and__(self, other):
        if isinstance(other, FuzzyAbstract):
            val = min(self.value, other.value)
        else:
            val = min(self.value, float(other))
        return FuzzyMinMax(val)

    def __radd__(self, other):
        if isinstance(other, FuzzyAbstract):
            val = min(self.value, other.value)
        else:
            val = min(self.value, float(other))
        return FuzzyMinMax(val)


    def __or__(self, other):
        if isinstance(other, FuzzyAbstract):
            val = max(self.value, other.value)
        else:
            val = max(self.value, float(other))
        return FuzzyMinMax(val)


    def __ror__(self, other):
        if isinstance(other, FuzzyAbstract):
            val = max(self.value, other.value)
        else:
            val = max(self.value, float(other))
        return FuzzyMinMax(val)



class FuzzyColorometric(FuzzyAbstract):
    def __init__(self, value):
        if type(value) == FuzzyMinMax:
            value = value.value
        super().__init__(value)

    def __and__(self, other):
        result = self.value * other.value
        return FuzzyColorometric(result)

    def __or__(self, other):
        result = self.value + other.value - self.value * other.value
        return FuzzyColorometric(result)



class FuzzyAddMul(FuzzyAbstract):
    def __init__(self, value):
        super().__init__(value)

    def __and__(self, other):
        if isinstance(other, FuzzyAbstract):
            val = self.value * other.value
        else:
            val = self.value * float(other)
        return FuzzyAddMul(val)

    def __rand__(self, other):
        if isinstance(other, FuzzyAbstract):
            val = self.value * other.value
        else:
            val = self.value * float(other)
        return FuzzyAddMul(val)

    def __or__(self, other):
        if isinstance(other, FuzzyAbstract):
            val = self.value + other.value - self.value * other.value
        else:
            val = self.value + float(other) - self.value * float(other)
        return FuzzyAddMul(val)

    def __ror__(self, other):
        if isinstance(other, FuzzyMinMax):
            val = self.value + other.value - self.value * other.value
        else:
            val = self.value + float(other) - self.value * float(other)
        return FuzzyAddMul(val)




'''





def fuzzyParabolicFunction(x, x1, x2, y_min, y_max):

    hx = (x2 + x1) / 2

    if x <= x1:
        return y_min

    elif x >= x2:
        return y_min

    else:
        if y_min == y_max:
            return y_min
        elif x1 == x2:
            return  (y_min + y_max) / 2.0
        else:
            return 4 * (y_min - y_max)*((x - hx) / (x1 - x2))**2 + y_max




def fuzzyInverseParabolicFunction(x, x1, x2, y_min, y_max):

    hx = (x2 + x1) / 2

    if x <= x1:
        return y_max

    elif x >= x2:
        return y_max

    else:
        if y_min == y_max:
            return y_min
        elif x1 == x2:
            return  (y_min + y_max) / 2.0
        else:
            return 4 * (y_max - y_min)*((x - hx) / (x1 - x2))**2 + y_min




def fuzzyTwoParabolicFunction(x, x1, x2, y1, y2):
    hx = (x1 + x2) / 2
    hy = (y1 + y2) / 2
    if y1 <= y2:
        if x <= hx:
            return fuzzyHalfParabolicFunction(x, x1, hx, y1, hy)
        else:
            return fuzzyInverseHalfParabolicFunction(x, hx, x2, hy, y2)
    else:
        if x <= hx:
            return fuzzyInverseHalfParabolicFunction(x, x1, hx, y1, hy)
        else:
            return fuzzyHalfParabolicFunction(x, hx, x2, hy, y2)

def fuzzyTwoParabolicPickFunction(x, x1, x2, y_min, y_max):
    hx = (x1 + x2) / 2
    if x <= hx:
        return fuzzyTwoParabolicFunction(x, x1, hx, y_min, y_max)
    else:
        return fuzzyTwoParabolicFunction(x, hx, x2, y_max, y_min)




def fuzzyExponentFunction(x, x1, x2, y1, y2):
    hx = (x1 + x2) / 2
    sigma = (x2 - x1) / 6
    f = math.fabs(y2 - y1)

    if y1 <= y2:
        return f / (1 + math.exp(- sigma * (x - hx))) + y1
    else:
        return f * (1 - 1 / (1 + math.exp(- sigma * (x - hx)))) + y2








def fuzzyExponentTriagleFunction(x, x1, x2, y_min, y_max):

    a = (x1 + x2) / 2
    sigma = (x2 - x1) / 6
    f = y_max - y_min


    if x1 != x2:
        tmp = (x - a) / sigma
        return f * math.exp(- tmp * tmp / 2) + y_min
    else:
        return (y_max + y_min) / 2 + y_min








def fuzzyInverseHalfParabolicFunction(x, x1, x2, y1, y2):

    if x <= x1:
        return y1
    elif x >= x2:
        return y2
    else:
        if y1 == y2:
            return y1
        elif x1 == x2:
            return  (y1 + y2) / 2.0
        else:
            if y1 <= y2:
                return (y1 - y2)*((x - x2) / (x1 - x2))**2 + y2
            else:
                return (y2 - y1)*((x - x1) / (x1 - x2))**2 + y1

'''
