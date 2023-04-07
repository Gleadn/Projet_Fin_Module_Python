'''
    - ajouter une salle
    - supprimer une salle
'''

import Plateforme_Centrale.database as db


def ajoutSalle(places):
    nom = 'salle' + str(len(db.salles))
    nbr_place = [0] * places
    db.salles[nom] = nbr_place
    print(db.salles)
    print(f"La salle '{nom}' de {places} places a été créé et ajouté à la liste.")


def supprimerSalle(nom):
    del db.salles[nom]
    print(db.salles)
    print(f"La salle '{nom}' a été supprimé de la liste.")


def supprimerSalleVide():
    for salle in db.salles:
        if tableauVide(salle):
            supprimerSalle(salle)


def tableauVide(nom):
    for value in db.salles[nom]:
        if value != 0:
            return False
    return True
