'''
    -une fonction pour lister les salles et les places dispo ->
            lire le dictionnaire des salles, afficher le nombre de place total (longueur du tableau),
            afficher le nombre de place libre (nombre de zéro dans le tableau)

    -une fonction de demande d'accès aux salles
    -une fonction pour quitter la file d'attente d'accès à une salle

    -une fonction pour quitter la salle
'''

import Plateforme_Centrale.database as db

def consulter_salles():
    description = dict(bienvenue="Liste des salles de jeux:")
    description['liste salle'] = list()
    for salle in db.salles:
        description['liste salle'].append(f"Nom: {salle}; Nombre de joueurs autorisés: {db.salles[salle][1]}; "
                                          f"Nombre de joueurs actuels: {len(db.salles[salle][0])}; "
                                          f"Joueurs présents dans la salle: {db.salles[salle][0]}")
    return description


def rejoindre_salle(nom, id):
    if len(db.salles[nom][0]) < db.salles[nom][1]:
        db.salles[nom][0].append(id)


def quitter_salle(nom, id):
    db.salles[nom][0].remove(id)


def consulter_joueurs():
    description = dict(bienvenue="Liste des joueurs connectés:")
    description['liste joueurs'] = list()
    for joueur in db.joueurs:
        description['liste joueurs'].append(f"ID: {joueur}; Pseudo: {db.joueurs[joueur]}")
    return description
