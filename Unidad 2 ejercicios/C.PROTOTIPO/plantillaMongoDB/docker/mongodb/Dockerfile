# Usamos la imagen oficial de MongoDB
FROM mongo:latest

# Copiamos el archivo de configuración personalizada en el contenedor
COPY mongodb.conf /etc/mongo/mongodb.conf

# Exponemos el puerto predeterminado de MongoDB
EXPOSE 27017

# Ejecutamos MongoDB usando el archivo de configuración personalizado
CMD ["mongod", "--config", "/etc/mongo/mongodb.conf"]