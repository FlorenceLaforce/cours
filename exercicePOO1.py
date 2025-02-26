from math import sqrt
class cartesien:
    """Initialistaion d'une instance de point"""
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_X(self):
        """Ici on retourne les coordonnees x"""
        return self.__x
    def get_Y(self):
        """Ici on retourne les coordonnees y"""
        return self.__y


    def distance(self,):
        """Determiner distance"""
        return sqrt(self.__x ** 2 + self.__y ** 2)

monpoint = cartesien(3,4)
print(F"Les coordonnees de ce point sont : ({monpoint.get_X()}, {monpoint.get_Y()})")
print(F"La distance de ce point par rapport a l'origine est de : {monpoint.distance()}")