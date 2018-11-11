from flask import Flask, jsonify
from flask_basicauth import BasicAuth

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'user'
app.config['BASIC_AUTH_PASSWORD'] = 'password'
app.config['BASIC_AUTH_FORCE'] = True
basic_auth = BasicAuth(app)

actors = [
    {'id': 1, 'actor': 'William Shatner', 'role': 'James T'},
    {'id': 2, 'actor': 'Leonard Nimoy', 'role': 'Spock'},
    {'id': 3, 'actor': 'DeForest Kelley', 'role': 'Leonard McCoy'},
    {'id': 4, 'actor': 'James Doohan', 'role': 'Montgomery Scott'},
    {'id': 5, 'actor': 'George Takei', 'role': 'Hikaru Sulu'},
    {'id': 6, 'actor': 'Walter Koenig', 'role': 'Pavel Chekov'},
    {'id': 7, 'actor': 'Nichelle Nichols', 'role': 'Nyota Uhura'},
    {'id': 8, 'actor': 'Majel Barrett', 'role': 'Christine Chapel'}
]

@app.route('/actors', methods=['GET'])
def get_persons():
    return jsonify(actors), 200

@app.route('/actors/<int:id>', methods=['GET'])
def get_actor_by_id(id: int):
    found = None
    for actor in actors:
        if actor['id'] == id:
            found = actor
            break

    if found:
        return jsonify(found), 200
    else:
        return '', 404


app.run(debug=True, host="0.0.0.0", port=5000)
