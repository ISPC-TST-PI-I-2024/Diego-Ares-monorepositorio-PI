from db_connector import create_connection, close_connection

def get_usuarios():
    """Retorna una lista de todos los usuarios desde la base de datos."""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    close_connection(connection)
    return usuarios

def add_usuario(nombre, detalles_contacto):
    """Agrega un nuevo usuario a la base de datos."""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Usuarios (Nombre, DetallesContacto) VALUES (%s, %s)", (nombre, detalles_contacto))
    connection.commit()
    cursor.close()
    close_connection(connection)
    return cursor.lastrowid  # Retorna el ID del nuevo usuario

def update_usuario(usuario_id, nombre, detalles_contacto):
    """Actualiza la información de un usuario existente."""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Usuarios SET Nombre=%s, DetallesContacto=%s WHERE UsuarioID=%s",
                   (nombre, detalles_contacto, usuario_id))
    connection.commit()
    cursor.close()
    close_connection(connection)

def delete_usuario(usuario_id):
    """Elimina un usuario de la base de datos."""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE UsuarioID=%s", (usuario_id,))
    connection.commit()
    cursor.close()
    close_connection(connection)