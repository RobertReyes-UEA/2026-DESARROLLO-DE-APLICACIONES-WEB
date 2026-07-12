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
let vehiculos = [];
   function renderizarVehiculos(){

    lista.innerHTML = "";

    if(vehiculos.length === 0){

        lista.innerHTML = `
        <div class="alert alert-warning">
            No existen vehículos registrados.
        </div>
        `;

        total.textContent = 0;

        return;

    }

    vehiculos.forEach((vehiculo, indice)=>{

        const card = document.createElement("div");

        card.className="card p-3 mt-3 shadow";

        card.innerHTML=`

        <h4>${vehiculo.placa}</h4>

        <p><strong>Descripción:</strong> ${vehiculo.descripcion}</p>

        <p><strong>Tipo:</strong> ${vehiculo.tipo}</p>

        <button class="btn btn-danger eliminar">
            Eliminar
        </button>

        `;

        card.querySelector(".eliminar").addEventListener("click",function(){

            vehiculos.splice(indice,1);

            renderizarVehiculos();

        });

        lista.appendChild(card);

    });

    total.textContent = vehiculos.length;

vehiculos.push({

    placa:nombre.value,

    descripcion:descripcion.value,

    tipo:categoria.value

});

renderizarVehiculos();

formulario.reset();
