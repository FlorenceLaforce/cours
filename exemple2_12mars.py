def afficher_infos(**kwargs):
    """Affiche des informations à partir de parametres nommés"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(afficher_infos(nom="Florence", age=17, ville="candiac"))

