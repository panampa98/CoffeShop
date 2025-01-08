# **Configuración de un proyecto en Django**

## **¿Cómo crear y activar el entorno virtual?**
Para iniciar, nos posicionamos en la carpeta deseada en nuestro editor. Creamos el entorno virtual con:

```bash
python -m venv <ruta_donde_guardar>/Coffee_Shop
```

Activamos el entorno con:
```bash
source Coffee_Shop/bin/activate
```

Verificamos su activación y procedemos a instalar Django:
```bash
pip install django
```

## **¿Cómo iniciar un proyecto Django?**
Creamos el proyecto utilizando el comando:

```bash
django-admin startproject Coffee_Shop
```

Listamos las carpetas para confirmar la creación del proyecto. Abrimos el proyecto en Visual Studio Code:

```bash
code -r Coffee_Shop
```
Ahora tenemos el archivo `manage.py` y las configuraciones listas en nuestro editor.

## **¿Qué extensiones instalar en Visual Studio Code?**
Aprovechamos las alertas de Visual Studio Code para instalar extensiones esenciales como:
- Python
- PyLance
- Python Debugger
- Black (formateo de código)
- Django (para visualizar templates)

## **¿Cómo configurar el control de versiones con Git?**
Inicializamos un repositorio Git:

```bash
git init
```

Añadimos y comiteamos los archivos iniciales creados por Django:

```bash
git add .
git commit -m "Initial setup"
```

## **¿Cómo crear y utilizar un archivo .gitignore?**
Para evitar subir archivos innecesarios al repositorio, generamos un archivo .`gitignore` con *gitignore.io* especificando “Django” como criterio. Pegamos el contenido generado en un nuevo archivo `.gitignore` y lo comiteamos:

```bash
git add .gitignore
git commit -m "Add .gitignore"
```

## **¿Cómo manejar las dependencias del proyecto?**
Creamos dos archivos para gestionar las dependencias:

1. **requirements.txt:** para dependencias de producción.
2. **requirements-dev.txt:** para dependencias de desarrollo como `iPython`.

Agregamos las dependencias instaladas en nuestro entorno actual:

`pip freeze > requirements.txt`

Comiteamos ambos archivos:

```bash
git add requirements.txt requirements-dev.txt
git commit -m "Add requirements files"
```

## **¿Cómo continuar con la configuración del proyecto?**
Con el entorno preparado, es importante crear un archivo base HTML que sirva como plantilla. Te reto a crear `base.html` con un menú y un pie de página para usar en el curso de Django.

## **¿Qué permite hacer Pillow con los campos de imagen?**
Pillow permite realizar validaciones en imágenes, como asegurarse de que las imágenes subidas cumplan con ciertas características en cuanto a resolución.