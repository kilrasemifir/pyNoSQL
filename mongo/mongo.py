from pymongo import MongoClient

mongo_host = "localhost"
mongo_port = 27017
# Création d'un client mongo
client = MongoClient(host=mongo_host, port=mongo_port)
# Récupération de la base de données demo
database = client.demo
# Récupération de la collection users
users = database.users
# Récupération d'un utilisateur avec le champs "name" portant la valeur "toto"
print(users.find_one({"name":"toto"}))
# Insertion d'une nouvelle valeur
users.insert_one({"name":"truc bidule", "voitures":[
    {"marque":"Tesla"}
]})
# Récupération du nombre d'utilisateur avec une voiture portant la marque Tesla
print(users.find({"voitures.marque":"Tesla"}).count())
# Récupération de tout les utilisateurs avec une voiture portant la marque Tesla
for user in users.find({"voitures.marque":"Tesla"}):
    print(user)