from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/productos")
def productos():

    productos = [
        {
            "nombre": "Monitoreo GPS",
            "descripcion": "Seguimiento de vehículos en tiempo real.",
            "categoria": "Monitoreo"
        },
        {
            "nombre": "Control de rutas",
            "descripcion": "Seguimiento de rutas y recorridos.",
            "categoria": "Logística"
        },
        {
            "nombre": "Alertas de seguridad",
            "descripcion": "Notificaciones para eventos importantes.",
            "categoria": "Seguridad"
        }
    ]

    return render_template(
        "productos.html",
        productos=productos
    )


@app.route("/clientes")
def clientes():

    clientes = [
        {
            "nombre": "Empresa ABC",
            "correo": "empresaabc@gmail.com",
            "telefono": "0991111111"
        },
        {
            "nombre": "Transportes Costa",
            "correo": "transportescosta@gmail.com",
            "telefono": "0982222222"
        },
        {
            "nombre": "Logística Peninsular",
            "correo": "logisticapeninsular@gmail.com",
            "telefono": "0973333333"
        }
    ]

    return render_template(
        "clientes.html",
        clientes=clientes
    )


@app.route("/proveedores")
def proveedores():

    proveedores = [
        {
            "empresa": "GPS Ecuador",
            "servicio": "Equipos GPS",
            "telefono": "0961111111"
        },
        {
            "empresa": "Seguridad Vehicular",
            "servicio": "Sistemas de seguridad",
            "telefono": "0952222222"
        },
        {
            "empresa": "Tecnología Logística",
            "servicio": "Software de monitoreo",
            "telefono": "0943333333"
        }
    ]

    return render_template(
        "proveedores.html",
        proveedores=proveedores
    )


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


if __name__ == "__main__":
    app.run(debug=True)
