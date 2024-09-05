# Desarrollo de APIs RESTful con Flask
## Introducción a Flask
Flask es un microframework de Python para el desarrollo de aplicaciones web, desarrollado por Armin Ronacher como parte del proyecto Pocoo. A diferencia de otros frameworks más grandes como Django, Flask se caracteriza por ser ligero y modular, permitiendo a los desarrolladores escoger las extensiones y bibliotecas que necesiten para su proyecto. Esta flexibilidad lo convierte en una opción popular para desarrollar aplicaciones web de tamaño pequeño a mediano.

## Aplicaciones de Flask
**Desarrollo de APIs:** Flask es ideal para crear APIs RESTful debido a su simplicidad y capacidad para manejar solicitudes HTTP de manera eficiente.  

**Prototipos Rápidos:** Gracias a su naturaleza ligera, Flask es excelente para crear prototipos rápidos y pruebas de concepto.  

**Aplicaciones Web Complejas:** Aunque es ligero, Flask puede ser escalado para soportar aplicaciones web complejas mediante el uso de diversas extensiones.  

**Microservicios:** Su modularidad y facilidad de integración lo hacen una elección perfecta para construir microservicios.  

## Estructura del Módulo Flask
A continuación, se presenta una explicación de los componentes principales del módulo Flask y cómo se utilizan.

- Flask Class: La clase principal que se utiliza para crear la aplicación web.
```python
from flask import Flask
app = Flask(__name__)  
```

- Routing: Define las rutas (endpoints) de la aplicación utilizando decoradores.
```python
@app.route('/')
def home():
    return "Hello, Flask!"
```

- Templates: Flask utiliza Jinja2 como motor de plantillas para renderizar HTML.
```python
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')
```

- Static Files: Manejo de archivos estáticos como CSS, JavaScript e imágenes.

```html
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
```

- Request and Response: Manipulación de solicitudes y respuestas HTTP.
```python
from flask import request, jsonify

@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.get_json()
    return jsonify(data)
```

## Extensiones de Flask
Flask, al ser un microframework, puede ser extendido con diversas bibliotecas y extensiones para añadir funcionalidades adicionales. A continuación, se describen algunas de las extensiones más populares:

1. Flask-SQLAlchemy: Facilita la integración con bases de datos utilizando SQLAlchemy.

**Instalación:**

```bash
pip install Flask-SQLAlchemy
```

**Configuración:**  
```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
```

2. Flask-Migrate: Permite la migración de bases de datos utilizando Alembic.

**Instalación:**
```bash
pip install Flask-Migrate
```

**Configuración:**  
```python
from flask_migrate import Migrate

migrate = Migrate(app, db)
```

3. Flask-WTF: Proporciona herramientas para el manejo de formularios web utilizando WTForms.

**Instalación:**  
```bash
pip install Flask-WTF
```

**Configuración:**  
```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
```

4. Flask-Login: Manejo de autenticación de usuarios.

**Instalación:**  
```bash
pip install Flask-Login
```

**Configuración:**  
```python
from flask_login import LoginManager

login_manager = LoginManager(app)
login_manager.login_view = 'login'
Flask-Mail: Facilita el envío de correos electrónicos.
```

**Instalación:**  
```bash
pip install Flask-Mail
```

**Configuración:**  
```python
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-password'
mail = Mail(app)

@app.route('/send-email')
def send_email():
    msg = Message('Hello', sender='your-email@example.com', recipients=['to@example.com'])
    msg.body = 'This is a test email'
    mail.send(msg)
    return 'Email sent'
```  

## Ejemplos de Desarrollo de APIs RESTful con Flask
### Crear la Base de Datos
Primero, necesitamos crear la base de datos y las tablas necesarias para nuestra aplicación IoT. Utilizaremos MySQL para esto. Ejecuta el siguiente script SQL para crear la base de datos y las tablas:

