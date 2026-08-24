# Sistema Logístico de Monitoreo

## Proyecto Integrador - Desarrollo de Aplicaciones Web

Este proyecto corresponde al desarrollo progresivo de un Sistema Logístico de Monitoreo, creado como parte de la asignatura Desarrollo de Aplicaciones Web.

El sistema está orientado al seguimiento y administración de unidades de transporte, permitiendo presentar información de vehículos, servicios, clientes, proveedores y facturación mediante una interfaz web moderna y responsiva.

El proyecto ha sido desarrollado progresivamente incorporando HTML5, CSS3, Bootstrap, JavaScript, manipulación del DOM, validaciones dinámicas, renderizado de contenido y posteriormente Python con Flask y Jinja2.

---

## Objetivo del proyecto

Desarrollar una aplicación web que permita representar y administrar información relacionada con operaciones logísticas y transporte, utilizando tecnologías web modernas y una estructura organizada que permita su futura conexión con una base de datos.

---

## Tecnologías utilizadas

- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- Python
- Flask
- Jinja2
- GitHub
- GitHub Pages

---

## Desarrollo del proyecto

### Semana 3 - Estructura HTML5

Se desarrolló la estructura inicial del sitio web utilizando HTML5 y etiquetas semánticas.

Se incorporaron elementos como:

- `header`
- `nav`
- `main`
- `section`
- `article`
- `aside`
- `footer`

También se desarrollaron las secciones principales del Sistema Logístico de Monitoreo.

---

### Semana 4 - Diseño con Bootstrap y CSS3

Se mejoró la presentación visual del proyecto mediante Bootstrap y CSS3.

Se incorporaron:

- Navbar responsiva.
- Sistema de grillas.
- Botones Bootstrap.
- Tarjetas.
- Formularios.
- Imágenes responsivas.
- Espaciado.
- Colores.
- Sombras.
- Bordes.
- Efectos visuales.
- Media queries.

El proyecto fue preparado para visualizarse correctamente en computadoras, tablets y celulares.

---

### Semana 5 - JavaScript, DOM y eventos

Se incorporó JavaScript para agregar funcionalidad dinámica al proyecto.

El sistema permite:

- Registrar vehículos.
- Mostrar vehículos en pantalla.
- Contar registros.
- Eliminar registros.
- Manipular elementos del DOM.
- Utilizar `createElement()`.
- Utilizar `appendChild()`.
- Utilizar `addEventListener()`.
- Utilizar `preventDefault()`.

Los registros se muestran sin necesidad de recargar la página.

---

### Semana 6 - Validaciones dinámicas

Se incorporaron validaciones dinámicas al formulario de registro de vehículos.

Se validan:

- Placa del vehículo.
- Descripción.
- Tipo de vehículo.

También se implementaron eventos:

- `input`
- `blur`
- `change`
- `submit`

Se utilizan clases de Bootstrap para mostrar visualmente los estados de validación:

- `is-valid`
- `is-invalid`
- `alert-success`
- `alert-danger`

El sistema evita registrar información cuando existen errores en los campos.

---

### Semana 7 - Renderizado dinámico

Se reorganizó el proyecto para utilizar estructuras de datos y renderizado dinámico mediante JavaScript.

Se implementaron:

- Arreglos.
- Objetos.
- Funciones.
- Estructuras repetitivas.
- Condicionales.
- Renderizado dinámico.
- Tarjetas generadas mediante JavaScript.

Los vehículos son almacenados temporalmente en un arreglo y posteriormente renderizados en la interfaz.

También se preparó la estructura del proyecto para una futura migración hacia Flask y Jinja2.

---

### Semana 9 - Implementación de Flask

Se incorporó Python Flask al proyecto.

Se creó una estructura organizada utilizando:

```text
app.py
requirements.txt

templates/
    base.html
    index.html
    productos.html
    clientes.html
    proveedores.html
    facturacion.html

    components/
        navbar.html
        footer.html

static/
    css/
        style.css

    js/
        script.js

    img/
