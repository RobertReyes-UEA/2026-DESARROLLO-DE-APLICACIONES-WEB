const formulario = document.getElementById("formProducto");
const lista = document.getElementById("listaProductos");
const mensaje = document.getElementById("mensaje");
const total = document.getElementById("total");

let contador = 0;

formulario.addEventListener("submit", function (e) {

    e.preventDefault();

    const nombre = document.getElementById("nombre").value.trim();
    const descripcion = document.getElementById("descripcion").value.trim();
    const categoria = document.getElementById("categoria").value;

    if (nombre === "" || descripcion === "" || categoria === "") {

        mensaje.innerHTML =
            `<div class="alert alert-danger">
                Todos los campos son obligatorios.
            </div>`;

        return;
    }

    mensaje.innerHTML =
        `<div class="alert alert-success">
            Producto registrado correctamente.
        </div>`;

    const card = document.createElement("div");

    card.className = "card shadow p-3 mb-3";

    card.innerHTML = `

        <div class="card-body">

            <h4 class="card-title text-primary">${nombre}</h4>

            <p class="card-text">
                <strong>Descripción:</strong>
                ${descripcion}
            </p>

            <p>
                <strong>Categoría:</strong>
                ${categoria}
            </p>

            <button class="btn btn-danger eliminar">
                Eliminar
            </button>

        </div>

    `;

    lista.appendChild(card);

    contador++;

    total.textContent = contador;

    formulario.reset();

    card.querySelector(".eliminar").addEventListener("click", function () {

        card.remove();

        contador--;

        total.textContent = contador;

    });

});
