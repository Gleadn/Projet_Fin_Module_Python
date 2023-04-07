from flask import Flask, request
import User_Action.user as user
import Plateforme_Centrale.database as db

app = Flask(__name__)


@app.route('/')
def home():
    db.salles = db.creer_salles(5, 10, 10, 30)
    return 'Bienvenue sur l\'API de notre site de salle de jeux!'


@app.route('/afficher_salle', methods=['GET', 'POST'])
def afficher_salle():
    result = user.consulter_salles()
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
    except:
        print("Bad request")
        return dict(error_msg="missing required field 'nom'"), 400

    user.quitter_salle(nom)
    return f'Vous avez quitter la {nom}'
