# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

model_path = "/home/joaojunior/project2-pv2/model.pickle"

print("Carregando o modelo...")
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    songs = data.get("songs", [])
    recommendations = [song for song in model['rules'] if song not in songs][:10]

    response = {
        "model_date": os.path.getmtime(model_path),
        "songs": recommendations,
        "version": "1.0"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
