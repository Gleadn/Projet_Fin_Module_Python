import random


# 'nom_salle' = [0,0,0,0,0,0,0,0,0,0]
# 'nom_salle' = ['id_user'], max
salles = {}

def creer_salles(min_salles, max_salles, min_participants, max_participants):
    nb_salles = random.randint(min_salles,
                               max_salles)  # Génère un nombre aléatoire de salles entre min_salles et max_salles
    salles = {}
    for i in range(nb_salles):
        nb_max = random.randint(min_participants, max_participants) // 5 * 5  # Génère un nombre maximum de participants multiple de 5 entre min_participants et max_participants
        nom_salle = f"salle_{i}"  # Génère un nom de salle avec un identifiant unique
        salles[nom_salle] = [[], nb_max]  # Initialise la liste des utilisateurs dans la salle à vide
    return salles


# 'pseudo' = ID
joueurs = {}
