#combinaison des 2 types (*arg et **kwards)
def creer_profile(nom, prenom, *competence,**details):
    profile = {
        "nom": nom,
        "prenom": prenom,
        "competence": competence,
        **details
    }
    return profile

profil = creer_profile(
    "laforce", "florence", "ski",
    "à bromont", age=17, email="florence.laforce@icloud.com"
)
print(profil)