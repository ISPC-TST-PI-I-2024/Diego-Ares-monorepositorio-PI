# Instalación y Configuración

Este documento proporciona una guía sobre cómo instalar y configurar Python y Visual Studio Code (VSCode) para el desarrollo en Python.

## Contenidos

- Instalación de Python
- Instalación de Visual Studio Code (VSCode)
- Configuración de VSCode para Python
- Configuración de la extensión de Jupyter Notebook en VSCode
- Verificación de la instalación

## Instalación de Python

1. Ve a la [página oficial de Python](https://www.python.org/downloads/).
2. Descarga la última versión de Python para tu sistema operativo.
3. Sigue las instrucciones de instalación, asegurándote de marcar la opción "Add Python to PATH".

## Instalación de VSCode

1. Ve a la [página oficial de Visual Studio Code](https://code.visualstudio.com/).
2. Descarga el instalador correspondiente a tu sistema operativo.
3. Instala VSCode siguiendo las instrucciones.

## Configuración de VSCode para Python

1. Abre VSCode.
2. Instala la extensión de Python:
   - Ve a la barra lateral de extensiones (icono de cuadrados).
   - Busca "Python" y selecciona la extensión oficial de Microsoft.
   - Haz clic en "Install".
3. Configura el intérprete de Python:
   - Abre la paleta de comandos con `Ctrl+Shift+P` o `Cmd+Shift+P`.
   - Escribe "Python: Select Interpreter" y selecciona la versión de Python instalada.

## Configuración de la Extensión de Jupyter Notebook en VSCode

1. Abre VSCode.
2. Instala la extensión de Jupyter:
   - Ve a la barra lateral de extensiones (icono de cuadrados).
   - Busca "Jupyter" y selecciona la extensión oficial de Microsoft.
   - Haz clic en "Install".
3. Abre un archivo `.ipynb` o crea uno nuevo:
   - Haz clic en `File` > `New File` y selecciona `Jupyter Notebook`.
   - Guarda el archivo con la extensión `.ipynb`.

## Configuración del Entorno Virtual (Opcional pero Recomendado)

1. Abre un terminal en VSCode (`Ctrl+`` o `Cmd+``).
2. Navega al directorio de tu proyecto.
3. Crea un entorno virtual con el comando:
```bash
   python -m venv env  
```
## Activa el entorno virtual:  

En Windows: .\env\Scripts\activate  
En macOS/Linux: source env/bin/activate  
Asegúrate de seleccionar el intérprete del entorno virtual en VSCode:  
Abre la paleta de comandos con Ctrl+Shift+P o Cmd+Shift+P.  
Escribe "Python: Select Interpreter" y selecciona el intérprete dentro de la carpeta env.  

## Verificación de la Instalación  
Para verificar que todo está instalado correctamente, abre un terminal en VSCode y ejecuta los siguientes comandos:  

```bash
python --version
pip --version
```
Deberías ver la versión de Python y pip instaladas en tu sistema.

## Práctica con el Intérprete Interactivo (REPL)  
Abre una terminal y escribe python o python3 para iniciar el REPL.  
Prueba algunos comandos básicos:  

```python
print("¡Hola, mundo!")
import this  # Muestra el Zen de Python
import keyword
print(keyword.kwlist)  # Muestra las palabras reservadas en Python  
exit()  # Sale del intérprete interactivo
```
## Primeras Prácticas con Python  
**Ejecutar el Notebook**:
   - Abre el notebook `instalacion_configuracion.ipynb` en Jupyter Notebook, colab o VSCode.
   - Sigue las instrucciones y ejecuta las celdas de código para completar los ejercicios.

Este `README.md` proporciona una guía completa sobre cómo instalar y configurar Python y VSCode, configurar la extensión de Jupyter Notebook, y cómo realizar las primeras prácticas con Python.