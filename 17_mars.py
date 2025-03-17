import math
from abc import ABC, abstractmethod


class Forme(ABC):
    def __init__(self, couleur= "noir", rempli="False"):
        self.couleur = couleur
        self.rempli = rempli

    @abstractmethod
    def aire(self):
        """elle va retourner la forme"""
        pass

    @abstractmethod
    def perimetre(self):
        """Elle va calculer la perimetre de la forme"""
        pass

class GroupeFormes:
    """Cette classe représent3 un groupe de forme"""
    def __init__(self, malisteformes = None):
        self.formes = []
        if malisteformes is not None:
            for forme in malisteformes:
                self.ajouter(forme)

    def ajouter(self, forme):
        if not isinstance(forme, Forme):
            raise TypeError("L'objet doit être une instance de la forme")
        self.formes.append(forme)

    def aire_totale(self):
        """Calcule la somme totale des aires des formes"""
        return sum(forme.aire() for forme in self.formes)

    def __iter__(self):
        """Elle permet d'iterer"""
        return iter(self.formes)

class Rectangle(Forme):
    def __init__(self, couleur = "rouge", rempli = "False", largeur = 1.0, longueur = 2.0):
        super().__init__(couleur, rempli)
        self.largeur = largeur
        self.longueur = longueur

    def aire(self):
        return self.largeur * self.longueur

    def perimetre(self):
        return (self.largeur + self.longueur)* 2

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.aire() + other.aire()
        else:
            raise TypeError("L'opération n'est possible que entre 2 rectangle")

    def __mul__(self, nb):
        if isinstance(nb, (int, float)):
            return Rectangle(
                self.couleur,
                self.rempli,
                self.largeur,
                self.longueur*nb)
        else:
            raise TypeError("Le multiplicateur doit etre une nombre")

class cercle(Forme):
    def __init__(self, couleur = "rouge", rempli = "False", rayon = 1.0):
        super().__init__(couleur, rempli)
        self.rayon = rayon

    def aire(self):
        return math.pi*self.rayon**2

    def perimetre(self):
        return 2*math.pi*self.rayon

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.aire() + other.aire()
        else:
            raise TypeError("L'opération n'est possible que entre 2 cercle")


