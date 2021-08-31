# Neo4j avec Python

## Exercice 1:
1. Lancer le docker compose.
2. Attendre un peu (Neo4j est assez long a se lancer)
3. Dans un navigateur Web:
```URL
http://localhost:7474/browser/
```
4. Pour se connécter:
    * Utilisateur: `neo4j`
    * Mot de passe: `neo4j`
5. Changer le mot de passe
6. Bravo vous etes connécté a neo4j.

## Exercice 2:
1. Pour ajouter une valeur:
```Neo4J
CREATE (unLabel:TRUC { nom: "Toto", prenom: "Truc", age: 18 })
```
Vous avez ajouter la valeur "unLabel" de type UNTRUC avec les propriétés:
* nom: Toto
* prenom: Truc
* age: 18
2. Pour récupéré une valeur:
```Neo4j
MATCH ( result:UNTYPE ) 
RETURN result
```
Vous récupérez une valeur de type UNTYPE
3. Pour récupéré une valeur en filtrant:
```Neo4j
MATCH ( result:UNTYPE ) 
WHERE result.prenom = "Machin"
RETURN result
```
4. Vous pouvez ajouter plusieur nodes et les lier entre elles:
```Neo4j
MATCH (p1:UNTYPE) WHERE p1.prenom = "Truc"
CREATE (p2:UNTYPE { nom: "Toto", prenom: "Bidule"}),
(p1)-[:LIEN]->(p2)
```
Vous avez selectionné une node de type UNTYPE portant le prenom `Truc` et le sauvegarder dans la variable `p1`, créer une autre node `p2` et créer un lien entre les deux `LIEN`.
5. Vous pouvez récupéré l'ensemble des nodes lié avec une certaine avec le lien `LIEN`:
```Neo4j
MATCH (p1:UNTYPE)-[:LIEN]->(amis)
RETURN p1, amis
```