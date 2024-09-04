-- Obtener todos los usuarios
SELECT * FROM Usuarios;

-- Obtener un usuario específico por ID
SELECT * FROM Usuarios WHERE UsuarioID = 1;

-- Agregar un nuevo usuario
INSERT INTO Usuarios (Nombre, DetallesContacto) VALUES ('Juan Perez', 'juan.perez@example.com');

-- Actualizar detalles de contacto de un usuario
UPDATE Usuarios SET DetallesContacto = 'nuevo.email@example.com' WHERE UsuarioID = 1;

-- Eliminar un usuario
DELETE FROM Usuarios WHERE UsuarioID = 1;

-- Listar todos los dispositivos
SELECT * FROM Dispositivos;

-- =============================================
-- Obtener dispositivos de un usuario específico
SELECT * FROM Dispositivos WHERE UsuarioID = 1;

-- Agregar un nuevo dispositivo
INSERT INTO Dispositivos (Nombre, Ubicacion, Tipo, UsuarioID, CategoriaID) VALUES ('Sensor de Temperatura', 'Sala', 'sensor', 1, 2);

-- Actualizar ubicación de un dispositivo
UPDATE Dispositivos SET Ubicacion = 'Cocina' WHERE DispositivoID = 1;

-- Eliminar un dispositivo
DELETE FROM Dispositivos WHERE DispositivoID = 1;

-- ================================================
-- Ver todos los eventos de un dispositivo específico
SELECT * FROM Eventos WHERE DispositivoID = 1;

-- Insertar un nuevo evento
INSERT INTO Eventos (DispositivoID, TipoEvento, ValorEvento) VALUES (1, 'Temperatura', '22°C');

-- ================================================
