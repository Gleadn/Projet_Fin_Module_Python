'''
    -une fonction pour lister les salles et les places dispo ->
            lire le dictionnaire des salles, afficher le nombre de place total (longueur du tableau),
            afficher le nombre de place libre (nombre de zéro dans le tableau)

    -une fonction de demande d'accès aux salles
    -une fonction pour quitter la file d'attente d'accès à une salle

    -une fonction pour quitter la salle
'''

def consulter_salles(salles):
    """
    Cette fonction prend en entrée une liste de salles de jeux et affiche les informations sur chaque salle:
    - Le nom de la salle
    - Le nombre de joueurs autorisés
    - Le nombre de joueurs actuels
    - L'état de la salle (ouverte/fermée)
    """

    
    print("Liste des salles de jeux:\n")
    for salle in salles:
        print(f"Nom: {salle.nom}")
        print(f"Nombre de joueurs autorisés: {salle.nb_max_joueurs}")
        print(f"Nombre de joueurs actuels: {len(salle.joueurs)}")
        if salle.etat == "ouvert":
            print("Etat: Ouverte\n")
        else:
            print("Etat: Fermée\n")

consulter_salles()
