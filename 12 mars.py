def somme(*args):
    """Somme un nombre variable d'arguments"""
    total = 0
    for arg in args:
        total += arg
    return total

print(somme(1, 2, 3, 4))
print(somme(5, 10))