import pymongo
import sqlite3

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Connect to SQLite database
conn = sqlite3.connect('pokemon.sqlite')
cursor = conn.cursor()

# Retrieve data from SQLite database
cursor.execute("SELECT * FROM pokemon")
rows = cursor.fetchall()

# Convert each row to a dictionary and insert into MongoDB
for row in rows:
    doc = {
        "name": row[0],
        "type1": row[1],
        "type2": row[2],
        "total": row[3],
        "hp": row[4],
        "attack": row[5],
        "defense": row[6],
        "spatk": row[7],
        "spdef": row[8],
        "speed": row[9],
        "generation": row[10],
        "legendary": row[11],
    }
    collection.insert_one(doc)

# Close connections
cursor.close()
conn.close()
client.close()
