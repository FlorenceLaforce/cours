#Question 1
import math
class vecteur:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        return vecteur(self.x+other.x,self.y+other.y,self.z+other.z)

    def __sub__(self,other):
        return vecteur(self.x-other.x,self.y-other.y,self.z-other.z)

    def __mul__(self,other):
        return vecteur(self.x*other.x,self.y*other.y,self.z*other.z)

    def __eq__(self,other):
        return self.x==other.x and self.y==other.y and self.z==other.z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def calcul_norme(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2), 2)

v1 = vecteur(1, 2, 3)
v2 = vecteur(4, 5, 6)

print(f"Somme de v1 et v2 : {v1 + v2}")
print(f"Différence de v1 et v2 : {v1 - v2}")
print(f"Multiplication de v1 et v2 : {v1 * v2}")
print(f"Est ce que v1 est égal à v2 : {v1 == v2}")
print(f"La norme de v1 est {v1.calcul_norme()}")
print(f"La norme de v2 est {v2.calcul_norme()}")