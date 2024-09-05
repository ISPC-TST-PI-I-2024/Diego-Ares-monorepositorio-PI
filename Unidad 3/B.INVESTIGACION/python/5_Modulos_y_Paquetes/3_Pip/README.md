# Uso de Pip

Este documento proporciona una guía sobre cómo usar `pip` para instalar, actualizar y desinstalar paquetes en Python.

## Contenidos

- Introducción a Pip
- Instalación de Paquetes con Pip
- Actualización de Paquetes con Pip
- Desinstalación de Paquetes con Pip
- Listado de Paquetes Instalados
- Uso de `requirements.txt`

## Introducción a Pip

`pip` es el administrador de paquetes de Python. Te permite instalar y gestionar bibliotecas y dependencias que no forman parte de la biblioteca estándar de Python.

## Instalación de Paquetes con Pip

Para instalar un paquete, usa el comando `pip install`.

```sh
pip install nombre_paquete
```

### Ejemplo:

```sh
pip install requests
```

## Actualización de Paquetes con Pip
Para actualizar un paquete, usa el comando pip install --upgrade.

```sh
pip install --upgrade nombre_paquete
```

### Ejemplo:

```sh
pip install --upgrade requests
```

## Desinstalación de Paquetes con Pip
Para desinstalar un paquete, usa el comando pip uninstall.

```sh
pip uninstall nombre_paquete
```

### Ejemplo:

```sh
pip uninstall requests
```

## Listado de Paquetes Instalados
Para listar todos los paquetes instalados, usa el comando pip list.

```sh
pip list
```

## Uso de requirements.txt
El archivo requirements.txt se utiliza para especificar las dependencias de tu proyecto. Puedes crear este archivo y listar todos los paquetes necesarios, luego instalarlos usando pip.

```plaintext
Copiar código
# requirements.txt
requests==2.25.1
numpy==1.19.5
```

### Para instalar todos los paquetes listados en requirements.txt, usa el comando:

```sh
pip install -r requirements.txt
```

## Ejercicios
1. Instala el paquete pandas utilizando pip y verifica su instalación listando los paquetes instalados.
2. Actualiza el paquete numpy a la última versión utilizando pip.
3. Desinstala el paquete requests utilizando pip y verifica que ya no está instalado.
4. Crea un archivo requirements.txt con al menos tres paquetes y sus versiones específicas, y utiliza pip para instalar todos los paquetes listados en el archivo.
