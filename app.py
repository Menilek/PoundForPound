from flask import Flask, render_template
from bson import ObjectId #CURRENTLY NOT USED
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object('instance.config.Config')
client = MongoClient(app.config['DATABASE_URI'])
print(client)

title = 'Top Fighters'

@app.route('/')
def fighters():
    db = client['fantasy-fighter'] #select db
    fighters = db['fighters'] #select collection
    heading = 'POUND FOR POUND'
    fighter_list = fighters.find({},{"_id": 0, "name": 1, "striking": 1, "grappling": 1})
    return render_template('index.html',fighters=fighter_list, t=title, h=heading)

if __name__ == '__main__':
    app.run(debug=True)