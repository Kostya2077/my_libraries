from libraries.fuzzy_logic.fuzzy_logic import *
import math


def fuzzyLineFunction(x, x1, y1, x2, y2):

    if x <= x1:
        # левый хвост
        return y1
    elif x >= x2:
        # правый хвост
        return y2
    else:
        # наклонная
        if x1 != x2:
            # не параллельна оси
            k = (y1 - y2) / (x1 - x2)
            b = y1 - k * x1
            return k * x + b
        else:
            # параллельна оси
            return (y1 + y2) / 2




def fuzzyTriangleFunction(x, x1, y1, x2, y2, x3, y3):
    if x < x2:
        return fuzzyLineFunction(x, x1, y1, x2, y2)
    else:
        return fuzzyLineFunction(x, x2, y2, x3, y3)




def fuzzyTrapezoidFunction(x, x1, y1, x2, y2, x3, y3, x4, y4):
    if x < x2:
        return fuzzyLineFunction(x, x1, y1, x2, y2)
    elif x < x3:
        return fuzzyLineFunction(x, x2, y2, x3, y3)
    else:
        return fuzzyLineFunction(x, x3, y3, x4, y4)



def fuzzyHalfParabolicFunction(x, x_c, y_c, x_g, y_g):

    if x_g < x_c:
        if x < x_g:
            return y_g
        elif x < x_c:
            return (y_g - y_c)*((x - x_c) / (x_c - x_g))**2 + y_c
        else:
            return y_c
    else:
        if x < x_c:
            return y_c
        elif x < x_g:
            return (y_g - y_c) * ((x - x_c) / (x_c - x_g)) ** 2 + y_c
        else:
            return y_g


def fuzzyParabolicTriangle(x, x1, y1, x2, y2, x3, y3):
    if x < x2:
        return fuzzyHalfParabolicFunction(x, x2, y2, x1, y1)
    else:
        return fuzzyHalfParabolicFunction(x, x2, y2, x3, y3)


def fuzzyParabolicPick(x, x1, y1, x2, y2, x3, y3):
    if x < x2:
        return fuzzyHalfParabolicFunction(x, x1, y1, x2, y2)
    else:
        return fuzzyHalfParabolicFunction(x, x3, y3, x2, y2)


def fuzzySFunction(x, x1, y1, x2, y2):
    if x < x1:
        return y1
    elif x < x2:
        hx = (x1 + x2) / 2
        hy = (y1 + y2) / 2
        if x < hx:
            return fuzzyHalfParabolicFunction(x, x1, y1, hx, hy)
        else:
            return fuzzyHalfParabolicFunction(x, x2, y2, hx, hy)
    else:
        return y2




def fuzzySFunctionTriangle(x, x1, y1, x2, y2, x3, y3):
    if x < x2:
        return fuzzySFunction(x, x1, y1, x2, y2)
    else:
        return fuzzySFunction(x, x2, y2, x3, y3)

def fuzzySFunctionTrapezoid(x, x1, y1, x2, y2, x3, y3, x4, y4):
    if x < x2:
        return fuzzySFunction(x, x1, y1, x2, y2)
    elif x < x3:
        return fuzzyLineFunction(x, x2, y2, x3, y3)
    else:
        return fuzzySFunction(x, x3, y3, x4, y4)

def fuzzySigmoid(x, x_c, y_c):
    return (x - x_c) / (math.fabs(x - x_c) + 1) + y_c


def fuzzyLeftHalfBell(x, x_c, y_c, y = 0, a = 1, b = 1):
    k = math.fabs(y_c - y)
    c = x_c
    if x < x_c:
        if y > y_c:
            return  - k / (1 + math.pow((x - c) / a, 2 * b)) + y
        else:
            return k / (1 + math.pow((x - c) / a, 2 * b)) + y
    else:
        return y_c


def fuzzyRightHalfBell(x, x_c, y_c, y = 0, a = 1, b = 1):
    k = math.fabs(y_c - y)
    c = x_c
    if x > x_c:
        if y > y_c:
            return  - k / (1 + math.pow((x - c) / a, 2 * b)) + y
        else:
            return k / (1 + math.pow((x - c) / a, 2 * b)) + y
    else:
        return y_c



def fuzzyBell(x, x_c, y_c, y = 0, a = 1, b = 1):
    k = math.fabs(y_c - y)
    c = x_c
    if y > y_c:
        return  - k / (1 + math.pow((x - c) / a, 2 * b)) + y
    else:
        return k / (1 + math.pow((x - c) / a, 2 * b)) + y

def fuzzyBellTrapezoid(x, y, x1, y1, x2, y2):
    if x < x1:
        return fuzzyBell(x, x1, y1, y)
    elif x < x2:
        return fuzzyLineFunction(x, x1, y1, x2, y2)
    else:
        return fuzzyBell(x, x2, y2, y)


def softmax(iterable):

    sum = 0
    for item in iterable:
        if isinstance(item, FuzzyAbstract):
            sum += math.exp(item.value)
        else:
            sum += math.exp(item)

    result = []
    for item in iterable:
        if isinstance(item, FuzzyAbstract):
            result.append(math.exp(item.value) / sum)
        else:
            result.append(math.exp(item) / sum)

    return result



def hardmax(iterable):

    sum = 0
    for item in iterable:
        if isinstance(item, FuzzyAbstract):
            sum += item.value
        else:
            sum += item

    result = []
    for item in iterable:
        if isinstance(item, FuzzyAbstract):
            result.append(item.value / sum)
        else:
            result.append(item / sum)

    return result