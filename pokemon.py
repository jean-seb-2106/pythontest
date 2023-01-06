class pokemon:
    def __init__(self,nom,vie,degats,niveau):
        self.nom = nom
        self.vie = vie
        self.degats = degats
        self.niveau = niveau

a = pokemon("pikachu",50,80,2) #création d'une instance
print(a.nom) #affichage de l'attribut