# Sistema Logístico de Monitoreo

## Proyecto Integrador – Desarrollo de Aplicaciones Web

**Estudiante:** Robert Reyes
**Asignatura:** Desarrollo de Aplicaciones Web
**Año:** 2026
**Proyecto:** Sistema Logístico de Monitoreo

---

## Descripción del proyecto

El **Sistema Logístico de Monitoreo** es un proyecto web desarrollado para facilitar la administración y supervisión de vehículos de transporte.

La aplicación busca mejorar el control de las operaciones logísticas mediante el registro y gestión de información relacionada con vehículos, productos, clientes, proveedores y facturación.

El proyecto se ha desarrollado progresivamente utilizando **HTML5, CSS3, Bootstrap, JavaScript, Flask, Jinja2, Flask-WTF y WTForms**.

---

## Objetivo general

Desarrollar una aplicación web para apoyar la gestión de operaciones logísticas, incorporando una interfaz responsiva, formularios con validaciones, contenido dinámico y una estructura preparada para futuras conexiones con una base de datos.

---

## Tecnologías utilizadas

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Python
* Flask
* Jinja2
* Flask-WTF
* WTForms
* GitHub
* GitHub Pages

---

## Funcionalidades desarrolladas

### Interfaz web

* Página principal informativa.
* Encabezado del sistema.
* Menú de navegación responsivo.
* Sección Inicio.
* Sección Quiénes Somos.
* Sección Servicios.
* Sección Contacto.
* Información complementaria.
* Diseño adaptable para computadora, tablet y celular.

### JavaScript

* Registro dinámico de información.
* Manipulación del DOM.
* Uso de arreglos y objetos.
* Renderizado dinámico.
* Uso de `createElement()`.
* Uso de `appendChild()`.
* Eventos mediante `addEventListener()`.
* Eliminación de registros.
* Contador de registros.
* Validaciones dinámicas.
* Mensajes de error y éxito.

### Validaciones

El proyecto incorpora validaciones para evitar el registro de información incorrecta.

Se utilizan:

* `input`
* `blur`
* `submit`
* `preventDefault()`
* `is-valid`
* `is-invalid`
* `alert-success`
* `alert-danger`

También se validan campos obligatorios, longitud mínima, categorías y otros datos ingresados por el usuario.

---

## Flask

El proyecto fue preparado para trabajar con Python y Flask.

El archivo principal del backend es:

```text
app.py
```

Las principales rutas implementadas son:

```text
/
 /productos
 /clientes
 /proveedores
 /facturacion
```

Cada ruta utiliza `render_template()` para mostrar las páginas correspondientes.

---

## Estructura del proyecto

```text
Sistema-Logistico-Monitoreo/
│
├── app.py
├── requirements.txt
├── README.md
│
├── forms/
│   ├── __init__.py
│   ├── producto_form.py
│   ├── cliente_form.py
│   ├── proveedor_form.py
│   └── facturacion_form.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── productos.html
│   ├── clientes.html
│   ├── proveedores.html
│   ├── facturacion.html
│   │
│   └── components/
│       ├── navbar.html
│       └── footer.html
│
└── static/
    │
    ├── css/
    │   └── style.css
    │
    ├── js/
    │   └── script.js
    │
    └── img/
```

---

## Plantillas Jinja2

Para evitar repetir código HTML se utiliza una plantilla principal:

```text
base.html
```

Las páginas internas utilizan herencia mediante:

```jinja2
{% extends "base.html" %}
```

El contenido de cada página se incorpora mediante:

```jinja2
{% block content %}
{% endblock %}
```

Esto permite reutilizar el encabezado, menú, Bootstrap, archivos CSS, JavaScript y pie de página.

---

## Formularios Flask-WTF

El proyecto incorpora formularios independientes utilizando:

```python
FlaskForm
```

Los formularios se encuentran en:

```text
forms/
```

Los módulos implementados son:

* ProductoForm
* ClienteForm
* ProveedorForm
* FacturacionForm

Se utilizan validadores de WTForms como:

```python
DataRequired()
Length()
NumberRange()
Email()
```

Los formularios utilizan métodos `GET` y `POST` y validación mediante:

```python
form.validate_on_submit()
```

---

## Protección CSRF

Los formularios utilizan protección CSRF mediante Flask-WTF.

La aplicación configura una clave secreta mediante:

```python
app.config["SECRET_KEY"] = "clave-secreta-sistema-logistico-2026"
```

Los formularios incluyen:

```jinja2
{{ form.hidden_tag() }}
```

Esto permite incorporar el token de seguridad CSRF en los formularios.

