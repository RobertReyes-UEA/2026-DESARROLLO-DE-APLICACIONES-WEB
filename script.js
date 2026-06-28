const formulario = document.getElementById("formProducto");

const lista = document.getElementById("listaProductos");

const mensaje = document.getElementById("mensaje");

const total = document.getElementById("total");

let contador = 0;

formulario.addEventListener("submit", function(event){

event.preventDefault();

const nombre = document.getElementById("nombre").value.trim();

const descripcion = document.getElementById("descripcion").value.trim();

const categoria = document.getElementById("categoria").value;

if(nombre==="" || descripcion==="" || categoria===""){

mensaje.innerHTML="<div class='alert alert-danger'>Complete todos los campos.</div>";

return;

}

mensaje.innerHTML="<div class='alert alert-success'>Producto registrado correctamente.</div>";

const tarjeta=document.createElement("div");

tarjeta.className="card p-3 m-3";

tarjeta.innerHTML=`
<h5>${nombre}</h5>

<p>${descripcion}</p>

<p><strong>Categoría:</strong> ${categoria}</p>

<button class="btn btn-danger eliminar">
Eliminar
</button>
`;

lista.appendChild(tarjeta);

contador++;

total.textContent=contador;

formulario.reset();

tarjeta.querySelector(".eliminar").addEventListener("click",function(){

tarjeta.remove();

contador--;

total.textContent=contador;

});

});
