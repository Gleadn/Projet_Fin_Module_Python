import requests, random


def simunlation_init(url):
    response = requests.get(url + '/')
    if response.status_code == 200:
        print("Salles et joueurs initialisés")
    else:
        print("Erreur lors de l'initialisation")


def simulation_afficher_salles(url):
    global salles
    afficher_salle_route = '/afficher_salle'
    response = requests.get(url + afficher_salle_route)
    if response.status_code == 200:
        salles = response.json()
        print('Salles créées :')
        for salle in salles['liste salle']:
            print(salle)
    else:
        print('Erreur lors de la récupération des salles :', response.text)
    return salles


def simulation_afficher_joueurs(url):
    global joueurs
    afficher_joueurs_route = '/afficher_joueurs'
    response = requests.get(url + afficher_joueurs_route)
    if response.status_code == 200:
        joueurs = response.json()
        print('Liste des joueurs :')
        for joueur in joueurs:
            print(joueur, joueurs[joueur])
    else:
        print('Erreur lors de la tentative d\'afficher les joueurs :', response.text)
    return joueurs


def simulation_rejoindre_salle(url, nom_salle, id_joueur):
    acces_salle_route = '/acces_salle'
    params = f"?nom={nom_salle}&id_user={id_joueur}"
    response = requests.get(url + acces_salle_route + params)
    if response.status_code == 200:
        print('Le joueur avec l\'ID', id_joueur, 'a rejoint la', nom_salle + '.')
    else:
        print('Erreur lors de la tentative de rejoindre la salle :', response.text)


def simulation_quitter_salle(url, nom_salle, id_joueur):
    quitter_salle_route = '/quitter_salle'
    params = f"?nom={nom_salle}&id_user={id_joueur}"
    response = requests.get(url + quitter_salle_route + params)
    if response.status_code == 200:
        print('Le joueur avec l\'ID', id_joueur, 'a été enlevé de la', nom_salle + '.')
    else:
        print('Erreur lors de la tentative de quitter la salle :', response.text)


if __name__ == '__main__':
    url = 'http://localhost:5000'
    simunlation_init(url)
    dbsalles = simulation_afficher_salles(url)
    dbjoueurs = simulation_afficher_joueurs(url)
    nbr_joueur = len(dbjoueurs['liste joueurs'])
    nbr_salle = len(dbsalles['liste salle'])
    liste_joueurs_dans_salle = list()
    liste_salle_occupee = list()

    #permet de placer 20 joueurs tiré au hasard dans une salle tirée au hasard
    for _ in range(20):
        id_salle = random.randint(0, nbr_salle -1)
        nom_salle = 'salle_' + str(id_salle)
        id_joueur = random.randint(1, nbr_joueur)
        liste_joueurs_dans_salle.append(id_joueur)
        liste_salle_occupee.append(nom_salle)
        simulation_rejoindre_salle(url, nom_salle, id_joueur)

    #permet de retirer 5 joueurs de la salle dans laquelle il se trouve
    for i in range(5):
        nom_salle = liste_salle_occupee[i]
        id_joueur = liste_joueurs_dans_salle[i]
        simulation_quitter_salle(url, nom_salle, id_joueur)
