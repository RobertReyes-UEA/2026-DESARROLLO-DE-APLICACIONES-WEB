const formulario = document.getElementById("formProducto");

const nombre = document.getElementById("nombre");
const descripcion = document.getElementById("descripcion");
const categoria = document.getElementById("categoria");

const lista = document.getElementById("listaProductos");
const mensaje = document.getElementById("mensaje");
const total = document.getElementById("total");

const spinner = document.getElementById("spinner");

let vehiculos = [];

/* ===========================
   VALIDACIONES
=========================== */

function validarNombre() {

    if (nombre.value.trim().length < 3) {

        nombre.classList.add("is-invalid");
        nombre.classList.remove("is-valid");

        errorNombre.textContent =
            "La placa debe tener al menos 3 caracteres.";

        return false;
    }

    nombre.classList.remove("is-invalid");
    nombre.classList.add("is-valid");

    errorNombre.textContent = "";

    return true;
}

function validarDescripcion() {

    if (descripcion.value.trim().length < 10) {

        descripcion.classList.add("is-invalid");
        descripcion.classList.remove("is-valid");

        errorDescripcion.textContent =
            "La descripción debe contener mínimo 10 caracteres.";

        return false;
    }

    descripcion.classList.remove("is-invalid");
    descripcion.classList.add("is-valid");

    errorDescripcion.textContent = "";

    return true;
}

function validarCategoria() {

    if (categoria.value == "") {

        categoria.classList.add("is-invalid");
        categoria.classList.remove("is-valid");

        errorCategoria.textContent =
            "Seleccione un tipo de vehículo.";

        return false;
    }

    categoria.classList.remove("is-invalid");
    categoria.classList.add("is-valid");

    errorCategoria.textContent = "";

    return true;
}

/* ===========================
   EVENTOS
=========================== */

nombre.addEventListener("input", validarNombre);
nombre.addEventListener("blur", validarNombre);

descripcion.addEventListener("input", validarDescripcion);
descripcion.addEventListener("blur", validarDescripcion);

categoria.addEventListener("change", validarCategoria);

/* ===========================
   RENDERIZAR VEHÍCULOS
=========================== */

function renderizarVehiculos() {

    lista.innerHTML = "";

    if (vehiculos.length === 0) {

        lista.innerHTML = `
        <div class="alert alert-warning">
            No existen vehículos registrados.
        </div>`;

        total.textContent = 0;

        return;
    }

    vehiculos.forEach((vehiculo, indice) => {

        const columna = document.createElement("div");

        columna.className = "col-md-4 mb-3";

        columna.innerHTML = `

        <div class="card shadow h-100">

            <div class="card-body">

                <h5 class="card-title">
                    ${vehiculo.placa}
                </h5>

                <p class="card-text">
                    <strong>Descripción:</strong><br>
                    ${vehiculo.descripcion}
                </p>

                <p>
                    <strong>Tipo:</strong>
                    ${vehiculo.tipo}
                </p>

                <button class="btn btn-danger eliminar">
                    Eliminar
                </button>

            </div>

        </div>

        `;

        columna.querySelector(".eliminar").addEventListener("click", function () {

            vehiculos.splice(indice, 1);

            renderizarVehiculos();

        });

        lista.appendChild(columna);

    });

    total.textContent = vehiculos.length;

}

/* ===========================
   REGISTRAR
=========================== */

formulario.addEventListener("submit", function (e) {

    e.preventDefault();

    if (!(validarNombre() && validarDescripcion() && validarCategoria())) {

        mensaje.innerHTML = `
        <div class="alert alert-danger">
            Corrija los errores antes de continuar.
        </div>`;

        return;
    }

    spinner.style.display = "block";

    setTimeout(() => {

        vehiculos.push({

            placa: nombre.value,

            descripcion: descripcion.value,

            tipo: categoria.value

        });

        spinner.style.display = "none";

        mensaje.innerHTML = `
        <div class="alert alert-success">
            Vehículo registrado correctamente.
        </div>`;

        renderizarVehiculos();

        formulario.reset();

        nombre.classList.remove("is-valid");
        descripcion.classList.remove("is-valid");
        categoria.classList.remove("is-valid");

    }, 1000);

});
