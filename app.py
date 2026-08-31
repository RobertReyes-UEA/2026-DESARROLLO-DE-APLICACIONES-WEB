from flask import Flask, render_template, redirect, url_for, flash

from forms.producto_form import ProductoForm
from forms.cliente_form import ClienteForm
from forms.proveedor_form import ProveedorForm
from forms.facturacion_form import FacturacionForm


app = Flask(__name__)

# Clave secreta para Flask-WTF y protección CSRF
app.config["SECRET_KEY"] = "clave-secreta-sistema-logistico-2026"


# ==============================
# DATOS DEMOSTRATIVOS
# ==============================

productos = [
    {
        "nombre": "Monitoreo GPS",
        "descripcion": "Seguimiento de vehículos en tiempo real.",
        "categoria": "Monitoreo",
        "precio": 50.00
    },
    {
        "nombre": "Sistema de Seguridad",
        "descripcion": "Control y alertas para unidades de transporte.",
        "categoria": "Seguridad",
        "precio": 75.00
    }
]

clientes = [
    {
        "nombre": "Cervecería Nacional",
        "correo": "cliente@empresa.com",
        "telefono": "0991234567"
    }
]

proveedores = [
    {
        "empresa": "GPS Ecuador",
        "contacto": "Carlos Pérez",
        "correo": "ventas@gpsecuador.com"
    }
]

facturas = [
    {
        "cliente": "Cervecería Nacional",
        "concepto": "Servicio de monitoreo",
        "total": 150.00,
        "estado": "Pagada"
    }
]


# ==============================
# INICIO
# ==============================

@app.route("/")
def inicio():
    return render_template(
        "index.html",
        nombre_sistema="Sistema Logístico de Monitoreo"
    )


# ==============================
# PRODUCTOS
# ==============================

@app.route("/productos", methods=["GET", "POST"])
def productos_ruta():

    form = ProductoForm()

    if form.validate_on_submit():

        nuevo_producto = {
            "nombre": form.nombre.data,
            "descripcion": form.descripcion.data,
            "categoria": form.categoria.data,
            "precio": form.precio.data
        }

        productos.append(nuevo_producto)

        flash(
            "Producto registrado correctamente.",
            "success"
        )

        return redirect(url_for("productos_ruta"))

    return render_template(
        "productos.html",
        productos=productos,
        form=form
    )


# ==============================
# CLIENTES
# ==============================

@app.route("/clientes", methods=["GET", "POST"])
def clientes_ruta():

    form = ClienteForm()

    if form.validate_on_submit():

        nuevo_cliente = {
            "nombre": form.nombre.data,
            "correo": form.correo.data,
            "telefono": form.telefono.data,
            "direccion": form.direccion.data
        }

        clientes.append(nuevo_cliente)

        flash(
            "Cliente registrado correctamente.",
            "success"
        )

        return redirect(url_for("clientes_ruta"))

    return render_template(
        "clientes.html",
        clientes=clientes,
        form=form
    )


# ==============================
# PROVEEDORES
# ==============================

@app.route("/proveedores", methods=["GET", "POST"])
def proveedores_ruta():

    form = ProveedorForm()

    if form.validate_on_submit():

        nuevo_proveedor = {
            "empresa": form.empresa.data,
            "contacto": form.contacto.data,
            "correo": form.correo.data,
            "telefono": form.telefono.data,
            "direccion": form.direccion.data
        }

        proveedores.append(nuevo_proveedor)

        flash(
            "Proveedor registrado correctamente.",
            "success"
        )

        return redirect(url_for("proveedores_ruta"))

    return render_template(
        "proveedores.html",
        proveedores=proveedores,
        form=form
    )


# ==============================
# FACTURACIÓN
# ==============================

@app.route("/facturacion", methods=["GET", "POST"])
def facturacion_ruta():

    form = FacturacionForm()

    if form.validate_on_submit():

        nueva_factura = {
            "cliente": form.cliente.data,
            "concepto": form.concepto.data,
            "total": form.total.data,
            "estado": form.estado.data
        }

        facturas.append(nueva_factura)

        flash(
            "Factura registrada correctamente.",
            "success"
        )

        return redirect(url_for("facturacion_ruta"))

    return render_template(
        "facturacion.html",
        facturas=facturas,
        form=form
    )


# ==============================
# EJECUTAR APLICACIÓN
# ==============================

if __name__ == "__main__":
    app.run(debug=True)
