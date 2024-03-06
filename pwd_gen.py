import random
import string


def randompwd(password_len):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(password_len))
    return password


password_len = int(input("Saisissez la taille de votre mot de passe (entre 8 et 16) : "))
if password_len < 8 or password_len > 16:
    print("La taille requise n'est pas correcte.")
else:
    generated_password = randompwd(password_len)
    print("Mot de passe généré :", generated_password)
