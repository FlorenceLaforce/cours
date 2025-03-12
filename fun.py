titre: str = "BIENVENUE"
question : str = "quelle est votre nom?"
presentation : str = "Bonjour à toi "
exclame : str = " !"
question2 : str  = "Quelle âge as-tu? "
non : str = "Impossible de rentrer puisque tu es mineur."
oui : str = "YESS! tu peux entrer."
question3 : str = "Quelle est ta couleur préférer? "
bonne_couleur : str = "Wow quelle belle couleur!"
mauvaise_couleur : str = "Wash! Tu ne peux pas continuer."
question4 : str = "Quelle est ton animal préférer? "
animal_cool : str = "C'est mon animal préférer aussi. YOUPI!"
animal_nul : str = "Décevant..."
amis : str = "Nous pouvons maintenant être ami!"

print(f">{titre:~^51}<")

nom = input(f">{question:^51}<")

print(f">{presentation+nom+exclame:.^51}<")


def main():
    age()
    details()
    ami()

def age():
    age = int(input(f">{question2:^51}<"))
    if age < 18:
        print(f">{non:^51}<")
        exit()
    if age >= 18:
        print(f">{oui:^51}<")

def details():
    couleur = input(f">{question3:^51}<")
    if couleur == "rouge" or couleur == "bleu" or couleur == "rose":
        print(f">{bonne_couleur:^51}<")
    else:
        print(f">{mauvaise_couleur:^51}<")
        exit()

    animal = input(f">{question4:^51}<")
    if animal == "cheval" or animal == "chat":
        print(f">{animal_cool:^51}<")
    else:
        print(f">{animal_nul:^51}<")
        exit()

def ami():
    exit(f">{amis:^51}<")




if __name__ == "__main__":
    main()