```sql
-- Crear base de datos
CREATE DATABASE IF NOT EXISTS iot_project;
USE iot_project;

-- Crear tabla Usuarios
CREATE TABLE IF NOT EXISTS Usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    rol VARCHAR(50) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear tabla Dispositivos
CREATE TABLE IF NOT EXISTS Dispositivos (
    id_dispositivo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    ubicacion VARCHAR(100),
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Crear tabla Datos_Dispositivos
CREATE TABLE IF NOT EXISTS Datos_Dispositivos (
    id_dato INT AUTO_INCREMENT PRIMARY KEY,
    id_dispositivo INT,
    fecha_recoleccion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valor FLOAT,
    unidad VARCHAR(20),
    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivos(id_dispositivo)
);

-- Crear tabla Seguridad
CREATE TABLE IF NOT EXISTS Seguridad (
    id_seguridad INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_dispositivo INT,
    permisos VARCHAR(50),
    fecha_asignacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivos(id_dispositivo)
);

-- Crear tabla Proyectos
CREATE TABLE IF NOT EXISTS Proyectos (
    id_proyecto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    id_usuario INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Crear tabla Configuraciones
CREATE TABLE IF NOT EXISTS Configuraciones (
    id_configuracion INT AUTO_INCREMENT PRIMARY KEY,
    id_dispositivo INT,
    parametro VARCHAR(50),
    valor VARCHAR(100),
    fecha_asignacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivos(id_dispositivo)
);
```
#### 1. API Básica
Objetivo: Crear un endpoint simple que responda con un mensaje.

Código:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return {'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run(debug=True)
```

**Explicación:**

Flask Class: Importamos Flask y creamos una instancia de la clase Flask.

```python
from flask import Flask
app = Flask(__name__)
```

Routing: Definimos una ruta (endpoint) utilizando el decorador @app.route. Este endpoint responde a las solicitudes GET con un mensaje.

```python
@app.route('/api/hello', methods=['GET'])
def hello_world():
    return {'message': 'Hello, World!'}
```

Run Server: Iniciamos el servidor en modo debug.

```python
if __name__ == '__main__':
    app.run(debug=True)
```

#### 2. API con CRUD en Memoria
Objetivo: Crear una API que realice operaciones CRUD (Crear, Leer, Actualizar, Borrar) en una lista de elementos en memoria.

Código:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

items = []

@app.route('/api/items', methods=['POST'])
def create_item():
    item = request.json
    items.append(item)
    return jsonify(item), 201

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = request.json
    items[item_id] = item
    return jsonify(item)

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = items.pop(item_id)
    return jsonify(item)

if __name__ == '__main__':
    app.run(debug=True)
```

**Explicación:**  

Crear y Leer Elementos:

```python
@app.route('/api/items', methods=['POST'])
def create_item():
    item = request.json
    items.append(item)
    return jsonify(item), 201

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)
```

Actualizar y Borrar Elementos:

```python
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = request.json
    items[item_id] = item
    return jsonify(item)

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = items.pop(item_id)
    return jsonify(item)
```

Run Server: Iniciamos el servidor en modo debug.

```python
if __name__ == '__main__':
    app.run(debug=True)
```

#### 3. API con Base de Datos MySQL
Objetivo: Crear una API que realice operaciones CRUD utilizando una base de datos MySQL.

Configuración de Flask-SQLAlchemy:

Instalación:

```bash
pip install Flask-SQLAlchemy
```
Configuración:

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/iot_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())

class Dispositivo(db.Model):
    id_dispositivo = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    ubicacion = db.Column(db.String(100))
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))

class DatoDispositivo(db.Model):
    id_dato = db.Column(db.Integer, primary_key=True)
    id_dispositivo = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'))
    fecha_recoleccion = db.Column(db.DateTime, default=db.func.current_timestamp())
    valor = db.Column(db.Float)
    unidad = db.Column(db.String(20))

class Seguridad(db.Model):
    id_seguridad = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    id_dispositivo = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'))
    permisos = db.Column(db.String(50))
    fecha_asignacion = db.Column(db.DateTime, default=db.func.current_timestamp())

class Proyecto(db.Model):
    id_proyecto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)

class Configuracion(db.Model):
    id_configuracion = db.Column(db.Integer, primary_key=True)
    id_dispositivo = db.Column(db.Integer, db.ForeignKey('dispositivo.id_dispositivo'))
    parametro = db.Column(db.String(50))
    valor = db.Column(db.String(100))
    fecha_asignacion = db.Column(db.DateTime, default=db.func.current_timestamp())

