-- Creación de la base de datos (opcional, depende de la configuración previa)
CREATE DATABASE IF NOT EXISTS IoTDevices;
USE IoTDevices;

-- Creación de la tabla Usuarios
CREATE TABLE Usuarios (
    UsuarioID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    DetallesContacto VARCHAR(255)
);

-- Creación de la tabla Categorías de Dispositivos
CREATE TABLE CategoriasDispositivos (
    CategoriaID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Descripcion VARCHAR(255)
);

-- Creación de la tabla Dispositivos
CREATE TABLE Dispositivos (
    DispositivoID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Ubicacion VARCHAR(255),
    Tipo ENUM('sensor', 'actuador', 'híbrido') NOT NULL,
    UsuarioID INT,
    CategoriaID INT,
    FOREIGN KEY (UsuarioID) REFERENCES Usuarios(UsuarioID),
    FOREIGN KEY (CategoriaID) REFERENCES CategoriasDispositivos(CategoriaID)
);

-- Creación de la tabla Eventos
CREATE TABLE Eventos (
    EventoID INT AUTO_INCREMENT PRIMARY KEY,
    DispositivoID INT NOT NULL,
    TipoEvento VARCHAR(255) NOT NULL,
    ValorEvento VARCHAR(255),
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (DispositivoID) REFERENCES Dispositivos(DispositivoID)
);