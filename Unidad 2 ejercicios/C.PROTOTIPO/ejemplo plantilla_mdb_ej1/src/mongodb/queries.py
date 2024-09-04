from datetime import datetime
from bson import ObjectId
from .init_db import get_database

db = get_database()

# Funciones para los autores
def add_author(name, biography):
    """Añade un nuevo autor a la colección de autores."""
    author = {"name": name, "biography": biography}
    return db.authors.insert_one(author).inserted_id

def get_author(author_id):
    """Recupera un autor por su ID."""
    return db.authors.find_one({"_id": ObjectId(author_id)})

# Funciones para las publicaciones
def create_post(title, content, author_id):
    """Crea una nueva publicación."""
    post = {
        "title": title,
        "content": content,
        "author_id": ObjectId(author_id),
        "publish_date": datetime.now(),
        "comments": []
    }
    return db.posts.insert_one(post).inserted_id

def add_comment(post_id, content, author_id):
    """Añade un comentario a una publicación existente."""
    comment = {
        "content": content,
        "author_id": ObjectId(author_id),
        "date": datetime.now()
    }
    db.posts.update_one({"_id": ObjectId(post_id)}, {"$push": {"comments": comment}})

def get_post(post_id):
    """Recupera una publicación por su ID, incluyendo detalles del autor y comentarios."""
    return db.posts.aggregate([
        {"$match": {"_id": ObjectId(post_id)}},
        {"$lookup": {
            "from": "authors",
            "localField": "author_id",
            "foreignField": "_id",
            "as": "author"
        }},
        {"$unwind": "$author"}
    ]).next()

# Funciones para eliminar datos (opcional)
def delete_post(post_id):
    """Elimina una publicación por su ID."""
    return db.posts.delete_one({"_id": ObjectId(post_id)})


# Significado de CRUD. {Create, Read, Update, Delete}.
# CRUD es un acrónimo que significa Crear, Leer, Actualizar y Eliminar.
# Estas son las operaciones básicas que se pueden realizar en cualquier 
# base de datos o sistema de almacenamiento de datos.