# Tutorial de Postman

Postman es una poderosa herramienta para probar APIs. Aquí encontrarás cómo utilizar Postman para probar la API RESTful que has creado con Flask.

## Instalación

Para empezar, necesitarás descargar e instalar Postman desde su [sitio web oficial](https://www.postman.com/downloads/).

## Prueba de la API

Sigue estos pasos para probar tu API con Postman:

### 1. Iniciar tu servidor Flask

Ejecuta `python app.py` en tu terminal.

### 2. Abre Postman

Una vez abierto, verás un campo para ingresar una URL. Esta es la ruta a la que quieres enviar una solicitud.

### 3. Ingresar la URL de tu API

Como estás ejecutando el servidor en tu propia máquina, la URL base será `http://localhost:5000/`.

### 4. Seleccionar el tipo de solicitud

A la derecha del campo URL, hay un menú desplegable para seleccionar el tipo de solicitud HTTP que quieres enviar (GET, POST, PUT o DELETE).

Aquí están los detalles de cómo probar cada método:

#### GET

- Selecciona 'GET' en el menú desplegable y escribe `http://localhost:5000/blog` en la barra de URL.
- Haz clic en el botón 'Send'. Deberías ver un arreglo JSON de todas las publicaciones en la respuesta.

#### POST

- Selecciona 'POST' en el menú desplegable y escribe `http://localhost:5000/blog` en la barra de URL.
- Haz clic en la pestaña 'Body', luego selecciona 'raw' y cambia el formato a 'JSON'.
- Escribe el cuerpo de tu solicitud en formato JSON, por ejemplo: `{"id": 3, "contenido": "Mi tercera publicación"}`.
- Haz clic en el botón 'Send'. Deberías ver la nueva publicación en la respuesta.

#### PUT

- Selecciona 'PUT' en el menú desplegable y escribe `http://localhost:5000/blog/1` en la barra de URL, donde '1' es el ID de la publicación que quieres actualizar.
- Escribe el cuerpo de tu solicitud en formato JSON, por ejemplo: `{"contenido": "Contenido de la publicación actualizado"}`.
- Haz clic en el botón 'Send'. Deberías ver la publicación actualizada en la respuesta.

#### DELETE

- Selecciona 'DELETE' en el menú desplegable y escribe `http://localhost:5000/blog/1` en la barra de URL, donde '1' es el ID de la publicación que quieres eliminar.
- Haz clic en el botón 'Send'. Deberías ver un mensaje indicando que la publicación se eliminó con éxito.