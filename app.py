from flask import Flask, render_template

app = Flask(__name__)


# ==============================
# INICIO
# ==============================

@app.route("/")
def inicio():

    nombre_sistema = "Sistema Logístico de Monitoreo"

    descripcion = (
        "Plataforma para el control, seguimiento y "
        "administración de unidades de transporte."
    )

    return render_template(
        "index.html",
        nombre_sistema=nombre_sistema,
        descripcion=descripcion
    )


# ==============================
# PRODUCTOS / SERVICIOS
# ==============================

@app.route("/productos")
def productos():

    productos = [

        {
            "nombre": "Monitoreo GPS",
            "descripcion": "Seguimiento de vehículos en tiempo real.",
            "categoria": "Monitoreo",
            "precio": 50.00,
            "stock": 10
        },

        {
            "nombre": "Control de rutas",
            "descripcion": "Seguimiento y control de recorridos.",
            "categoria": "Logística",
            "precio": 75.00,
            "stock": 5
        },

        {
            "nombre": "Alertas de seguridad",
            "descripcion": "Sistema de alertas para unidades.",
            "categoria": "Seguridad",
            "precio": 35.00,
            "stock": 0
        },

        {
            "nombre": "Reporte logístico",
            "descripcion": "Generación de reportes de operaciones.",
            "categoria": "Reportes",
            "precio": 25.00,
            "stock": 8
        }

    ]

    return render_template(
        "productos.html",
        productos=productos
    )


# ==============================
# CLIENTES
# ==============================

@app.route("/clientes")
def clientes():

    clientes = [

        {
            "nombre": "Empresa ABC",
            "correo": "empresaabc@gmail.com",
            "telefono": "0991111111",
            "estado": "Activo"
        },

        {
            "nombre": "Transportes Costa",
            "correo": "transportescosta@gmail.com",
            "telefono": "0982222222",
            "estado": "Activo"
        },

        {
            "nombre": "Logística Peninsular",
            "correo": "logisticapeninsular@gmail.com",
            "telefono": "0973333333",
            "estado": "Inactivo"
        }

    ]

    return render_template(
        "clientes.html",
        clientes=clientes
    )


# ==============================
# PROVEEDORES
# ==============================

@app.route("/proveedores")
def proveedores():

    proveedores = [

        {
            "empresa": "GPS Ecuador",
            "servicio": "Equipos GPS",
            "telefono": "0961111111",
            "estado": "Activo"
        },

        {
            "empresa": "Seguridad Vehicular",
            "servicio": "Sistemas de seguridad",
            "telefono": "0952222222",
            "estado": "Activo"
        },

        {
            "empresa": "Tecnología Logística",
            "servicio": "Software de monitoreo",
            "telefono": "0943333333",
            "estado": "Inactivo"
        }

    ]

    return render_template(
        "proveedores.html",
        proveedores=proveedores
    )


# ==============================
# FACTURACIÓN
# ==============================

@app.route("/facturacion")
def facturacion():

    facturas = [

        {
            "numero": "FAC-001",
            "cliente": "Empresa ABC",
            "total": 150.00,
            "estado": "Pagada"
        },

        {
            "numero": "FAC-002",
            "cliente": "Transportes Costa",
            "total": 220.00,
            "estado": "Pendiente"
        },

        {
            "numero": "FAC-003",
            "cliente": "Logística Peninsular",
            "total": 180.00,
            "estado": "Pagada"
        }

    ]

    return render_template(
        "facturacion.html",
        facturas=facturas
    )


# ==============================
# EJECUTAR FLASK
# ==============================

if __name__ == "__main__":
    app.run(debug=True)
