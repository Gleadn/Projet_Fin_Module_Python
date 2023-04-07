import Plateforme_Centrale.databaseSalle as dbs

#Ces fonctions ne sont pas utilisé car il n'y a pas de différence entre un user classique et un user admin

#permet d'ajouter une seule salle
def ajoutSalle(places):
    nom = 'salle' + str(len(dbs.salles))
    nbr_place = [0] * places
    dbs.salles[nom] = nbr_place
    print(dbs.salles)
    print(f"La salle '{nom}' de {places} places a été créé et ajouté à la liste.")


#permet de supprimer une seule salle
def supprimerSalle(nom):
    del dbs.salles[nom]
    print(dbs.salles)
    print(f"La salle '{nom}' a été supprimé de la liste.")

