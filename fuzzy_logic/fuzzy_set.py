from libraries.fuzzy_logic.fuzzy_function import *

class FuzzySet:

    def __init__(self, values, type=FuzzyAddMul):
        tmp = []
        for v in values:
            if isinstance(v, FuzzyAbstract):
                tmp.append(type(v.value))
            else:
                tmp.append(type(float(v)))
        self.__values = tmp
        self.__type = type

    def __repr__(self):
        return '[values: {} type: [{}]]'.format(self.__values, self.__type)

    @property
    def values(self):
        return self.__values

    @property
    def type(self):
        return self.__type

    def __getitem__(self, i):
        return self.__values[i]

    def __setitem__(self, key, value):
        self.__values[key] = value


    def __and__(self, other):
        if isinstance(other, FuzzySet):
            return  FuzzySet([item[0] & item[1] for item in zip(self.__values, other.values)], self.__type)
        else:
            return  FuzzySet([item[0] & item[1] for item in zip(self.__values, other)], self.__type)


    def __rand__(self, other):
        if isinstance(other, FuzzySet):
            return  FuzzySet([item[0] & item[1] for item in zip(self.__values, other.values)], self.__type)
        else:
            return  FuzzySet([item[0] & item[1] for item in zip(self.__values, other)], self.__type)

    def __or__(self, other):
        if isinstance(other, FuzzySet):
            return  FuzzySet([item[0] | item[1] for item in zip(self.__values, other.values)], self.__type)
        else:
            return  FuzzySet([item[0] | item[1] for item in zip(self.__values, other)], self.__type)

    def __ror__(self, other):
        if isinstance(other, FuzzySet):
            return  FuzzySet([item[0] | item[1] for item in zip(self.__values, other.values)], self.__type)
        else:
            return  FuzzySet([item[0] | item[1] for item in zip(self.__values, other)], self.__type)


    def soft_max(self):
        return FuzzySet(softmax(self.__values), self.__type)

    def hard_max(self):
        return FuzzySet(hardmax(self.__values), self.__type)

    def best(self):
        return self.__values.index(max(self.__values))



class FuzzyGenerator:

    def __init__(self, *generators):
        self.__generators = generators

    def __call__(self, *args, **kwargs):
        return [f(args[0]) for f in self.__generators]

    @property
    def generators(self):
        return self.__generators

    def generate(self, x):
        return [f(x) for f in self.__generators]
