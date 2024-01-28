# app.py
import random
from flask import Flask, jsonify
from flask_cors import CORS
from ben_10 import get_alien_by_name, get_random_alien

app = Flask(__name__)
CORS(app)

@app.route('/aliens/<string:alien_name>', methods=['GET'])
  
def get_alien(alien_name):
    if alien_name.lower() == 'random':
        alien_data = get_random_alien()
    else:
        alien_data = get_alien_by_name(alien_name)

    if alien_data:
        return jsonify(alien_data)
    else:
        return jsonify({"error": "Alien not found"}), 404
      
@app.route('/aliens', methods=['GET'])
def get_random_alien_route():
    random_alien = get_random_alien()
    return jsonify(random_alien)


if __name__ == '__main__':
    app.run(debug=True)
