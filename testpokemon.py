from pokemon import pokemon
from dresseur import dresseur

perso1 = pokemon("pikachu", 50, 80, 2) #création d'une instance
perso2 = pokemon("bulbizzard", 100, 50, 20) #autre instance

#Test exercice 1
print(perso1.nom) #affichage de l'attribut

perso1.statut()

#Test exercice 2

perso1.attaque(perso2)
print(perso2.vie)

dresseur1 = dresseur(Nom = "Indiana") #création d'une instance
print(dresseur1.listepokemon)
print(dresseur1.Nom)

dresseur1.capture(perso1)
dresseur1.capture(perso2)
print(dresseur1.listepokemon[0].statut()) #afficher le statut du premier pokemon capturé par le dresseur 1

def combat(perso1,perso2):
    while(perso1.vie > 0 | perso2.vie > 0):
        perso1.vie = perso1.vie - perso2.degats
        perso2.vie = perso2.vie - perso1.degats
    if perso1.vie > perso2.vie:
        print(perso1.statut[0]+" a gagné")