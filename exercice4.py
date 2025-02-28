# Création de la class Livre            
class Livre:
    # Constructeur de la classe Livre
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        
# Création de la class LivreEmpruntable
class LivreEmpruntable(Livre):
    # Constructeur de la classe LivreEmpruntable qui hérite de Livre
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur)
        self.disponibilite = True
        
    # Fonction emprunter 
    def emprunter(self):
        if self.disponibilite:
            self.disponibilite = False
            print(f"Le livre a été emprunté.")
    # Fonction retourner
    def retourner(self):
        if not self.disponibilite:
            self.disponibilite = True
            print(f"Le livre a été retourné.")
    
    # Méthode spécifique à LivreEmpruntable
    def __str__(self):
        return f"Titre : {self.titre}, Auteur : {self.auteur}, Disponibilité : {'Disponible' if self.disponibilite else 'Indisponible'}"


# Test
livre1 = LivreEmpruntable("1984", "George Orwell")
print(livre1)
livre2 = LivreEmpruntable("Le Petit Prince", "Antoine Saint Exupery")
print(livre2)
livre2.emprunter()
print(livre2)
livre2.retourner()
print(livre2)
