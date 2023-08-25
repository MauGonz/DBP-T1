from flask import Flask, request, jsonify

app = Flask(__name__)

animes = [
    {
        "id": 1,
        "titulo": "One Punch Man",
        "puntaje": 10,
        "tipo": "Serie",
        "season": "1",
        "generos": ["Accion", "Aventura", "Comedia"]
    },
    {
        "id": 2,
        "titulo": "Hunter X Hunter",
        "puntaje": 10,
        "tipo": "Serie",
        "season": "2",
        "generos": ["Shonen", "Accion", "Aventura"]
    },
    {
        "id": 3,
        "titulo": "Dr. Stone",
        "puntaje": 10,
        "tipo": "Serie",
        "season": "1",
        "generos": ["Accion", "Aventura", "Ciencia ficcion"]
    }
]

# GET
@app.route('/anime', methods=['GET'])
def get_anime():
    return jsonify({'anime': animes})

# GET id
@app.route('/anime/<int:anime_id>', methods=['GET'])
def get_anime_id(anime_id):
    anime_= next((anime for anime in animes if anime['id'] == anime_id), None)
    if anime_ is None:
        return jsonify({'error': 'Anime not found'}), 404
    return jsonify({'anime':anime_})

# POST
@app.route('/anime', methods=['POST'])
def add_anime():
    new_anime = request.json
    if any(anime['id'] == new_anime['id'] for anime in animes):
        return jsonify({'error': 'Anime already exist'}), 400
    animes.append(new_anime)
    return jsonify({'message': 'Anime correctly created'}), 201

# PUT id
@app.route('/anime/<int:anime_id>', methods=['PUT'])
def update_anime(anime_id):
    anime_ = next((anime for anime in animes if anime['id'] == anime_id), None)
    if anime_ is None:
        return jsonify({'error': 'Anime not found'}), 404
    
    update_data = request.json
    anime_.update(update_data)

    return jsonify({'message': 'Anime correctly updated', 'anime': anime_})

# PATCH id
@app.route('/anime/<int:anime_id>', methods=['PATCH'])
def partial_update_anime(anime_id):
    anime_ = next((anime for anime in animes if anime['id'] == anime_id), None)
    if anime_ is None:
        return jsonify({'error': 'Anime not found'}), 404
    
    update_data = request.json
    anime_.update(update_data)

    return jsonify({'message': 'Anime correctly updated', 'anime': anime_})

# DELETE id
@app.route('/anime/<int:anime_id>', methods=['DELETE'])
def delete_anime(anime_id):
    anime_ = next((anime for anime in animes if anime['id']== anime_id), None)
    if anime_ is None:
        return jsonify({'error': 'Anime not found'}), 404
    animes.remove(anime_)
    return jsonify({'message': 'Anime coorectly eliminated'})

if __name__ == '__main__':
    app.run(debug=True)