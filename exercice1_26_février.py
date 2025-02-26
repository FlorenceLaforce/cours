#exercice 1
from abc import ABC, abstractmethod
class forme(ABC):

    @property
    @abstractmethod
    def aire(self):
        pass


    @abstractmethod
    def perimetre(self):
        pass

    def afficher_forme(self):
        return "ceci est une forme"



class rectangle(forme):

    def __init__(self, base, hauteur):
        if base > 0 and hauteur > 0:
            self.__base = base
            self.__hauteur = hauteur
        else:
            raise ValueError("Base and hauteur must be positive")


    @property
    def aire(self):
        return self.__base * self.__hauteur

    def perimetre(self):
        return self.__base * 2 + self.__hauteur * 2

    def afficher_rectangle(self):
        return "ceci est une rectangle"

class carre(forme):

    def __init__(self, cotes):
        if cotes > 0:
            self.__cotes = cotes
        else:
            raise ValueError("Cotes must be positive")

    @property
    def aire(self):
        return self.__cotes ** 2

    def perimetre(self):
        return self.__cotes * 4

    def afficher_carre(self):
        return "ceci est un carre"


carre = carre(2)
print(carre.aire)
print(carre.perimetre())
print(carre.afficher_carre())

rectangle = rectangle(8, 5)
print(rectangle.aire)
print(rectangle.perimetre())
print(rectangle.afficher_rectangle())
