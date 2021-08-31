# Redis en Python.

## Exerice 1:
1. Créer un docker compose avec un service `redis` qui utilise l'image `redis` et qui ouvre le port `6379`. 
2. Lancer le docker compose.
3. Ouvrir un terminal dans le conteneur (avec VSCode ou avec une commande docker)
4. taper la commande `redis-cli`
5. Ajouter une valeur a redis avec la commande `SET`:
```redis
SET macle mavaleur
```
6. Récupérer la valeur de la clé `macle`avec la commande `GET macle`
7. Bravo... Vous savez faire du redis en ligne de commande.

## Exercice 2:
Il existe plusieur client redis en Python. Pour cette exercice nous allons utiliser le client `aioredis`.
1. dans un terminal: `pip install redis`
2. dans un terminal ajouter la dependance redis: `pip install redis`
3. dans un fichier python, créer une instance de client redis:
```python
from redis import Redis
client = Redis(host="localhost", port="6379")
```
4. pour ajouter une valeur:
```python
client.set("unecle", "ma super valeur de la mort")
```
5. recupération d'une valeur:
```python
result = client.get("uncle")
print(result)
```
6. bravo vous faite maintenant du redis en python.
