class moteur:
    def __init__(self, cylindree, type):
        self.cylindree = cylindree
        self.type = type
        self.est_demarrer = False

    def demarrer(self):
        self.est_demarrer = True
        return f"Moteur: {self.type} {self.cylindree}cc demarre"

    def arreter(self):
        self.est_demarrer = False
        return "Moteur arrete"

class voiture:
    def __init__(self, marque, modele, cylindre_moteur, type_moteur):
        self.marque = marque
        self.modele = modele
        #le moteur est crée à l'intérieur de la voiture
        self.moteur = moteur(cylindre_moteur, type_moteur)

    def demarrer(self):
        return f"{self.marque} {self.modele} {self.moteur.demarrer()}"

    def arreter(self):
        return f"{self.marque} {self.modele} {self.moteur.arreter()}"


ma_voiture = voiture("porsche", "911", 10, "essence")
print(ma_voiture.arreter())
print(ma_voiture.demarrer())