from pymongo import MongoClient

def test_connection():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client['blog']
        # Intentamos obtener una lista de colecciones para probar la conexión
        collections = db.list_collection_names()
        if 'posts' in collections:
            print("Connection to the 'blog' database successful.")
        else:
            print("Connection successful but 'posts' collection does not exist.")
    except Exception as e:
        print("Failed to connect to MongoDB:", e)

if __name__ == "__main__":
    test_connection()