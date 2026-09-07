```python
from flask import Flask, render_template, redirect, url_for, flash
from forms.producto_form import ProductoForm
import sqlite3
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = "sistema-logistico-2026"


# ==========================================
# CONFIGURACIÓN DE BASE DE DATOS
# ==========================================

DATABASE = os.path.join("data", "ferreteria.db")


def obtener_conexion():
    os.makedirs("data", exist_ok=True)
    conexion = sqlite3.connect(DATABASE)
    conexion.row_factory = sqlite3.Row
    return conexion


# ==========================================
# CREAR TABLA PRODUCTOS
# ==========================================

def inicializar_base_datos():

    conexion = obtener_conexion()

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()


# ==========================================
# INICIO
# ==========================================

@app.route("/")
def index():
    return render_template("index.html")


# ==========================================
# PRODUCTOS
# ==========================================

@app.route("/productos", methods=["GET", "POST"])
def productos():

    form = ProductoForm()

    if form.validate_on_submit():

        conexion = obtener_conexion()

        conexion.execute("""
            INSERT INTO productos
            (nombre, descripcion, categoria, precio)
            VALUES (?, ?, ?, ?)
        """, (
            form.nombre.data,
            form.descripcion.data,
            form.categoria.data,
            form.precio.data
        ))

        conexion.commit()
        conexion.close()

        flash("Producto registrado correctamente.", "success")

        return redirect(url_for("productos"))

    conexion = obtener_conexion()

    productos = conexion.execute("""
        SELECT * FROM productos
        ORDER BY id DESC
    """).fetchall()

    conexion.close()

    return render_template(
        "productos.html",
        form=form,
        productos=productos
    )


# ==========================================
# CLIENTES
# ==========================================

@app.route("/clientes")
def clientes():
    return render_template("clientes.html")


# ==========================================
# PROVEEDORES
# ==========================================

@app.route("/proveedores")
def proveedores():
    return render_template("proveedores.html")


# ==========================================
# FACTURACIÓN
# ==========================================

@app.route("/facturacion")
def facturacion():
    return render_template("facturacion.html")


# ==========================================
# EJECUCIÓN
# ==========================================

if __name__ == "__main__":

    inicializar_base_datos()

    app.run(debug=True)
```
