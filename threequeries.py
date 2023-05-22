import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['pokemondb']
collection = db['pokemonk_data']

# Query 1: Return all the Pokemon named "Pikachu"
result = collection.find({'name': 'Pikachu'})
print('All the Pokemon named "Pikachu":')
for pokemon in result:
    print(pokemon)

# Query 2: Return all the Pokemon with an attack greater than 150
result = collection.find({'attack': {'$gt': 150}})
print('All the Pokemon with an attack greater than 150:')
for pokemon in result:
    print(pokemon)

# Query 3: Return all the Pokemon with an ability of "Overgrow"
result = collection.find({'abilities':{'$regex':"Overgrow"}})
print('All the Pokemon with an ability of "Overgrow":')
for pokemon in result:
    print(pokemon)