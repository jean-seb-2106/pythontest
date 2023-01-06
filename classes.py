class Personne:

    def __init__(self, nom, prenom, age):
        self.nom=nom # attribut nom
        self.prenom=prenom # attribut prenom
        self.age=age # attribut age


moi=Personne("Eneman","Donatien",26) #moi est une instance de la classe Personne
print(moi.nom) #¨pour acceder a l'attribut nom
