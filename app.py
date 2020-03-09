from flask import Flask, render_template, request, redirect, url_for
from bson import ObjectId
from pymongo import MongoClient
import os

app = Flask(__name__)
app.config.from_object('config')
client = MongoClient()
db = client['fantasy-fighter'] #select db
fighters = db['fighters'] #select collection

title = 'Top Fighters'

# fighters = [
#     {"name" : "Menilek", "striking" : "Boxing", "grappling" : "Jiu Jitsu"},
#     {"name" : "Venom", "striking" : "Kickboxing", "grappling" : "Jiu Jitsu"}
# ] <-- DUMMY DATA TO PLAY WITH

@app.route('/')
def fighters():
    heading = 'POUND FOR POUND'
    fighter_list = fighters.find()
    return render_template('index.html',fighters=fighter_list, t=title, h=heading)

if __name__ == '__main__':
    app.run(debug=True)