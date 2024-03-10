import json
import os

fichier_contacts = "contacts.json"


def charger_contacts():
    if os.path.exists(fichier_contacts):
        with open(fichier_contacts, 'r') as f:
            return json.load(f)
    else:
        # Si le fichier n'existe pas, retourne un dictionnaire vide
        return {}


# Fonction pour sauvegarder les contacts dans le fichier
def sauvegarder_contacts(contacts):
    with open(fichier_contacts, 'w') as f:
        json.dump(contacts, f)


# Charger les contacts existants ou créer un nouveau dictionnaire
contacts = charger_contacts()

print("Bienvenue sur votre gestionnaire de contact")

while True:
    print("Si vous souhaitez ajouter un contact, tapez 1")
    print("Si vous souhaitez supprimer un contact, tapez 2")
    print("Si vous souhaitez voir vos contact, tapez 3")
    print("Si vous souhaitez quitter, tapez q")
    user_choice = input("")

    if user_choice == '1':
        name = input("Veuillez rentrer le nom du contact: ")
        number = input("Veuillez rentrer le numéro du contact: ")
        email = input("Veuillez rentrer l'email du contact: ")
        contacts[name] = {'number': number, 'email': email}
        print("Contact ajouté avec succès!")

    if user_choice == '2':
        print("Saissiez le nom du contact a supprimer")
        name = input("")
        del contacts[name]
        print(" ", name, " à été supprimé")

    if user_choice == '3':
        print(contacts)


    elif user_choice.lower() == 'q':
        # Sauvegarder les contacts et quitter
        sauvegarder_contacts(contacts)
        print("Contacts enregistrés. Au revoir!")
        break

