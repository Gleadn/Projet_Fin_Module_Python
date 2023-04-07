import Plateforme_Centrale.databaseSalle as dbs
import User_Action.databaseJoueurs as dbj


#lit le dictionnaire de salle
def consulter_salles():
    description = dict(bienvenue="Liste des salles de jeux:")
    description['liste salle'] = list()
    for salle in dbs.salles:
        description['liste salle'].append(f"Nom: {salle}; Nombre de joueurs autorisés: {dbs.salles[salle][1]}; "
                                          f"Nombre de joueurs actuels: {len(dbs.salles[salle][0])}; "
                                          f"Joueurs présents dans la salle: {dbs.salles[salle][0]}")
    return description


#lit le dictionnaire des joueurs
def consulter_joueurs():
    description = dict(bienvenue="Liste des joueurs connectés:")
    description['liste joueurs'] = list()
    for joueur in dbj.joueurs:
        description['liste joueurs'].append(f"ID: {joueur}; Pseudo: {dbj.joueurs[joueur]}")

    return description


#ajoute l'id du user dans le tableau de la salle correspondante
def rejoindre_salle(nom, id):
    if len(dbs.salles[nom][0]) < dbs.salles[nom][1]:
        dbs.salles[nom][0].append(id)


#enlève l'id du user dans le tableau de la salle correspondante
def quitter_salle(nom, id):
    dbs.salles[nom][0].remove(id)
