import random


# 'nom_salle' = [0,0,0,0,0,0,0,0,0,0]
# 'nom_salle' = ['id_user'], max
salles = {}


def creer_salles(range_len, min_salles, max_salles, min_participants, max_participants):
    nb_salles = random.randint(min_salles, max_salles)  # Génère un nombre aléatoire de salles entre min_salles et max_salles
    for i in range(nb_salles):
        nb_max = random.randint(min_participants, max_participants) // 5 * 5  # Génère un nombre maximum de participants multiple de 5 entre min_participants et max_participants
        nom_salle = f"salle_{i + range_len}"  # Génère un nom de salle avec un identifiant unique
        salles[nom_salle] = [[], nb_max]  # Initialise la liste des utilisateurs dans la salle à vide
    return salles


# 'pseudo' = ID
joueurs = {}


def generate_pseudo(range_len):
    # Générer des pseudonymes aléatoires pour les joueurs
    noms = ["dragon", "licorne", "sorcier", "magicien", "elfe", "gobelin", "nain", "ogre", "géant", "centaure", "fée", "lutin", "vampire", "loup-garou", "zombie", "fantôme", "squelette", "momie", "monstre", "démon", "ange", "humain", "robot", "alien", "extraterrestre", "mutant", "super-héros", "ninja", "pirate", "cow-boy", "indien", "chevalier", "princesse", "roi", "reine", "peintre", "écrivain", "musicien", "chanteur", "acteur", "athlète", "scientifique", "astronaute", "médecin", "pompier", "policier", "chef", "jardinier", "vendeur", "étudiant", "professeur"]
    adjectifs = ["volant", "invisible", "puissant", "mystique", "ténébreux", "lumineux", "courageux", "maléfique", "héroïque", "sage", "joyeux", "triste", "fou", "énervé", "calme", "timide", "sérieux", "drôle", "créatif", "intelligent", "fort", "faible", "rapide", " lent", "grand", "petit", "mince", "gros", "jeune", "vieux", "beau", "moche", "clair", "obscur", "chaud", "froid", "dur", "mou", "sec", "humide", "sale", "propre", "parfumé", "malodorant", "bruyant", "silencieux", "occupé", "libre", "riche", "pauvre", "célèbre", "inconnu", "heureux", "malheureux", "confiant", "hésitant", "bavard", "taciturne", "doux", "dur", "sucré", "salé", "amer", "acide", "épicé", "amer", "réaliste", "idéaliste", "réfléchi", "impulsif", "curieux", "indifférent", "passionné", "détaché", "gentil", "méchant", "charmant", "froid", "délicat", "grossier", "patient", "impatient", "digne", "indigne", "radin", "généreux", "prudent", "téméraire"]

    pseudos = [random.choice(noms) + "_" + random.choice(adjectifs) + str(i) for i in range(1 + range_len, 101 + range_len)]

    # Générer des identifiants uniques pour chaque joueur
    ids = list(range(1 + range_len, 101 + range_len))

    # Créer le dictionnaire de joueurs
    joueurs = {pseudo: id for pseudo, id in zip(pseudos, ids)}

    return joueurs
