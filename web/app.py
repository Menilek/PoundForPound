from flask import Flask, render_template, request
from flask_paginate import Pagination, get_page_parameter, get_page_args
from pymongo import MongoClient
import os
from api import api
from seed import checkDBCollection

app = Flask(__name__)
app.register_blueprint(api, url_prefix="/api")

if os.environ.get('prod'):
    db_uri = os.environ.get('DATABASE_URI')
    client = MongoClient(db_uri)
else:
    # db_uri = 'mongodb://127.0.0.1/test-fantasy-fighter'
    client = MongoClient("mongodb://my_db:27017")

db = client['fantasy-fighter'] #select db 

#Set env to development, debug mode to True and seed db
if not os.environ.get('prod'):
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = 'True'
    fighters = db['fighters']
    checkDBCollection()

title = 'Top Fighters'

@app.route('/', methods=['GET'])
def fighters():
    search = False
    page, per_page, offset = get_page_args()
    fighters = db['fighters'] #select collection
    heading = 'POUND FOR POUND'
    fighter_list = fighters.find({},{"_id": 0, "name": 1, "striking": 1, "grappling": 1}).skip((page - 1)*per_page).limit(per_page)
    pagination = Pagination(page=page, per_page=10, offset=offset, total=fighter_list.count(), search=search, record_name='fighters')
    return render_template('index.html',fighters=fighter_list, t=title, h=heading, pagination=pagination)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)