from flask import Flask, render_template, jsonify, request
from bson import ObjectId #CURRENTLY NOT USED
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object('instance.config.Config')
client = MongoClient(app.config['DATABASE_URI'])
db = client['fantasy-fighter'] #select db

title = 'Top Fighters'

@app.route('/')
def fighters():
    fighters = db['fighters'] #select collection
    heading = 'POUND FOR POUND'
    fighter_list = fighters.find({},{"_id": 0, "name": 1, "striking": 1, "grappling": 1})
    return render_template('index.html',fighters=fighter_list, t=title, h=heading)

@app.route('/fighter-list/all', methods=['GET'])
def json_fighter_list():
    fighters = db['fighters'] #select collection
    fighter_list = []
    for f in fighters.find({},{"_id": 0, "name": 1, "striking": 1, "grappling": 1}):
        fighter_list.append({'name': f['name'], 'striking': f['striking'], 'grappling': f['grappling']})
    return jsonify({'fighters' : fighter_list}) 

if __name__ == '__main__':
    app.run(debug=True)