-- Insertar usuarios iniciales
INSERT INTO Usuarios (Nombre, DetallesContacto) VALUES ('Ana Gómez', 'ana.gomez@example.com');
INSERT INTO Usuarios (Nombre, DetallesContacto) VALUES ('Luis Morales', 'luis.morales@example.com');

-- Insertar categorías de dispositivos
INSERT INTO CategoriasDispositivos (Nombre, Descripcion) VALUES ('Sensores', 'Dispositivos que detectan y responden a algunos tipos de entradas del entorno físico.');
INSERT INTO CategoriasDispositivos (Nombre, Descripcion) VALUES ('Actuadores', 'Dispositivos que actúan sobre el entorno.');

-- Insertar dispositivos
INSERT INTO Dispositivos (Nombre, Ubicacion, Tipo, UsuarioID, CategoriaID) VALUES ('Sensor de Temperatura', 'Oficina', 'sensor', 1, 1);
INSERT INTO Dispositivos (Nombre, Ubicacion, Tipo, UsuarioID, CategoriaID) VALUES ('Actuador Luz', 'Sala', 'actuador', 2, 2);

-- Insertar eventos de ejemplo
INSERT INTO Eventos (DispositivoID, TipoEvento, ValorEvento) VALUES (1, 'Temperatura', '21°C');
INSERT INTO Eventos (DispositivoID, TipoEvento, ValorEvento) VALUES (2, 'Estado Luz', 'Encendido');