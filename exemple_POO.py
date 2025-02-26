class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

#NOM
    @property
    def nom(self):
        """ici il s'agit d'un accesseur"""
        return self.__nom

    @nom.setter
    def nom(self, nouveau_nom):
        """ici il s'agit d'un mutateur"""
        if nouveau_nom == "":
            nouveau_nom = "maely"
        self.__nom = nouveau_nom

#PRENOM
    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, prenom):
        self.__prenom = prenom

#AGE
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0 or age > 150:
            age = 18
        self.__age = age


alice = Personne("Alice", "Kenny", -12)
print(alice.age)
print(alice.nom)
alice.nom = ""
print(alice.nom)
alice.age = -52
print(alice.age)