from flask import Flask, render_template, request
from pymongo import MongoClient
import os
from api import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix="/api")

if os.environ.get('prod'):
    db_uri = os.environ.get('DATABASE_URI')
    client = MongoClient(db_uri)
else:
    db_uri = 'mongodb://127.0.0.1/test-fantasy-fighter'
    client = MongoClient(db_uri)

db = client['fantasy-fighter'] #select db 

if not os.environ.get('prod'):
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = 'True'

title = 'Top Fighters'

@app.route('/', methods=['GET'])
def fighters():
    fighters = db['fighters'] #select collection   
    heading = 'POUND FOR POUND'
    fighter_list = fighters.find({},{"_id": 0, "name": 1, "striking": 1, "grappling": 1})
    return render_template('index.html',fighters=fighter_list, t=title, h=heading)

if __name__ == '__main__':
    app.run()