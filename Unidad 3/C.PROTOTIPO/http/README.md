## Problemas con la version original

Cuando corro la pagina web con live server me dice : 

Respuesta del servidor:  

  
Lo cual esta mal, porque debiera poner:  
  
Respuesta del servidor: ¡Hola Mundo!  
  
y no pone nada, la direccion en live server es: http://127.0.0.1:5500/index.html

**Solucion:** 

Es posible que te estés encontrando con un problema de seguridad llamado "política del mismo origen" (Same-Origin Policy). Por defecto, los navegadores web no permiten que una página web en un origen (por ejemplo, http://127.0.0.1:5500) haga solicitudes AJAX a un origen diferente (en este caso, http://127.0.0.1:5000). Esta política está diseñada para prevenir ciertos tipos de ataques de seguridad.

Sin embargo, en el caso de desarrollo local, puedes evitar este problema utilizando un proxy o permitiendo explícitamente las solicitudes de orígenes cruzados en tu servidor Flask. Para este último, Flask tiene una extensión llamada Flask-CORS que puedes usar. Puedes instalarla con el siguiente comando:

**pip install -U flask-cors**

Luego, puedes utilizarla en tu aplicación Flask de la siguiente manera:


from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Esto habilita CORS para todas las rutas.

@app.route('/')
def home():
    return jsonify(message='¡Hola Mundo!')

if __name__ == '__main__':
    app.run(debug=True)


Reinicia tu servidor Flask y prueba nuevamente la página web. Ahora deberías poder ver la respuesta del servidor en la página.

Si estás utilizando un proxy, asegúrate de que esté configurado correctamente. Si estás utilizando el servidor de desarrollo de Flask, no necesitas un proxy.