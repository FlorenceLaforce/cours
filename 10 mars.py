#Surcharge d'operateur

class vecteur:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,autre):
        """surcharge de l'operateur"""
        return vecteur(self.x+autre.x,self.y+autre.y)

    def __sub__(self,autre):
        """surcharge de l'operateur'"""
        return vecteur(self.x-autre.x,self.y-autre.y)

    def __mul__(self,scalaire):
        """surcharge de l'operateur'"""
        return vecteur(self.x*scalaire,self.y*scalaire)

    def __str__(self):
        return f"vecteur ({self.x}, {self.y})"

v1 = vecteur(1,2)
v2 = vecteur(3,4)
print(v1 + v2)
print(v1 - v2)
print(v1 * 3)