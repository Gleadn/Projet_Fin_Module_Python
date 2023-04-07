from flask import Flask, request
import User_Action.user as user
import User_Action.databaseJoueurs as dbj
import Plateforme_Centrale.databaseSalle as dbs


app = Flask(__name__)


#Route principale, page d'accueil avec explications des routes et intialisation des salles et joueurs
@app.route('/')
def home():
    dbs.salles = dbs.creer_salles(len(dbs.salles), 5, 10, 10, 30)
    dbj.joueurs = dbj.generate_pseudo(len(dbj.joueurs))
    text = dict(bienvenue='Bienvenue sur l\'API de notre site de salle de jeux!')
    text['liste route'] = list()
    text['liste route'].append('Route /afficher_salle -> lire le dictionnaire de salle + afficher info')
    text['liste route'].append('Route /afficher_joueurs -> lire le dictionnaire de joueurs')
    text['liste route'].append('Route /acces_salle -> rejoindre la salle indiqué. Les paramêtres sont: '
                               '?nom=nom_salle&id_user=id')
    text['liste route'].append('Route /quitter_salle -> enlever l\'ID du joueur de la salle.'
                               ' Les paramêtres sont: ?nom=nom_salle&id_user=id')
    text['liste route'].append('Route /ajouter_salle -> rajouter un certains nombre de salle')
    text['liste route'].append('Route /ajouter_joueurs -> ajouter 100 nouveaux joueurs')
    return text


#permet d'afficher toutes salles disponible
@app.route('/afficher_salle', methods=['GET', 'POST'])
def afficher_salle():
    result = user.consulter_salles()
    return result


#permet d'afficher tous les joueurs connectés
@app.route('/afficher_joueurs', methods=['GET', 'POST'])
def afficher_joueurs():
    result = user.consulter_joueurs()
    return result


#permet d'accèder à une salle à l'aide de ce nom et de l'id du joueur
@app.route('/acces_salle', methods=['GET', 'POST'])
def acces_salle():
    try:
        nom = str(request.args["nom"])
        id = int(request.args["id_user"])
    except:
        print("Bad request")
        return dict(error_msg="missing required fields 'nom' ou 'id_user'"), 400

    user.rejoindre_salle(nom, id)
    return f'Le joueur avec l\'id {id} a rejoint la {nom}. ' \
           f'Rendez vous sur la route \'/afficher_salle\' pour voir les changements'


#permet de quitter une salle à l'aide de ce nom et de l'id du joueur
@app.route('/quitter_salle', methods=['GET', 'POST'])
def quitter_salle():
    try:
        nom = str(request.args["nom"])
        id = int(request.args["id_user"])
    except:
        print("Bad request")
        return dict(error_msg="missing required fields 'nom' ou 'id_user'"), 400

    user.quitter_salle(nom, id)
    return f'Le joueur avec l\'id {id} a quitté la {nom}. ' \
           f'Rendez vous sur la route \'/afficher_salle\' pour voir les changements'


#permet d'ajouter des salles
@app.route('/ajouter_salle', methods=['GET', 'POST'])
def ajouter_salle():
    dbs.salles = dbs.creer_salles(len(dbs.salles), 5, 10, 10, 30)
    return "Des salles ont été ajouté. Rendez vous sur la route \'/afficher_salle\' pour voir les changements"


#permet d'ajouter des joueurs
@app.route('/ajouter_joueurs', methods=['GET', 'POST'])
def ajouter_joueurs():
    dbj.joueurs = dbj.generate_pseudo(len(dbj.joueurs))
    return "100 joueurs ont été ajouté. Rendez vous sur la route \'/afficher_joueurs\' pour voir les changements"
