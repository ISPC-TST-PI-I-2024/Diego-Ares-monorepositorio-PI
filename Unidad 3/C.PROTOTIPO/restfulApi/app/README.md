# Directorio `app`

El directorio `app` contiene el núcleo de la aplicación FastAPI. Está organizado para seguir las mejores prácticas de desarrollo, permitiendo un mantenimiento fácil, escalabilidad y claridad en el código.

## Fundamentación de la Arquitectura

La arquitectura del proyecto está diseñada para separar las preocupaciones y modularizar el código, lo que facilita su gestión y escalabilidad. Cada módulo tiene una responsabilidad específica y se comunica con otros módulos a través de interfaces bien definidas.

## Estructura del Directorio

   ```bash

app/
├── routers/
│ ├── data.py
│ ├── devices.py
│ ├── projects.py
│ ├── security.py
│ ├── users.py
│ ├── configurations.py
├── config.py
├── crud.py
├── db.py
├── main.py
├── models.py
├── schemas.py
├── README.md
   ```

### Descripción de cada archivo y carpeta

- **`routers/`**: Este directorio contiene los diferentes módulos de rutas (endpoints) organizados por funcionalidad. Cada archivo en este directorio define los endpoints relacionados con una entidad específica de la base de datos.

  - **`data.py`**: Endpoints relacionados con la gestión de los datos recolectados por los dispositivos.
  - **`devices.py`**: Endpoints relacionados con la gestión de los dispositivos.
  - **`projects.py`**: Endpoints relacionados con la gestión de proyectos.
  - **`security.py`**: Endpoints relacionados con la seguridad, como la gestión de permisos y autenticación.
  - **`users.py`**: Endpoints relacionados con la gestión de usuarios.
  - **`configurations.py`**: Endpoints relacionados con la gestión de configuraciones de los dispositivos.

- **`config.py`**: Contiene la configuración de la aplicación, incluyendo variables de entorno y otros parámetros de configuración necesarios.

- **`crud.py`**: Define las operaciones CRUD (Create, Read, Update, Delete) para interactuar con la base de datos. Esto incluye funciones para cada entidad de la base de datos.

- **`db.py`**: Configuración de la conexión a la base de datos y la creación del motor de la base de datos utilizando SQLAlchemy.

- **`main.py`**: Punto de entrada de la aplicación FastAPI. Aquí se inicializa la instancia de FastAPI y se incluyen los routers.

- **`models.py`**: Define los modelos de datos usando SQLAlchemy, mapeando las tablas de la base de datos a clases Python.

- **`schemas.py`**: Define los esquemas de datos con Pydantic para la validación y serialización de datos.

- **`README.md`**: Este archivo. Proporciona una visión general del contenido y la estructura del directorio `app`.

## Base de Datos

La API se integra con una base de datos MySQL. A continuación se describe la estructura de la base de datos:

### Estructura de la Base de Datos

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
### Endpoints desarrollados  
A continuación se presentan los endpoints desarrollados para cada tabla en la base de datos:

**Usuarios**  

- GET /users/: Obtener todos los usuarios.
- POST /users/: Crear un nuevo usuario.
- GET /users/{user_id}: Obtener un usuario por ID.
- PUT /users/{user_id}: Actualizar un usuario por ID.
- DELETE /users/{user_id}: Eliminar un usuario por ID.

**Dispositivos**  

- GET /devices/: Obtener todos los dispositivos.
- POST /devices/: Crear un nuevo dispositivo.
- GET /devices/{device_id}: Obtener un dispositivo por ID.
- PUT /devices/{device_id}: Actualizar un dispositivo por ID.
- DELETE /devices/{device_id}: Eliminar un dispositivo por ID.

**Datos de Dispositivos**  

- GET /data/: Obtener todos los datos de dispositivos.
- POST /data/: Crear un nuevo dato de dispositivo.
- GET /data/{data_id}: Obtener un dato de dispositivo por ID.
- PUT /data/{data_id}: Actualizar un dato de dispositivo por ID.
- DELETE /data/{data_id}: Eliminar un dato de dispositivo por ID.

**Seguridad**  

- GET /security/: Obtener todos los registros de seguridad.
- POST /security/: Crear un nuevo registro de seguridad.
- GET /security/{security_id}: Obtener un registro de seguridad por ID.
- PUT /security/{security_id}: Actualizar un registro de seguridad por ID.
- DELETE /security/{security_id}: Eliminar un registro de seguridad por ID.

**Proyectos**  

- GET /projects/: Obtener todos los proyectos.
- POST /projects/: Crear un nuevo proyecto.
- GET /projects/{project_id}: Obtener un proyecto por ID.
- PUT /projects/{project_id}: Actualizar un proyecto por ID.
- DELETE /projects/{project_id}: Eliminar un proyecto por ID.

**Configuraciones**  

- GET /configurations/: Obtener todas las configuraciones.
- POST /configurations/: Crear una nueva configuración.
- GET /configurations/{config_id}: Obtener una configuración por ID.
- PUT /configurations/{config_id}: Actualizar una configuración por ID.
- DELETE /configurations/{config_id}: Eliminar una configuración por ID.  
