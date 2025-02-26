mon_dictionnaire = {}
mon_dictionnaire['num_téléphone'] = 2807
mon_dictionnaire['année_naissance'] = 2025
print(mon_dictionnaire)
ancien_numero = mon_dictionnaire.pop('num_téléphone')

for cle, valeur in mon_dictionnaire.items():
    print(f"L'attribut {cle} a pour valeur: {valeur}")

operation ={
    'addition': lambda x, y: x + y,
    'difference': lambda x, y: x - y,
    'multiplication': lambda x, y: x * y,
    'double': lambda x: x * 2,
}
print(operation['double'](2))

#Autre exemple
cube = {a: a**3 for a in range(1,10)}
print(cube)
carre_pairs = {a: a**2 for a in range(5) if a % 2 == 0}
print(carre_pairs)
carre_divi_trois = {a: a**2 for a in range(11) if a % 2 == 0}
print(carre_divi_trois)