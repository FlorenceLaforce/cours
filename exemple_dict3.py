produits = {'Fraise': 2, 'Banane': 5, 'Pain': 3}
produit_prix = {prod: f"{prix}$" for prod, prix in produits.items()}
print(produit_prix)

#autre exemple
notes = {'math': 15, 'physics': 18, 'chemistry': 18, 'histoire': 10}
mentions={
    matiere: 'excellent' if note>=16
            else 'bien' if note>=14
            else 'moyen' if note>=12
            else 'passable'
    for matiere, note in notes.items()
}
print(mentions)