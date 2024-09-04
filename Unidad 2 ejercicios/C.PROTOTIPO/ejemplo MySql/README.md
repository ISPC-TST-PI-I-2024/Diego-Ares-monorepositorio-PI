# Proyecto IoT - Parte Relacional

## Descripción del Ejercicio

Este proyecto está diseñado para manejar y almacenar datos de dispositivos IoT en un entorno multidisciplinario. La parte relacional de este proyecto involucra la creación de una base de datos MySQL para almacenar información sobre usuarios, dispositivos, categorías de dispositivos y eventos generados por estos dispositivos. 

## Objetivo

Desarrollar una base de datos relacional que permita:
- Almacenar información sobre dispositivos IoT y los usuarios que los gestionan.
- Clasificar dispositivos según su uso en diferentes sectores.
- Registrar eventos generados por los dispositivos.

## Árbol del Proyecto  

proyecto_iot/  
├── mysql/  
│ ├── init_db.sql # Script SQL para crear la base de datos y las tablas.  
│ ├── seed_data.sql # Script SQL para poblar las tablas con datos iniciales.  
│ └── queries.sql # Script SQL con las consultas que desees realizar.  
├── api/  
│ ├── app.py # Aplicación Flask para manejar las solicitudes API.  
│ └── README.md # Documentación específica para la API.  
├── utils/  
│ ├── db_connector.py # Módulo de Python para conectar con la base de datos MySQL.  
│ └── data_handler.py # Módulo de Python para funciones de manipulación y consulta de datos.  
├── .gitignore # Especifica archivos no rastreados por Git.  
├── LICENSE # Detalles de la licencia del proyecto.  
└── README.md # Documentación general del proyecto.  

## Stack Tecnológico

- **MySQL**: Utilizado para el almacenamiento y manejo de la base de datos relacional.
- **Python**: Lenguaje de programación para desarrollar la lógica de negocio y la API.
- **Flask**: Micro-framework de Python utilizado para crear la API que interactúa con la base de datos.
- **Visual Studio Code**: Editor de código recomendado para desarrollar el proyecto, con soporte para Python y MySQL.
- **MySQL Workbench**: Opcional para manejar visualmente la base de datos MySQL.

## Configuración y Uso

1. **Instalación de Dependencias**:
   - Asegúrese de tener Python y MySQL instalados en su sistema.
   - Instale las dependencias de Python especificadas en `api/requirements.txt`.

2. **Configuración de la Base de Datos**:
   - Ejecute `mysql/init_db.sql` para crear la estructura de la base de datos.
   - (Opcional) Ejecute `mysql/seed_data.sql` para insertar datos iniciales.

3. **Ejecución de la API**:
   - Navegue a la carpeta `api/` y ejecute `python app.py` para iniciar la API.

## Licencia

Este proyecto está licenciado bajo la [LICENCIA] (enlace a la licencia), que puede ser consultada para más detalles.