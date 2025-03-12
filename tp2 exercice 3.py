from datetime import date

class Etudiant:
    def __init__(self, id, nom, notes, annee_nais=2009):
        self.__id = id
        self.nom = nom
        self.__notes = []
        if notes:
            for note in notes:
                self.set_notes(note)
        self.annee_nais = annee_nais

    @property
    def get_nom(self):
        return self.__nom

    @get_nom.setter
    def set_nom(self, nom):
        if nom.strip():  # Vérifie que le nom n'est pas vide
            self.__nom = nom
        else:
            raise ValueError("Le nom ne peut pas être vide.")

    @property
    def get_notes(self):
        return self.__notes

    def set_notes(self, note):
        if 0 <= note <= 20:
            self.__notes.append(note)
        else:
            raise ValueError("Les notes doivent être comprises entre 0 et 20.")

    @property
    def get_annee_nais(self):
        return self.__annee_nais

    @get_annee_nais.setter
    def set_annee_nais(self, annee):
        annee_actuelle = date.today().year
        if 0 < annee <= annee_actuelle:
            self.__annee_nais = annee
        else:
            self.__annee_nais = 2009  # Valeur par défaut en cas d'année invalide

    def get_moyenne(self):
        if self.__notes:
            return sum(self.__notes) / len(self.__notes)
        return 0  # Retourne 0 si aucune note n'est enregistrée

    def get_age(self):
        annee_actuelle = date.today().year
        return annee_actuelle - self.__annee_nais

# Exemple d'utilisation
etudiant = Etudiant(id=1, nom="Jean Dupont", notes=[15, 18, 12], annee_nais=2005)
print(f"Nom: {etudiant.get_nom}")
print(f"Notes: {etudiant.get_notes}")
print(f"Moyenne: {etudiant.get_moyenne()}")
print(f"Âge: {etudiant.get_age()}")
