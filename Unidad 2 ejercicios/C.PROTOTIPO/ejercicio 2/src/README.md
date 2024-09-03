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

### Scripts de Operaciones CRUD para MongoDB en Python  

El script queries.py para realizar operaciones CRUD (Crear, Leer, Actualizar, Borrar) en MongoDB para los ejercicios de gestión de contenido para un blog y sistema de tickets para soporte técnico. Cada conjunto de operaciones está diseñado para manipular eficazmente las colecciones y documentos según las necesidades específicas de cada escenario.  
