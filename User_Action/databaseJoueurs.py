import random

# génération des joueurs avec un pseudo et un id
# 'pseudo' = ID
joueurs = {}


def generate_pseudo(range_len):
    noms = ["dragon", "licorne", "sorcier", "magicien", "elfe", "gobelin", "nain", "ogre", "géant", "centaure", "fée",
            "lutin", "vampire", "loup-garou", "zombie", "fantôme", "squelette", "momie", "monstre", "démon", "ange",
            "humain", "robot", "alien", "extraterrestre", "mutant", "super-héros", "ninja", "pirate", "cow-boy",
            "indien", "chevalier", "princesse", "roi", "reine", "peintre", "écrivain", "musicien", "chanteur", "acteur",
            "athlète", "scientifique", "astronaute", "médecin", "pompier", "policier", "chef", "jardinier", "vendeur",
            "étudiant", "professeur"]
    adjectifs = ["volant", "invisible", "puissant", "mystique", "ténébreux", "lumineux", "courageux", "maléfique",
                 "héroïque", "sage", "joyeux", "triste", "fou", "énervé", "calme", "timide", "sérieux", "drôle",
                 "créatif", "intelligent", "fort", "faible", "rapide", " lent", "grand", "petit", "mince", "gros",
                 "jeune", "vieux", "beau", "moche", "clair", "obscur", "chaud", "froid", "dur", "mou", "sec", "humide",
                 "sale", "propre", "parfumé", "malodorant", "bruyant", "silencieux", "occupé", "libre", "riche",
                 "pauvre", "célèbre", "inconnu", "heureux", "malheureux", "confiant", "hésitant", "bavard", "taciturne",
                 "doux", "dur", "sucré", "salé", "amer", "acide", "épicé", "amer", "réaliste", "idéaliste", "réfléchi",
                 "impulsif", "curieux", "indifférent", "passionné", "détaché", "gentil", "méchant", "charmant", "froid",
                 "délicat", "grossier", "patient", "impatient", "digne", "indigne", "radin", "généreux", "prudent",
                 "téméraire"]

    for i in range(1 + range_len, 101 + range_len):
        pseudo = random.choice(noms) + "_" + random.choice(adjectifs) + str(i)
        id = i
        joueurs[id] = [pseudo]

    return joueurs
