# import pymongo and sqlite3
from pymongo import MongoClient
# connect to the local MongoDB instance
client = MongoClient()


mongoClient =
MongoClient("mongodb://localhost/pokemon")
pokemonDB =
mongoClient['pokemondb']
pokemonColl =
pokemonDB['pokemon_data']



with open('pokemon.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        document = {
            "name": row['name'],
            "pokedex_number": int(row['pokedex_number']),
            "types": row['types'].split(","),
            "hp": int(row['hp']),
            "attack": int(row['attack']),
            "defense": int(row['defense']),
            "speed": int(row['speed']),
            "sp_attack": int(row['sp_attack']),
            "sp_defense": int(row['sp_defense']),
            "abilities": row['abilities'].split(",")
        }
        pokemonColl.insert_one(document)


#retrieve the data
import sqlite3
conn = sqlite3.connect('path/to/database')
c = conn.cursor()
c.execute('SELECT name, pokedex_number, type1, type2, hp, attack, defense, speed, sp_attack, sp_defense, ability1, ability2 FROM pokemon WHERE name = ?', ('Pikachu',))
results = c.fetchone()
conn.close()


# Connect to the SQLite database
conn = sqlite3.connect('pokemon.sqlite')
cur = conn.cursor()

# Connect to the MongoDB database
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Loop over each Pokemon in the database
for pokemon in pokemonColl.find():
    # Query the SQLite database to retrieve this Pokemon's abilities
    cur.execute("""
        SELECT a.identifier
        FROM pokemon_abilities pa
        JOIN abilities a ON pa.ability_id = a.id
        WHERE pa.pokemon_id = ?;
    """, (pokemon['pokedex_number'],))
    abilities = [row[0] for row in cur.fetchall()]

    # Update the Pokemon document in the MongoDB collection
    pokemonColl.update_one(
        {"_id": pokemon['_id']},
        {"$set": {"abilities": abilities}}
    )


# Query to return all the Pokemon named "Pikachu"
pikachu_query = {"name": "Pikachu"}
pikachu_results = pokemon_coll.find(pikachu_query)
for result in pikachu_results:
    print(result)

# Query to return all the Pokemon with an attack greater than 150
high_attack_query = {"attack": {"$gt": 150}}
high_attack_results = pokemon_coll.find(high_attack_query)
for result in high_attack_results:
    print(result)

# Query to return all the Pokemon with an ability of "Overgrow"
overgrow_query = {"abilities": {"$in": ["Overgrow"]}}
overgrow_results = pokemon_coll.find(overgrow_query)
for result in overgrow_results:
    print(result)



