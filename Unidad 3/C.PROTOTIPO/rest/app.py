from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Esta línea permitirá las solicitudes de origen cruzado

posts = [
    {'id': 1, 'contenido': 'Mi primera publicación'},
    {'id': 2, 'contenido': 'Mi segunda publicación'}
]

@app.route('/blog', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/blog', methods=['POST'])
def add_post():
    new_post = {'id': request.json['id'], 'contenido': request.json['contenido']}
    posts.append(new_post)
    return jsonify(new_post), 201

@app.route('/blog/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if not post:
        return jsonify({'error': 'No se encontró la publicación'}), 404
    post[0]['contenido'] = request.json.get('contenido', post[0]['contenido'])
    return jsonify(post[0])

@app.route('/blog/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if not post:
        return jsonify({'error': 'No se encontró la publicación'}), 404
    posts.remove(post[0])
    return jsonify({'exito': 'Publicación eliminada correctamente'}), 200

if __name__ == '__main__':
    app.run(debug=True)


    