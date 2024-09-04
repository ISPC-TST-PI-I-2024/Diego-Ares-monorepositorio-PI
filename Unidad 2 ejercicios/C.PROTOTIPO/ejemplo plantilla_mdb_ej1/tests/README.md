# Ejercicio 1: Gestión de Contenido para un Blog  

## Situación del Mundo Real:  
Un sistema de gestión de contenido (CMS) para un blog que necesita manejar publicaciones, comentarios y autores.  

### Planteo del Ejercicio:  
El sistema debe permitir:  

- Crear publicaciones con título, contenido, autor y fecha de publicación.
- Añadir comentarios a las publicaciones, con referencia al autor del comentario y la fecha.
- Mantener un registro de autores con nombre y biografía.  

**Modelo de Datos No Relacional:**  

Publicaciones: Documentos que contienen título, contenido, información del autor (referencia a Autores), y comentarios (lista de documentos embebidos).  

Autores: Documentos que contienen nombre y biografía.  

Comentarios: Documentos embebidos en Publicaciones con contenido, autor del comentario (referencia a Autores) y fecha.  

**Implementación en MongoDB:**  

Colecciones:

Publicaciones
Documentos con titulo, contenido, autor_id, fecha, y comentarios (array de documentos embebidos con contenido, autor_id, y fecha).  

Autores
Documentos con nombre y biografia. 

### Scripts de Pruebas de Conexión para MongoDB en Python  

Los scripts de prueba de conexión test_connection.py para ambos ejercicios (blog y sistema de tickets de soporte técnico) aseguran que la conexión a la base de datos MongoDB esté correctamente configurada y operativa. Este paso es crucial para verificar antes de comenzar cualquier operación con la base de datos.