db.create_all()
```

CRUD para Usuarios:

Código:

```python
@app.route('/api/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    new_usuario = Usuario(
        nombre=data['nombre'],
        email=data['email'],
        rol=data['rol'],
        password_hash=data['password_hash']
    )
    db.session.add(new_usuario)
    db.session.commit()
    return jsonify({'id_usuario': new_usuario.id_usuario}), 201

@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{'id_usuario': usuario.id_usuario, 'nombre': usuario.nombre, 'email': usuario.email, 'rol': usuario.rol} for usuario in usuarios])

@app.route('/api/usuarios/<int:id_usuario>', methods=['PUT'])
def update_usuario(id_usuario):
    data = request.json
    usuario = Usuario.query.get_or_404(id_usuario)
    usuario.nombre = data['nombre']
    usuario.email = data['email']
    usuario.rol = data['rol']
    usuario.password_hash = data['password_hash']
    db.session.commit()
    return jsonify({'id_usuario': usuario.id_usuario, 'nombre': usuario.nombre, 'email': usuario.email, 'rol': usuario.rol})

@app.route('/api/usuarios/<int:id_usuario>', methods=['DELETE'])
def delete_usuario(id_usuario):
    usuario = Usuario.query.get_or_404(id_usuario)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'id_usuario': id_usuario})
```

**Explicación:**

Crear Usuario:

```python
@app.route('/api/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    new_usuario = Usuario(
        nombre=data['nombre'],
        email=data['email'],
        rol=data['rol'],
        password_hash=data['password_hash']
    )
    db.session.add(new_usuario)
    db.session.commit()
    return jsonify({'id_usuario': new_usuario.id_usuario}), 201
```
Leer Usuarios:

```python
@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{'id_usuario': usuario.id_usuario, 'nombre': usuario.nombre, 'email': usuario.email, 'rol': usuario.rol} for usuario in usuarios])
```
Actualizar Usuario:

```python
@app.route('/api/usuarios/<int:id_usuario>', methods=['PUT'])
def update_usuario(id_usuario):
    data = request.json
    usuario = Usuario.query.get_or_404(id_usuario)
    usuario.nombre = data['nombre']
    usuario.email = data['email']
    usuario.rol = data['rol']
    usuario.password_hash = data['password_hash']
    db.session.commit()
    return jsonify({'id_usuario': usuario.id_usuario, 'nombre': usuario.nombre, 'email': usuario.email, 'rol': usuario.rol})
```

Borrar Usuario:

```python
@app.route('/api/usuarios/<int:id_usuario>', methods=['DELETE'])
def delete_usuario(id_usuario):
    usuario = Usuario.query.get_or_404(id_usuario)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'id_usuario': id_usuario})
```

### Pruebas con Postman
Para probar los endpoints anteriores, podemos utilizar Postman:

**Crear Usuario:**

Método: POST
URL: http://127.0.0.1:5000/api/usuarios
Body (raw JSON):
json
Copiar código
{
    "nombre": "Juan Perez",
    "email": "juan.perez@example.com",
    "rol": "admin",
    "password_hash": "hashed_password"
}  

**Leer Usuarios:**  

Método: GET
URL: http://127.0.0.1:5000/api/usuarios
Actualizar Usuario:

Método: PUT
URL: http://127.0.0.1:5000/api/usuarios/1
Body (raw JSON):
json
Copiar código
{
    "nombre": "Juan Perez",
    "email": "juan.perez@example.com",
    "rol": "user",
    "password_hash": "new_hashed_password"
}

**Borrar Usuario:**  

Método: DELETE
URL: http://127.0.0.1:5000/api/usuarios/1

## Conclusión
Flask es un framework versátil para el desarrollo de aplicaciones web en Python. Su naturaleza ligera y modularidad permiten a los desarrolladores construir aplicaciones desde simples hasta complejas, utilizando solo las herramientas necesarias. Con una comunidad activa y una amplia gama de extensiones, Flask sigue siendo una opción popular tanto para proyectos nuevos como para la migración de aplicaciones existentes.