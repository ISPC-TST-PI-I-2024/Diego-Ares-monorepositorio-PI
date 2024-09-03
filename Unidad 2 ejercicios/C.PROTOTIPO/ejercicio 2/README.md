# Implementación de BDNR con MongoDB  

Este documento describe la estructura y configuración necesaria para la implementación de una Base de Datos No Relacional (BDNR) usando MongoDB en un entorno Dockerizado. El objetivo es facilitar la creación, configuración y gestión de una base de datos MongoDB para su uso en aplicaciones y sistemas que requieren almacenamiento y manipulación de datos no relacionales.  

## Estructura de Directorios del Proyecto  
La estructura del proyecto se organiza en varios directorios y subdirectorios, cada uno con un propósito específico para facilitar la organización y el manejo del entorno de desarrollo y producción:  

    ```bash
baseDeDatos/  
│  
├── docker/  
│   ├── mongodb/  
│   │   ├── Dockerfile             # Dockerfile para configurar MongoDB  
│   │   └── mongodb.conf           # Configuración personalizada para MongoDB  
│   │  
│   └── docker-compose.yml         # Docker Compose para orquestar MongoDB  
│  
├── src/  
│   ├── mongodb/  
│   │   ├── init_db.py             # Script Python para inicializar la BD  
│   │   └── queries.py             # Script Python para operaciones básicas  
│   │  
│   └── README.md                  # Instrucciones y detalles del proyecto  
│  
├── tests/  
│   ├── mongodb/  
│   │   └── test_connection.py     # Prueba de conexión para MongoDB con Python  
│   │  
│   └── README.md                  # Guía de pruebas  
│  
├── .gitignore  
├── README.md                      # Documentación general del proyecto  
└── LICENSE  
  
    ```  

## Descripción de Directorios y Archivos  

**docker/:**  
  
Contiene todos los archivos necesarios para la configuración de Docker, incluyendo Dockerfiles y docker-compose.yml.  

docker/mongodb/:  

Dockerfile: Archivo de configuración para construir la imagen de Docker de MongoDB. Incluye instrucciones para instalar MongoDB y aplicar configuraciones personalizadas.  

mongodb.conf: Archivo de configuración personalizado para MongoDB que ajusta parámetros específicos para optimizar el rendimiento y la seguridad del servidor de base de datos.  

docker/docker-compose.yml:
Define y configura los servicios de Docker, incluyendo MongoDB. Este archivo permite gestionar cómo se orquestan los contenedores de Docker para el sistema de base de datos.  

**src/:**  

Contiene los scripts y el código fuente necesario para la base de datos.  

src/mongodb/:  

init_db.py: Script Python que utiliza pymongo para crear colecciones y documentos iniciales en la base de datos.  

queries.py: Script Python para ejecutar operaciones CRUD básicas en la base de datos.  

** tests/:**
Contiene scripts de prueba para verificar la configuración y conectividad de la base de datos.  

tests/mongodb/:

test_connection.py: Verifica la conexión con MongoDB usando Python para asegurar que la configuración es correcta y el servidor está operativo.

**Otros Archivos:**

.gitignore:
Define los archivos y directorios que Git deberá ignorar.  

README.md:
Proporciona una visión general del proyecto, incluyendo la estructura del directorio, instrucciones de instalación y configuración, y cualquier otra información relevante para usuarios y desarrolladores.  

LICENSE:
Define los términos bajo los cuales se distribuye el software.  


## 5 pasos para iniciar las pruebas.  

### Paso 1: Construir y Levantar los Contenedores  

Asegúrate de estar en el directorio donde se encuentra el docker-compose.yml y ejecuta los siguientes comandos:

Construir las imágenes:  

- docker-compose build    
 

Esto construirá la imagen de MongoDB con la configuración personalizada especificada en tu Dockerfile.

Levantar los servicios:

- docker-compose up -d  
 
Este comando levantará los contenedores en segundo plano (modo detached).  

### Paso 2: Inicializar la Base de Datos  
Deberás ejecutar el script init_db.py para inicializar la base de datos con datos de ejemplo:

Acceder al contenedor de Python:

- docker exec -it <nombre_del_servicio_python> /bin/bash  

Reemplaza <nombre_del_servicio_python> con el nombre del servicio de tu aplicación Python en el docker-compose.yml.  

Ejecutar el script de inicialización:  

- python src/mongodb/init_db.py  

Este script creará las colecciones y documentos iniciales en MongoDB.

### Paso 3: Ejecutar los Tests  
Una vez inicializada la base de datos, puedes ejecutar tus scripts de prueba para validar la funcionalidad del sistema.  

Ejecutar pruebas de CRUD (Crear, Leer, Actualizar, Eliminar):  
Puedes usar el script queries.py para ejecutar diferentes operaciones en la base de datos y observar los resultados.  

Ejecutar el script de test de conexión:  

- python src/mongodb/test_connection.py  

Este script verificará si la conexión a MongoDB funciona correctamente y si la colección 'posts' existe.  

### Paso 4: Monitorear los Resultados  
Utiliza los logs de Docker y MongoDB para monitorizar lo que está sucediendo:  

Ver los logs de Docker:  

- docker-compose logs  
  
Ver los logs de MongoDB:  
Puedes acceder a los logs de MongoDB dentro del contenedor para entender mejor cualquier problema que ocurra durante las pruebas.  

### Paso 5: Limpiar  
Una vez finalizadas las pruebas, es una buena práctica limpiar tu entorno:  

Detener y remover los contenedores:  

- docker-compose down  

Limpiar las imágenes si es necesario:  

- docker rmi <nombre_de_la_imagen>  
  
Con estos pasos se ejecutan y validan las pruebas correctamente.  
