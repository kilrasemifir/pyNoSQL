from flask import Flask, request
from pymongo import MongoClient
from bson import ObjectId
import os

app = Flask(__name__)

mongo_host = os.environ.get("MONGO_HOST", "localhost")
mongo_port = 27017
mongo_uri  = f'mongo://{mongo_host}:{mongo_port}'
# Création d'un client mongo
client = MongoClient(host=mongo_host, port=mongo_port)
# Récupération de la base de données demo
database = client.demo
# Récupération de la collection users
utilisateurs = database.utilisateurs

@app.route("/api/utilisateurs", methods=["POST"])
def ajouter_utilisateur():
    data = request.json
    utilisateurs.insert_one(data)
    data["_id"] = str(data["_id"])
    return data

@app.route("/api/utilisateurs", methods=["GET"])
def findAll():
    result = list(utilisateurs.find(dict(request.args)))
    for ut in result:
        ut["_id"] = str(ut["_id"])
    return {"result": result}

@app.route("/api/utilisateurs/<id>", methods=["GET"])
def find_by_id(id):
    result = utilisateurs.find_one({"_id": ObjectId(id)})
    result["_id"] = str(result["_id"])
    return result

@app.route("/api/utilisateurs/<id>", methods=["DELETE"])
def delete_by_id(id):
    utilisateurs.delete_one({"_id": ObjectId(id)})
    return "OK"

@app.route("/api/utilisateurs/<prop>/<value>", methods=["GET"])
def find_by_props(prop, value):
    result = list(utilisateurs.find({prop: value}))
    for ut in result:
        ut["_id"] = str(ut["_id"])
    return {"result": result}

app.run(host="0.0.0.0", port=9000, debug=True)