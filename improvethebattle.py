import random
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemonk_data']

def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number":pokemonid})

def attack(attacker, defender):
    # Calculate the damage done by the attacker
    damage = attacker['attack'] - defender['defense']
    if damage < 1:
        damage = 1

    # Subtract the damage from the defender's HP
    defender['hp'] -= damage

    # Check if the defender has fainted
    if defender['hp'] <= 0:
        return True
    else:
        return False

def battle(pokemon1, pokemon2):
    print("Let the Pokemon battle begin! ================")
    print("It's " + pokemon1['name'] + " vs " + pokemon2['name'])

    # Determine which Pokemon goes first based on speed
    if pokemon1['speed'] > pokemon2['speed']:
        first_pokemon = pokemon1
        second_pokemon = pokemon2
    elif pokemon2['speed'] > pokemon1['speed']:
        first_pokemon = pokemon2
        second_pokemon = pokemon1
    else:
        # If the speeds are equal, choose randomly
        first_pokemon = random.choice([pokemon1, pokemon2])
        second_pokemon = pokemon2 if first_pokemon == pokemon1 else pokemon1

    # Loop until one Pokemon faints
    while True:
        # First Pokemon attacks
        print(first_pokemon['name'] + " attacks " + second_pokemon['name'])
        if attack(first_pokemon, second_pokemon):
            print(second_pokemon['name'] + " has fainted!")
            print(first_pokemon['name'] + " wins the battle!")
            break

        # Second Pokemon attacks
        print(second_pokemon['name'] + " attacks " + first_pokemon['name'])
        if attack(second_pokemon, first_pokemon):
            print(first_pokemon['name'] + " has fainted!")
            print(second_pokemon['name'] + " wins the battle!")
            break

def main():
    # Fetch two pokemon from the MongoDB database
    pokemon1 = fetch(random.randrange(1, 802))
    pokemon2 = fetch(random.randrange(1, 802))

    # Pit them against one another
    battle(pokemon1, pokemon2)

main()
