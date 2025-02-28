# Méthode avec une boucle et la fonction max()

# Je créer une liste vide
nombres = []

# Je demande à l'utilisateur de rentrer cinq nombres et je les ajoute à la liste vide nombre[]
for i in range(5):
    nombre = int(input(f"Entrez un nombre : "))
    nombres.append(nombre)

# Je cherche le plus grand nombre dans la liste nombres et je le stocke dans la variable plus_grand
plus_grand = max(nombres)

# Affichage
print(f"Le plus grand nombre est : {plus_grand}")