class etudiant:
    def __init__(self, id,  nom, prenom):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.cours = [] #listedes cours suivis par l'etudiant

    def ConsulterCours(self):
        return [cours.titre for cours in self.cours]

    def InscrireAuCours(self, cours):
        if cours not in self.cours:
            self.cours.append(cours)
            cours.ajouter_etudiant(self)

class cours:
    def __init__(self, code,  titre, credits):
        self.code = code
        self.titre = titre
        self.credits = credits
        self.etudiants = [] # liste etudiant inscrits

    def afficherDetails(self):
        return f"Cours: {self.titre}, Code: {self.code}, Credits: {self.credits}"

    def ajouter_etudiant(self, etudiant):
        if etudiant not in self.etudiants:
            self.etudiants.append(etudiant)

etudiant1 = etudiant(1, "Laforce", "Florence")
cours_python = cours(101, "structure de données en python", 3)
etudiant1.InscrireAuCours(cours_python)
print(etudiant1.ConsulterCours())