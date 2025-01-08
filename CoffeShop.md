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


# **Creacion de la aplicacion Products con Formularios en Django**
La funcionalidad de formularios en Django permite a los desarrolladores crear, validar y gestionar formularios de manera eficiente y organizada. A continuación, exploraremos cómo crear formularios en Django paso a paso.

## **¿Cómo se crean formularios en Django?**
Para crear un nuevo formulario en Django, primero se debe crear una clase que herede de `forms.Form`. Esta clase contendrá todos los campos que queremos incluir en el formulario.

**Crear el archivo forms.py**

```py
from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label='Nombre')
    description = forms.CharField(max_length=300, label='Descripción')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Precio')
    available = forms.BooleanField(initial=True, label='Disponible', required=False)
    photo = forms.ImageField(label='Foto', required=False)
```

## **¿Cómo se manejan los datos del formulario en Django?**
Una vez que el formulario está creado, necesitamos definir cómo manejar los datos cuando el usuario envía el formulario. Esto incluye validar los datos y guardarlos en la base de datos.

**Método save para guardar datos**

```py
def save(self):
    from .models import Product
    data = self.cleaned_data
    Product.objects.create(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        available=data['available'],
        photo=data['photo']
    )
```

## **¿Cómo se crea la vista para el formulario?**
La vista conecta el formulario con el template y maneja el request del usuario. Usaremos una vista genérica de Django para simplificar este proceso.

**Crear la vista**

```py
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ProductForm

class ProductFormView(FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
```

## **¿Cómo se configuran las URLs para la vista?**
Es necesario configurar las URLs para que la vista esté accesible desde el navegador.

**Configurar urls.py**

```py
from django.urls import path
from .views import ProductFormView

urlpatterns = [
    path('add/', ProductFormView.as_view(), name='add_product')
]
```

## **¿Cómo se crea el template para el formulario?**
El template define la estructura HTML del formulario y cómo se renderiza en la página web.

**Crear el template add_product.html**

```html
<h1>Agregar Producto</h1>
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Agregar</button>
</form>
```

## **¿Qué es el CSRF token y por qué es importante?**
El CSRF token es una medida de seguridad que protege contra ataques de tipo Cross-Site Request Forgery. Django lo incluye automáticamente en los formularios para asegurar que las solicitudes provengan de fuentes confiables.

## **¿Cómo se maneja la redirección después de enviar el formulario?**
La redirección después del envío del formulario se maneja configurando el parámetro `success_url` en la vista, utilizando `reverse_lazy` para obtener la URL de destino.

## **¿Cómo se valida y guarda el producto?**
Cuando el formulario es válido, el método `form_valid` se encarga de llamar al método `save` del formulario para guardar el producto en la base de datos.