---

## Datos demostrativos

En esta etapa del proyecto los datos son demostrativos y se almacenan temporalmente en estructuras de Python.

Se utilizan datos de ejemplo para:

* Productos.
* Clientes.
* Proveedores.
* Facturas.

La conexión con una base de datos será incorporada en una etapa posterior del proyecto.

---

## Ejemplo de producto

```text
Nombre: Monitoreo GPS
Descripción: Seguimiento de vehículos en tiempo real
Categoría: Monitoreo
Precio: $50.00
```

---

## Ejemplo de cliente

```text
Cliente: Cervecería Nacional
Correo: cliente@empresa.com
Teléfono: 0991234567
```

---

## Ejemplo de proveedor

```text
Empresa: GPS Ecuador
Contacto: Carlos Pérez
Correo: ventas@gpsecuador.com
```

---

## Ejemplo de factura

```text
Cliente: Cervecería Nacional
Concepto: Servicio de monitoreo
Total: $150.00
Estado: Pagada
```

---

## Organización por semanas

### Semana 4

Se desarrolló la interfaz principal utilizando:

* HTML5.
* CSS3.
* Bootstrap.
* Diseño responsive.
* Navbar.
* Formularios.
* Cards.
* Sistema de grillas.

### Semana 5

Se incorporó JavaScript para:

* Registrar información.
* Mostrar registros sin recargar.
* Contar registros.
* Eliminar registros.
* Manipular el DOM.
* Manejar eventos.

### Semana 6

Se incorporaron validaciones dinámicas mediante JavaScript.

Se validaron:

* Campos obligatorios.
* Longitud mínima.
* Categorías.
* Mensajes de error.
* Mensajes de éxito.

### Semana 7

Se incorporó el renderizado dinámico mediante:

* Arreglos.
* Objetos.
* Funciones.
* Estructuras repetitivas.
* Condicionales.

También se preparó la estructura para una futura integración con Flask.

### Semana 9

Se incorporó Flask y se organizó el proyecto mediante:

```text
templates/
static/
app.py
```

Se implementaron las rutas:

```text
/
 /productos
 /clientes
 /proveedores
 /facturacion
```

También se incorporó la herencia de plantillas mediante Jinja2.

### Semana 11

Se incorporaron formularios utilizando:

* Flask-WTF.
* WTForms.
* `FlaskForm`.
* `DataRequired()`.
* `Length()`.
* `NumberRange()`.
* `Email()`.

También se implementaron:

* Formularios independientes.
* Métodos GET y POST.
* `validate_on_submit()`.
* Mensajes mediante `flash()`.
* Protección CSRF.
* `SECRET_KEY`.

---

## Ejecución del proyecto Flask

Para ejecutar el proyecto localmente se debe instalar Python y posteriormente Flask.

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

También puede instalarse Flask-WTF directamente:

```bash
pip install flask-wtf
```

Para iniciar la aplicación:

```bash
python app.py
```

La aplicación estará disponible en:

```text
http://127.0.0.1:5000
```

---

## Rutas disponibles

Página principal:

```text
http://127.0.0.1:5000/
```

Productos:

```text
http://127.0.0.1:5000/productos
```

Clientes:

```text
http://127.0.0.1:5000/clientes
```

Proveedores:

```text
http://127.0.0.1:5000/proveedores
```

Facturación:

```text
http://127.0.0.1:5000/facturacion
```

---

## GitHub

El código fuente del proyecto se encuentra alojado en GitHub.

El repositorio contiene:

* Código HTML.
* Código CSS.
* Código JavaScript.
* Código Python.
* Plantillas Jinja2.
* Formularios Flask-WTF.
* Archivos de configuración.
* Documentación del proyecto.

---

## GitHub Pages

GitHub Pages se utiliza para publicar la parte frontend del proyecto.

Debido a que GitHub Pages no ejecuta aplicaciones Python/Flask, las rutas del backend Flask se prueban localmente mediante:

```text
http://127.0.0.1:5000
```

La publicación de GitHub Pages permite visualizar la interfaz web desarrollada en las etapas anteriores.

---

## Próximas etapas

En las siguientes etapas se podrá incorporar:

* Base de datos.
* Persistencia de información.
* CRUD completo.
* Autenticación de usuarios.
* API REST.
* Conexión entre Flask y base de datos.
* Sistema de monitoreo de vehículos.
* Gestión de información logística.

---

## Autor

**Robert Reyes**

Proyecto desarrollado para la asignatura:

**Desarrollo de Aplicaciones Web**

**2026**
