#exercice compte bancaire

class Comptebancaire:
    def __init__(self, solde_initial = 0):
        self.__solde = solde_initial

    def deposer(self, montant_depot):
        """Ici on va deposer un montant au solde"""
        if montant_depot > 0:
            self.__solde += montant_depot
        else:
            print("Le montant doit etre positif")

    def retirer(self, montant_retire):
        if 0<=montant_retire< self.__solde:
            self.__solde -= montant_retire
        elif montant_retire > self.__solde:
            print("Fonds insufisants ")
        else:
            print(";Le montant doit etre positif")

    def afficher_solde(self):
        print(f"Solde actuel : {self.__solde}$")

#À l'exterieur de la classe

compteBanc1 = Comptebancaire(1200)
compteBanc1.retirer(500)
compteBanc1.deposer(300)
compteBanc1.afficher_solde()