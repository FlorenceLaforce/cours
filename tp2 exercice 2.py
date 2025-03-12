from abc import ABC, abstractmethod
import math

class MonctionMathematique(ABC):

    @abstractmethod
    def evaluer(self, x):
        pass

class parabole(MonctionMathematique):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def evaluer(self, x):
        return self.__a * x**2 + self.__b * x + self.__c

    def __str__(self):
        return f"{self.__a}x² + {self.__b}x + {self.__c}"

class exponential(MonctionMathematique):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def evaluer(self, x):
        return self.__a * math.exp(self.__b * x)

    def __str__(self):
        return f"{self.__a} * exp({self.__b}x)"

class sinusoide(MonctionMathematique):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def evaluer(self, x):
        return self.__a * math.sin(self.__b * x + self.__c)

    def __str__(self):
        return f"{self.__a} * sin({self.__b}x + {self.__c})"

#Parabole
p1 = parabole(4,2,1)
print(p1)
print(p1.evaluer(2))

#Expodentiel
E1 = exponential(4,2)
print(E1)
print(E1.evaluer(2))

#sinusoide
S1 = sinusoide(4,2,1)
print(S1)
print(S1.evaluer(2))