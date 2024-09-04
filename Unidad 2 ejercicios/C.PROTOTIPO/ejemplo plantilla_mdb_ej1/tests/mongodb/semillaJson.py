from faker import Faker
import json
import random

fake = Faker()

def generate_authors(num_authors):
    authors = []
    for _ in range(num_authors):
        author = {
            "_id": str(fake.unique.random_int(min=1)),
            "name": fake.name(),
            "biography": fake.text()
        }
        authors.append(author)
    return authors

def generate_posts_and_embedded_comments(num_posts, num_authors, num_comments_per_post):
    posts = []
    author_ids = [str(i) for i in range(1, num_authors + 1)]

    for i in range(1, num_posts + 1):
        comments = []
        for _ in range(num_comments_per_post):
            comment = {
                "content": fake.sentence(),
                "author_id": random.choice(author_ids),
                "date": fake.date_time_this_year().isoformat()
            }
            comments.append(comment)

        post = {
            "_id": str(i),
            "title": fake.sentence(),
            "content": fake.text(),
            "author_id": random.choice(author_ids),
            "publish_date": fake.date_time_this_year().isoformat(),
            "comments": comments
        }
        posts.append(post)

    return posts

def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

# Configuración
num_authors = 10  # Total de autores
num_posts = 50   # Total de publicaciones
num_comments_per_post = 3  # Comentarios por publicación

# Generar datos
authors_list = generate_authors(num_authors)
posts_list = generate_posts_and_embedded_comments(num_posts, num_authors, num_comments_per_post)

# Guardar en archivos JSON
save_json(authors_list, 'tests/json/autores.json')
save_json(posts_list, 'tests/json/publicaciones.json')