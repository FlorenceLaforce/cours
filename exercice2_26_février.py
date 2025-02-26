from abc import ABC, abstractmethod

class vehicule(ABC):

    @property
    @abstractmethod
    def type_vehicule(self):
        pass

    @abstractmethod
    def demarrer(self):
        pass

    @abstractmethod
    def arreter(self):
        pass

    def afficher_annee(self, annee):
        return f"Ce {self.type_vehicule} à été fabriquer en {annee}"


class voiture(vehicule):
    @property
    def type_vehicule(self):
        return "voiture"
    def demarrer(self):
        return "La voiture démarre avec la clé"
    def arreter(self):
        return "La voiture s'arrête en coupant le moteur"

class avion(vehicule):
    @property
    def type_vehicule(self):
        return "avion"
    def demarrer(self):
        return "L'avion démarre en activant les turbine"
    def arreter(self):
        return "L'avions arrête après l'atterissage"

voiture = voiture()
print(voiture.type_vehicule)
print(voiture.demarrer())
print(voiture.arreter())

avion = avion()
print(avion.type_vehicule)
print(avion.demarrer())
print(avion.arreter())