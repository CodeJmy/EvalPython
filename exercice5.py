# Fonction retirer()
def retirer():
    while True:
        # Je demande à l'utilisateur de saisir le montant à retirer
        montant = int(input("Entrez le montant à retirer : "))
        # Je fais ma condition pour que le montant doit être un multiple de 10
        if montant % 10 != 0:
            print("Le montant doit être un multiple de 10.")
        # Vérification du montant qui ne doit pas dépasser les 500€
        elif montant > 500:
            print("Le montant ne peut pas dépasser 500€.")
        
        # Vérification du montant pour 50€
        billets_50 = montant // 50
        montant -= billets_50 * 50
        
        # Vérification du montant pour 20€
        billets_20 = montant // 20
        montant -= billets_20 * 20
        
        # Vérification du montant pour 10€
        billets_10 = montant // 10
        montant -= billets_10 * 10
        # Affichage du nombre de billets distribués
        print(f"Billets distribués : - {billets_50} billets de 50€ - {billets_20} billets de 20€ - {billets_10} billets de 10€")
    

# Utilisation de la fonction retirer()

retirer()