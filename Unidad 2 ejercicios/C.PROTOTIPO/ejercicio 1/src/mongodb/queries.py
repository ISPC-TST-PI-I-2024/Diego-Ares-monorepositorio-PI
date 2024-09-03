from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['blog']

# Crear una publicación nueva
def create_post(title, content, author_id):
    post = {
        'title': title,
        'content': content,
        'author_id': author_id,
        'date': datetime.now(),
        'comments': []
    }
    db.posts.insert_one(post)
    print("Post created successfully")

# Leer todas las publicaciones
def read_posts():
    for post in db.posts.find():
        print(post)

# Actualizar una publicación
def update_post(post_id, new_content):
    db.posts.update_one({'_id': post_id}, {'$set': {'content': new_content}})
    print("Post updated successfully")

# Borrar una publicación
def delete_post(post_id):
    db.posts.delete_one({'_id': post_id})
    print("Post deleted successfully")

# Añadir un comentario a una publicación
def add_comment(post_id, content, author_id):
    comment = {'content': content, 'author_id': author_id, 'date': datetime.now()}
    db.posts.update_one({'_id': post_id}, {'$push': {'comments': comment}})
    print("Comment added successfully")