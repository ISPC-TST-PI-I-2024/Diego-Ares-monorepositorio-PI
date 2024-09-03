from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def create_connection():
    """Crea una conexión a la base de datos."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='tu_usuario',
            password='tu_contraseña',
            database='IoTDevices'
        )
        print("Conexión a MySQL exitosa")
    except Error as e:
        print(f"El error '{e}' ocurrió")
    return connection

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    """Obtiene todos los usuarios de la base de datos."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(usuarios)

@app.route('/usuarios', methods=['POST'])
def create_usuario():
    """Crea un nuevo usuario en la base de datos."""
    conn = create_connection()
    cursor = conn.cursor()
    new_user = request.json
    cursor.execute("INSERT INTO Usuarios (Nombre, DetallesContacto) VALUES (%s, %s)",
                   (new_user['nombre'], new_user['detallesContacto']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_user), 201

@app.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    """Actualiza un usuario en la base de datos."""
    conn = create_connection()
    cursor = conn.cursor()
    updated_user = request.json
    cursor.execute("UPDATE Usuarios SET Nombre=%s, DetallesContacto=%s WHERE UsuarioID=%s",
                   (updated_user['nombre'], updated_user['detallesContacto'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(updated_user)

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    """Elimina un usuario de la base de datos."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE UsuarioID=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Usuario eliminado con éxito"}), 200

if __name__ == '__main__':
    app.run(debug=True)