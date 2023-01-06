class dresseur:

    def __init__(self,Nom):
        self.Nom = Nom
        self.listepokemon = []
    
    def capture(self,perso):
        self.listepokemon.append(perso)