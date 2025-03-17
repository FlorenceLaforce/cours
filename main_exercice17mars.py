from 17_mars.py import Rectangle

def creer_rectangle():
    """Définir la fonction pour créer un rectangle"""
    while True:
        try:
            largeur = float(input("Entrez la largeur svp: "))
            if largeur < 0:
                print("La largueur doit être positive")
                continue
            break
        except ValueError:
            print("Veuillez entrez un nombre valide")

    while True:
        try:
            longueur = float(input("Entrez la largeur svp: "))
            if longueur < 0:
                print("La largueur doit être positive")
                continue
            break
        except ValueError:
            print("Veuillez entrez un nombre valide")

    return Rectangle(largeur, longueur)

    def afficher_aire(largeur, longueur):
