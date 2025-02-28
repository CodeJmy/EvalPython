# Fonction pour vérifier le mot de passe
def verifier_mot_de_passe(mot_de_passe):
    # Je fais une condition pour vérifier si le mot de passe contient au moins 8 caractères
    # Je vérifie avec any() si la chaîne contient au moins un chiffre (0-9) en utilisant une expression lambda (chiffre.isdigit())
    # Si les deux conditions sont remplies, le mot de passe est valide
    # Sinon, le mot de passe est invalide
    if len(mot_de_passe) >= 8 and any(chiffre.isdigit() for chiffre in mot_de_passe):  
        print("Mot de passe valide")
    else:
        print("Mot de passe invalide (doit contenir au moins 8 caractères et un chiffre)")

# Demande à l'utilisateur d'entrer un mot de passe
mot_de_passe = input("Entrer un mot de passe :")

# Appelle la fonction avec le mot de passe entré par l'utilisateur
verifier_mot_de_passe(mot_de_passe)