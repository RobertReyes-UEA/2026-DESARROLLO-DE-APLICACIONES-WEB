# Proyecto Integrador U2 - Avance 2

## Sistema Logístico de Monitoreo

## Descripción

Este proyecto corresponde a la **Semana 6** de la asignatura **Desarrollo de Aplicaciones Web**. Consiste en la mejora de un sitio web desarrollado en las semanas anteriores, incorporando validaciones dinámicas mediante JavaScript y manejo de formularios sin recargar la página.

El sistema permite registrar vehículos de una empresa de transporte, validando la información ingresada antes de almacenarla y mostrando los registros de forma dinámica.

## Tecnologías utilizadas

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* GitHub
* GitHub Pages

## Funcionalidades implementadas

* Diseño responsivo con Bootstrap.
* Formulario para registrar vehículos.
* Validaciones dinámicas en tiempo real utilizando los eventos **input**, **blur** y **submit**.
* Validación de campos obligatorios.
* Validación de longitud mínima para la placa y la descripción.
* Validación de selección del tipo de vehículo.
* Mensajes dinámicos de éxito y error.
* Uso de las clases de Bootstrap **is-valid**, **is-invalid**, **alert-success** y **alert-danger**.
* Manipulación del DOM mediante JavaScript.
* Registro de vehículos sin recargar la página utilizando **preventDefault()**.
* Creación dinámica de tarjetas con **createElement()** y **appendChild()**.
* Eliminación de registros mediante botones y eventos **click**.
* Contador automático del total de vehículos registrados.
## Nuevas funcionalidades

En esta actualización se reorganizó el proyecto pensando en una futura integración con Flask mediante plantillas reutilizables.

### Mejoras implementadas

- Organización de la interfaz mediante secciones reutilizables.
- Preparación para una futura plantilla `base.html`.
- Uso de un arreglo (`vehiculos[]`) para almacenar la información.
- Uso de objetos JavaScript para representar cada vehículo.
- Renderizado dinámico de tarjetas mediante la función `renderizarVehiculos()`.
- Implementación de estructuras repetitivas (`forEach`) para mostrar los registros.
- Uso de estructuras condicionales (`if`) para mostrar mensajes cuando no existen vehículos registrados.
- Conservación de las validaciones dinámicas desarrolladas en la Semana 6.
- Posibilidad de registrar y eliminar vehículos sin recargar la página.
- Diseño responsivo utilizando Bootstrap y CSS personalizado.

## Se incorporaron componentes de Bootstrap:

- Navbar responsiva.
- Sistema de rejillas.
- Cards.
- Formularios Bootstrap.
- Alertas.
- Modal.
- Spinner.
- Diseño adaptable.
## Estructura del proyecto

```text
Sistema-Logistico-Monitoreo/
│── index.html
│── style.css
│── script.js
│── README.md
```

## Objetivo del proyecto

Desarrollar una aplicación web interactiva que permita registrar, validar, mostrar, contar y eliminar vehículos de forma dinámica, aplicando JavaScript, manipulación del DOM, eventos y estilos con Bootstrap.

## Autor

**Robert Reyes**

## Asignatura

Desarrollo de Aplicaciones Web

## Publicación

El proyecto se encuentra alojado en **GitHub** y publicado mediante **GitHub Pages**.

