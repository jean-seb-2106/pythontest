from comptebancaire import Compte #bonne pratique
#import comptebancaire as cb autre façon de faire

client1 = Compte(titulaire = "Jean",solde = 150)
#client2 = cb.Compte(titulaire, solde) #correspond à l'autre façon de faire
print(client1.titulaire)
print(client1.solde)
client1.affiche_solde()

client1.depot(100)
print(client1.solde)

client1.retrait(100)
print(client1.solde)

client1.retrait(1000)
client2 = Compte("René",1000)
client1.transfert(50, client2)
print(client2.solde)
