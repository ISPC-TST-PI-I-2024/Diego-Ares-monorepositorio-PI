import json
import random
from mongodb.queries import create_post, add_comment, get_post, add_author

def load_data_from_json(file_path):
    """Carga datos desde un archivo JSON."""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def main():
    # Cargar datos de autores y publicaciones
    authors = load_data_from_json('tests/json/autores.json')
    posts = load_data_from_json('tests/json/publicaciones.json')

    # Seleccionar un autor aleatorio y una publicación aleatoria
    random_author = random.choice(authors)
    random_post = random.choice(posts)

    # Añadir un autor
    author_id = add_author(random_author['name'], random_author['biography'])
    
    # Crear una nueva publicación usando datos aleatorios de publicación y el nuevo autor_id
    post_id = create_post(random_post['title'], random_post['content'], author_id)
    
    # Añadir un comentario a la publicación recién creada
    add_comment(post_id, "Este es un comentario muy interesante.", author_id)
    
    # # Recuperar y mostrar los detalles de la publicación
    # post = get_post(post_id)
    # print(post)

if __name__ == "__main__":
    main()
