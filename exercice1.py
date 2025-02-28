# Je demande a l'utilisateur d'enter le montant total des achats
montant = float(input("Entrez le montant montant de vos achats : "))

# Si le montant total des achats est superieur à 100€, je calcule la reduction de 10%
if montant > 100:
    reduction = montant * 0.1
    payable = montant - reduction
    print(f"Vous bénéficiez d'une remise de 10%. Montant à payer : {payable}€")
else:
    print(f"Pas de remise. Montant à payer : {montant}€")

