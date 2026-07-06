const formulario = document.getElementById("formProducto");

const nombre = document.getElementById("nombre");
const descripcion = document.getElementById("descripcion");
const categoria = document.getElementById("categoria");

const lista = document.getElementById("listaProductos");
const mensaje = document.getElementById("mensaje");
const total = document.getElementById("total");

let contador = 0;

// Validar placa
function validarNombre() {

    if (nombre.value.trim().length < 3) {

        nombre.classList.add("is-invalid");
        nombre.classList.remove("is-valid");

        document.getElementById("errorNombre").textContent =
            "La placa debe tener al menos 3 caracteres.";

        return false;
    }

    nombre.classList.remove("is-invalid");
    nombre.classList.add("is-valid");

    document.getElementById("errorNombre").textContent = "";

    return true;
}

// Validar descripción
function validarDescripcion() {

    if (descripcion.value.trim().length < 10) {

        descripcion.classList.add("is-invalid");
        descripcion.classList.remove("is-valid");

        document.getElementById("errorDescripcion").textContent =
            "La descripción debe contener al menos 10 caracteres.";

        return false;
    }

    descripcion.classList.remove("is-invalid");
    descripcion.classList.add("is-valid");

    document.getElementById("errorDescripcion").textContent = "";

    return true;
}

// Validar categoría
function validarCategoria() {

    if (categoria.value === "") {

        categoria.classList.add("is-invalid");
        categoria.classList.remove("is-valid");

        document.getElementById("errorCategoria").textContent =
            "Seleccione un tipo de vehículo.";

        return false;
    }

    categoria.classList.remove("is-invalid");
    categoria.classList.add("is-valid");

    document.getElementById("errorCategoria").textContent = "";

    return true;
}

// Eventos en tiempo real
nombre.addEventListener("input", validarNombre);
nombre.addEventListener("blur", validarNombre);

descripcion.addEventListener("input", validarDescripcion);
descripcion.addEventListener("blur", validarDescripcion);

categoria.addEventListener("change", validarCategoria);

// Registrar vehículo
formulario.addEventListener("submit", function (e) {

    e.preventDefault();

    const nombreValido = validarNombre();
    const descripcionValida = validarDescripcion();
    const categoriaValida = validarCategoria();

    if (!(nombreValido && descripcionValida && categoriaValida)) {

        mensaje.innerHTML =
            "<div class='alert alert-danger'>Corrija los errores antes de registrar el vehículo.</div>";

        return;
    }

    mensaje.innerHTML =
        "<div class='alert alert-success'>Vehículo registrado correctamente.</div>";

    const tarjeta = document.createElement("div");

    tarjeta.className = "card p-3 mt-3 shadow";

    tarjeta.innerHTML = `
        <h4>${nombre.value}</h4>

        <p><strong>Descripción:</strong> ${descripcion.value}</p>

        <p><strong>Tipo:</strong> ${categoria.value}</p>

        <button class="btn btn-danger eliminar">
            Eliminar
        </button>
    `;

    lista.appendChild(tarjeta);

    contador++;

    total.textContent = contador;

    formulario.reset();

    nombre.classList.remove("is-valid");
    descripcion.classList.remove("is-valid");
    categoria.classList.remove("is-valid");

    tarjeta.querySelector(".eliminar").addEventListener("click", function () {

        tarjeta.remove();

        contador--;

        total.textContent = contador;

    });

});
