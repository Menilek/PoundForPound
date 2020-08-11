from flask import Blueprint, jsonify, request
from pymongo import MongoClient
import os

if os.environ.get('prod'):
    db_uri = os.environ.get('DATABASE_URI')
    client = MongoClient(db_uri)
else:
    db_uri = 'mongodb://127.0.0.1/test-fantasy-fighter'
    client = MongoClient(db_uri)
    # client = MongoClient("mongodb://my_db:27017")

db = client['fantasy-fighter'] #select db
fighters = db['fighters'] #select collection

api = Blueprint("api", __name__)

@api.route('/', methods=['GET'])
def fighter_list():
    fighter_list = []
    for f in fighters.find({},{"_id": 0, "name": 1, "striking": 1, "grappling": 1}):
        fighter_list.append({'name': f['name'], 'striking': f['striking'], 'grappling': f['grappling']})
    return jsonify({'fighters' : fighter_list})

@api.route('/grappling/<style>', methods=['GET'])
def grappler_list(style):
    query = {"grappling" : style}
    fighter_list = []
    for f in fighters.find(query):
        fighter_list.append({'name': f['name'], 'striking': f['striking'], 'grappling': f['grappling']})
    return jsonify({'grapplers' : fighter_list})

@api.route('/striking/<style>', methods=['GET'])
def striking_list(style):
    query = {"striking" : style}
    fighter_list = []
    for f in fighters.find(query):
        fighter_list.append({'name': f['name'], 'striking': f['striking'], 'grappling': f['grappling']})
    return jsonify({'strikers' : fighter_list})