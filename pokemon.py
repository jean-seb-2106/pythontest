class pokemon:
    def __init__(self,nom,vie,degats,niveau):
        self.nom = nom
        self.vie = vie
        self.degats = degats
        self.niveau = niveau
    
    def statut(self):
        print(self.nom + " ", str(self.vie) + " " + str(self.degats) + " " + str(self.niveau) )

    def attaque(self,perso):
        perso.vie = perso.vie - self.degats

