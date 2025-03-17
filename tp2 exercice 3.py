from datetime import datetime

class etudiant:
    def __init__(self, id,  nom, notes, annee_nais):
        self.__id = id
        self.__nom = nom if nom else "inconnu"
        self.__notes = [note for note in (notes or []) if 0 <= note <= 20]
        self.__annee_nais = annee_nais if (0 <= annee_nais <= datetime.now().year) else 2009

    def get_nom(self, nom):
        return self.__nom

    def set_nom(self, nom):
        if nom:
            self.__nom = nom

    def get_notes(self):
        return self.__notes

    def set_notes(self, notes):
        self.__notes = [note for note in notes if 0 <= note <= 20]

    def ajouter_notes(self, note):
        if 0 <= note <= 20:
            self.__notes.append(note)

    def get_annee_nais(self):
        return self.__annee_nais

    def set_annee_nais(self, annee_nais):
        if 0 <= annee_nais <= datetime.now().year:
            self.__annee_nais = annee_nais
        else:
            self.__annee_nais = 2009

    def get_moyenne(self):
        return sum(self.__notes)/len(self.__notes) if self.__notes else 0

    def get_age(self):
        return datetime.now().year - self.__annee_nais

    def afficher(self):
        print(f"ID: {self.__id}, Nom: {self.__nom}, Annee de naissance: {self.__annee_nais}")
        print(f"Notes: {self.__notes}")
        print(f"Moyenne: {self.get_moyenne():.2f}, Age: {self.get_age()}")

#exemple test
etudiants = [
    etudiant(1, "Charle", [15, 13, 18], 2005),
    etudiant(2, "Juan", [15, 10, 12], 2006),
    etudiant(3, "Florence", [19, 18, 19], 2007),
    etudiant(4, "", [15, 13, 18], -20) #exemple qui marche pas
]

etudiants[0].afficher()
etudiants[1].afficher()
etudiants[2].afficher()




