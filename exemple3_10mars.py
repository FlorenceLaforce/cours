class animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def faire_son(self):
        return "Son generique d'animal"

    def se_deplacer(self):
        return "Se deplace d'une manière generique"

class chien(animal):
    def __init__(self, nom, age, race):
        super().__init__(nom, age)
        self.race = race

    def faire_son(self):
        return "Woof!"

    def se_deplacer(self):
        return "Court sur 4 pattes"

    def chercher(self):
        return f"{self.nom} va chercher le baton!"


class chat(animal):
    def __init__(self, nom, age, poil_long=False):
        super().__init__(nom, age)
        self.poil_long = poil_long

    def faire_son(self):
        return "Miaou!"

    def se_deplacer(self):
        return "se deplace silencieusement"

    def grimper(self):
        return f"{self.nom} grimpe dans l'arbre"

