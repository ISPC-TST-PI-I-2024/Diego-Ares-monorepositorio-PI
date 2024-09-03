# Implementación de Base de Datos Relacional con MySQL y Docker  

Este documento describe la estructura y configuración necesaria para la implementación de una Base de Datos Relacional (BDR) usando MySQL en un entorno Dockerizado. El objetivo es facilitar la creación, configuración, y gestión de una base de datos MySQL para su uso en aplicaciones y sistemas que requieren almacenamiento y manipulación de datos relacionales.

## Estructura de Directorios del Proyecto  

La estructura del proyecto se organiza en varios directorios y subdirectorios, cada uno con un propósito específico para facilitar la organización y el manejo del entorno de desarrollo y producción:  

´´´  
baseDeDatos/  
│  
├── docker/  
│   ├── mysql/  
│   │   ├── Dockerfile             # Dockerfile para configurar MySQL  
│   │   └── mysql.conf             # Configuración personalizada para MySQL  
│   │  
│   └── docker-compose.yml         # Docker Compose para orquestar MySQL y MongoDB  
│  
├── src/  
│   ├── mysql/  
│   │   ├── init-db.sql            # Scripts SQL para inicializar la base de datos  
│   │   └── queries.sql            # Scripts SQL para operaciones básicas  
│   │  
│   └── README.md                  # Instrucciones y detalles del proyecto  
│  
├── tests/  
│   ├── mysql/  
│   │   └── test_connection.py     # Prueba de conexión para MySQL  
│   │  
│   └── README.md                  # Guía de pruebas  
│  
├── .gitignore  
├── README.md                      # Documentación general del proyecto  
└── LICENSE    
  
´´´	

## Descripción de Directorios y Archivos  

**docker/:**  

Contiene todos los archivos necesarios para la configuración de Docker, incluyendo Dockerfiles y docker-compose.yml.  

docker/mysql/:

Dockerfile: Archivo de configuración para construir la imagen de Docker de MySQL. Incluye instrucciones para instalar MySQL y aplicar configuraciones personalizadas.  

mysql.conf: Archivo de configuración personalizado para MySQL que ajusta parámetros específicos para optimizar el rendimiento y la seguridad del servidor de base de datos.  

docker/docker-compose.yml:
Define y configura los servicios de Docker, incluyendo MySQL. Este archivo permite gestionar cómo se orquestan los contenedores de Docker para el sistema de base de datos.  

**src/:**

Contiene los scripts y el código fuente necesario para la base de datos.
src/mysql/:

init-db.sql: Script SQL que contiene los comandos para crear la estructura inicial de la base de datos, incluyendo tablas, relaciones, y datos de prueba.  

queries.sql: Script que contiene consultas SQL básicas para operaciones como inserción, actualización, consulta y eliminación de datos.  

**tests/:**  

Contiene scripts de prueba para verificar la configuración y conectividad de la base de datos.  

tests/mysql/:

test_connection.py: Script en Python para probar la conexión con la base de datos MySQL. Este script ayuda a verificar que la configuración de la base de datos se haya realizado correctamente y que el servicio de base de datos esté accesible.  

**otros archivos:**
.gitignore:
Define los archivos y directorios que Git deberá ignorar.  

README.md:
Proporciona una visión general del proyecto, incluyendo la estructura del directorio, instrucciones de instalación y configuración, y cualquier otra información relevante para usuarios y desarrolladores.  

LICENSE:
Define los términos bajo los cuales se distribuye el software.  

