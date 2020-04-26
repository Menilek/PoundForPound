from pymongo import MongoClient

db_uri = 'mongodb://127.0.0.1/test-fantasy-fighter'
client = MongoClient(db_uri)

db = client['fantasy-fighter'] #select db
fighters = db['fighters'] #select collection

seed_fighters = [
    {"grappling":"Jiu Jitsu","name":"Menilek","striking":"Boxing"},
    {"grappling":"Judo","name":"Ryu","striking":"Karate"},
    {"grappling":"Aikido","name":"The Experiment","striking":"Boxing"},
    {"grappling":"Aikido","name":"Killer","striking":"Boxing"},
    {"grappling":"Aikido","name":"fighter","striking":"Boxing"},
    {"grappling":"Aikido","name":"SPARTAN","striking":"Boxing"},
    {"grappling":"Aikido","name":"RELOOOOAAAD","striking":"Boxing"},
    {"grappling":"Aikido","name":"AJ","striking":"Boxing"},
    {"grappling":"Aikido","name":"Kazuya","striking":"Boxing"},
    {"grappling":"Jiu Jitsu","name":"hassan","striking":"Muay Thai"},
    {"grappling":"Aikido","name":"mollee","striking":"Boxing"},
    {"grappling":"Aikido","name":"Najmi","striking":"Boxing"},
    {"grappling":"Aikido","name":"yula","striking":"Boxing"},
    {"grappling":"Aikido","name":"Bodgkin McHufflepuster","striking":"Karate"},
    {"grappling":"Judo","name":"Ogun","striking":"Muay Thai"},
    {"grappling":"Jiu Jitsu","name":"j","striking":"Karate"},
    {"grappling":"Jiu Jitsu","name":"test","striking":"Karate"},
    {"grappling":"Jiu Jitsu","name":"Gob","striking":"Karate"},
    {"grappling":"Judo","name":"Tommy","striking":"Muay Thai"},
    {"grappling":"Aikido","name":"411","striking":"Boxing"},
    {"grappling":"Aikido","name":"Paul","striking":"Boxing"},
    {"grappling":"Jiu Jitsu","name":"Kev","striking":"Muay Thai"},
    {"grappling":"Judo","name":"Paul","striking":"Karate"},
    {"grappling":"Judo","name":"Craig","striking":"Karate"},
    {"grappling":"Jiu Jitsu","name":"Barry","striking":"Muay Thai"},
    {"grappling":"Jiu Jitsu","name":"Craig","striking":"Karate"},
    {"grappling":"Jiu Jitsu","name":"Balrog","striking":"Boxing"},
    {"grappling":"Jiu Jitsu","name":"Genesyd","striking":"Muay Thai"},
    {"grappling":"Aikido","name":"Kickao","striking":"Karate"},
    {"grappling":"Aikido","name":"Yabsra","striking":"Boxing"},
    {"grappling":"Judo","name":"Alex","striking":"Karate"},
    {"grappling":"Aikido","name":"Alex","striking":"Boxing"}
    ]

seed_data = fighters.insert_many(seed_fighters)
print(seed_data.inserted_ids)

# fighters.drop()