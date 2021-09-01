from pymongo import MongoClient
import os

mongo_host = os.environ.get("MONGO_HOST", "localhost")
mongo_port = 27017
# Création d'un client mongo
client = MongoClient(host=mongo_host, port=mongo_port)
# Récupération de la base de données demo
database = client.demo

utilisateur_collection = database.utilisateur
utilisateur_collection.delete_many({})

def afficher():
    utilisateurs = utilisateur_collection.find()
    for ut in utilisateurs:
        print(f'Nom: {ut["nom"]}; Prenom:{ ut["prenom"]}, Voitures:{ut["voitures"]}')
    input()
    start()

def ajouter_utilisateur():
    prenom = input("Entrez un Prenom: ").lower()
    nom    = input("Entrez un Nom   : ").upper()
    utilisateur = {
        "prenom":prenom, 
        "nom":nom, 
        "voitures":ajouter_voitures() }
    utilisateur_collection.insert_one(utilisateur)
    input()
    start()

def ajouter_voitures():
    voitures = []
    while input("Voulez vous ajouter une voiture?") in ["y", "Y", "Yes", "yes"]:
        marque = input("marque:")
        model =  input("model :")
        voitures.append({"marque":marque, "model":model})
    return voitures

def chercher():
    key = input("Entrez le nom de la propriété a chercher")
    value = input("Entrez la valeur")
    res = utilisateur_collection.find({key:value})
    for u in res:
        print(u)
    input()
    start()

def start():
    print("Que voulez vous faire?")
    print(" 1: Ajouter un utilisateur")
    print(" 2: Afficher la liste des utilisateur")
    print(" 3: Chercher")
    print(" 4: Quitter")
    res = input("?:")
    if (res == "1"):
        ajouter_utilisateur()
    elif (res == "2"):
        afficher()
    elif( res == "3"):
        chercher()
    elif (res == "4"):
        return
    else:
        print("Pardon????")
        start()  
start()