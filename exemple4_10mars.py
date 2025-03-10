class employe:
    def __init__(self, id, nom, poste):
        self.id = id
        self.nom = nom
        self.poste = poste

    def afficher_info(self):
        return f"employer: {self.nom}, ID: {self.id}, poste: {self.poste}"

class departement:
    def __init__(self, nom, localisation):
        self.nom = nom
        self.localisation = localisation
        self.employe = []

    def ajouter_employe(self, employe):
        self.employe.append(employe)

    def afficher_employes(self):
        return [emp.nom for emp in self.employe]

emp1 = employe(1, "Martin", "developpeur")
emp2 = employe(2, "bernard", "designer")

dept_tech = departement("technologie", "batiment A")
dept_tech.ajouter_employe(emp1)
dept_tech.ajouter_employe(emp2)

print(dept_tech.afficher_employes())

#si le departement est suprimé, les employes existent toujours
del dept_tech
print(emp1.afficher_info())