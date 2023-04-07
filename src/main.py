from flask import Flask, request
import User_Action.user as user
import Plateforme_Centrale.database as db

app = Flask(__name__)


@app.route('/')
def home():
    db.salles = db.creer_salles(len(db.salles), 5, 10, 10, 30)
    db.joueurs = db.generate_pseudo(len(db.joueurs))
    return 'Bienvenue sur l\'API de notre site de salle de jeux!'


@app.route('/afficher_salle', methods=['GET', 'POST'])
def afficher_salle():
    result = user.consulter_salles()
    return result


@app.route('/afficher_joueurs', methods=['GET', 'POST'])
def afficher_joueurs():
    result = user.consulter_joueurs()
    return result


@app.route('/acces_salle', methods=['GET', 'POST'])
def acces_salle():
    try:
        nom = str(request.args["nom"])
        id = int(request.args["id_user"])
    except:
        print("Bad request")
        return dict(error_msg="missing required fields 'nom' ou 'id_user'"), 400

    user.rejoindre_salle(nom, id)
    return f'Vous avez rejoint la {nom}'


@app.route('/quitter_salle', methods=['GET', 'POST'])
def quitter_salle():
    try:
        nom = str(request.args["nom"])
        id = int(request.args["id_user"])
    except:
        print("Bad request")
        return dict(error_msg="missing required fields 'nom' ou 'id_user'"), 400

    user.quitter_salle(nom, id)
    return f'Vous avez quitter la {nom}'


@app.route('/ajouter_salle', methods=['GET', 'POST'])
def ajouter_salle():
    db.salles = db.creer_salles(len(db.salles), 5, 10, 10, 30)
    return "Des salles ont été ajouté. Rendez vous sur la route \'/afficher_salle\' pour voir les changements"


@app.route('/ajouter_joueurs', methods=['GET', 'POST'])
def ajouter_joueurs():
    db.joueurs = db.generate_pseudo(len(db.joueurs))
    return "100 joueurs ont été ajouté. Rendez vous sur la route \'/afficher_joueurs\' pour voir les changements"
