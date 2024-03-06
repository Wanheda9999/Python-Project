email = input("Veuillez entrer un email: ")
slice_mail = email.split('@')
if slice_mail[1] != "gmail.com" and slice_mail[1] != "hotmail.fr":
    print("Adresse du mail : ", slice_mail[0])
    print("Nom de domaine incorrect, veuillez renseignez une adresse mail google")
else:
    print("Adresse mail :", slice_mail[0], "\nNom de domaine du mail :", slice_mail[1])
