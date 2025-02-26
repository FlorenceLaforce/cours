class rectangle:
    def __init__(self, longueur, largeur):
        if longueur < 0 and largeur < 0:
            raise ValueError("largeur et longueur invalide")
        self.__longueur = longueur
        self.__largeur = largeur

    @property
    def longueur(self):
        return self.__longueur

    @longueur.setter
    def longueur(self, nouvelle_longueur):
        if nouvelle_longueur > 0:
            self.__longueur = nouvelle_longueur
        else:
            raise ValueError("longueur invalide, doit etre positive")

    @property
    def largeur(self):
        return self.__largeur

    @largeur.setter
    def largeur(self, nouvelle_largeur):
        if nouvelle_largeur > 0:
            self.__largeur = nouvelle_largeur
        else:
            raise ValueError("largeur invalide, doit etre positive")

    @property
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    @property
    def aire(self):
        return self.__largeur * self.__longueur



mon_rectangle = rectangle(5, 3)
print(f"longueur : {mon_rectangle.longueur}, largueur : {mon_rectangle.largeur}, perimetre : {mon_rectangle.perimetre}")
print(f"aire : {mon_rectangle.aire}")