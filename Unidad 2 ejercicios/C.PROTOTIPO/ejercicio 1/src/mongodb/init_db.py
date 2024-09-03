from pymongo import MongoClient
from datetime import datetime

def init_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['blog']

    # Crear colecciones y documentos iniciales
    authors = db['authors']
    author_id = authors.insert_one({'name': 'John Doe', 'biography': 'Writer'}).inserted_id

    posts = db['posts']
    post_id = posts.insert_one({
        'title': 'Welcome to My Blog',
        'content': 'This is the first post.',
        'author_id': author_id,
        'date': datetime.now(),
        'comments': [
            {'content': 'Great post!', 'author_id': author_id, 'date': datetime.now()}
        ]
    }).inserted_id

    print("Database initialized with sample data")

if __name__ == "__main__":
    init_db()