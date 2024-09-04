# Implementación de BDNR con MongoDB  

Este documento describe la estructura y configuración necesaria para la implementación de una Base de Datos No Relacional (BDNR) usando MongoDB. El objetivo es facilitar la creación, configuración y gestión de una base de datos MongoDB para su uso en aplicaciones y sistemas que requieren almacenamiento y manipulación de datos no relacionales.  

## Estructura de Directorios del Proyecto  
La estructura del proyecto se organiza en varios directorios y subdirectorios, cada uno con un propósito específico para facilitar la organización y el manejo del entorno de desarrollo y producción:  

    ```bash
baseDeDatos/  
│  
│  
├── src/  
│   ├── mongodb/  
│   │   ├── init_db.py             # Script Python para inicializar la BD  
│   │   └── queries.py             # Script Python para operaciones básicas  
|   |
|   |__ main.py                    # Script Python para ejecutar operaciones CRUD    
│   │  
│   └── README.md                  # Instrucciones y detalles del proyecto  
│  
├── tests/  
│   ├── json/                      # Archivos JSON para pruebas
│   │   
│   ├── mongodb/ 
│   │   ├── semillaJson.py         # Script Python para generar datos de prueba  
│   │   └── test_connection.py     # Prueba de conexión para MongoDB con Python  
│   │  
│   └── README.md                  # Guía de pruebas  
│  
├── .gitignore  
├── README.md                      # Documentación general del proyecto  
└── LICENSE  
  
    ```  

## Descripción de Directorios y Archivos  

**src/:**  

Contiene los scripts y el código fuente necesario para la base de datos.  

src/mongodb/:  

init_db.py: Script Python que utiliza pymongo para crear colecciones y documentos iniciales en la base de datos.  

queries.py: Script Python para definir operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en la base de datos.  
  
main.py: Script Python para ejecutar operaciones CRUD en la base de datos.

** tests/:**
Contiene scripts de prueba para verificar la configuración y conectividad de la base de datos.  

tests/mongodb/:

semillaJson.py: Script Python para generar datos de prueba en formato JSON para insertar en la base de datos.

test_connection.py: Verifica la conexión con MongoDB usando Python para asegurar que la configuración es correcta y el servidor está operativo.

**Otros Archivos:**

.gitignore:
Define los archivos y directorios que Git deberá ignorar.  

README.md:
Proporciona una visión general del proyecto, incluyendo la estructura del directorio, instrucciones de instalación y configuración, y cualquier otra información relevante para usuarios y desarrolladores.  

LICENSE:
Define los términos bajo los cuales se distribuye el software.  


## 5 pasos para iniciar las pruebas.  

### Paso 1: MongoDb Compass 

Inicializa MongoDb compass para visualizar la base de datos.  
Conecte la URI mongodb://localhost:27017 en la interfaz de MongoDb Compass.

### Paso 2: Generar las semillas de pruebas  

- Ejecute el script semillaJson.py para generar datos de prueba en formato JSON.  > python tests/mongodb/semillaJson.py  
-  Verifique que los datos se han generado correctamente en la carpeta tests/json.  

### Paso 3: Inicializar, Cargar y Probar la Base de Datos

- Inicializa la base de datos con el script main.py. 
- > python src/main.py
- Este scrip agrega un documento a las colecciones de la base de datos.

### Paso 4: Monitorear los Resultados en compass

- Verifique que los datos se han insertado correctamente en la base de datos. 
- La base de datos se llama: "blog_system" y las colecciones son: "autores" y "publicaciones".

### Paso 5: Limpiar  
Una vez finalizadas las pruebas, es una buena práctica limpiar tu entorno:  

- Elimina los datos de prueba generados en la carpeta tests/json.
- Elimina los documentos insertados en la base de datos con el script main.py.
- Eliminar la base de datos "blog_system" en MongoDB Compass.
- Detener el servidor de MongoDB si no se está utilizando.
- Borrar localhost:27017 en la interfaz de MongoDb Compass.
 
