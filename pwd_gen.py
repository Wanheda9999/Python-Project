import random
import string

password_types = {
    'maj': string.ascii_uppercase,
    'min': string.ascii_lowercase,
    'special': string.punctuation,
    'maj/min': string.ascii_letters,
    'maj/special': string.ascii_uppercase + string.punctuation,
    'min/special': string.ascii_lowercase + string.punctuation,
    'all': string.ascii_uppercase + string.ascii_lowercase + string.punctuation
}

def randompwd(password_len, characters):
    password = ''.join(random.choice(characters) for i in range(password_len))
    return password

while True:
    try:
        password_len = int(input("Saisissez la taille de votre mot de passe (entre 8 et 16) : "))
        if 8 <= password_len <= 16:
            break
        else:
            print("La taille requise n'est pas correcte.")
    except ValueError:
        print("Veuillez saisir un nombre entier.")

while True:
        password_type = input("Choisissez comment doit être composé votre mot de passe (maj/min/special/all) : ")
        if password_type in password_types:
            break
        else:
            print("Type de mot de passe invalide.")

characters = password_types[password_type]
generated_password = randompwd(password_len, characters)
print("Mot de passe généré :", generated_password)
