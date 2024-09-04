from pymongo import MongoClient

def get_database():
    """Conecta con la base de datos y retorna una referencia a la base de datos."""
    client = MongoClient("mongodb://localhost:27017/")
    return client["blog_system"]

# Si deseas probar la conexión directamente
if __name__ == "__main__":
    db = get_database()
    print("Conectado a la base de datos:", db.name)

