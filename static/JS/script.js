const url = "http://127.0.0.1:5000/"

// FUNCION PARA REDIRECCIONAR AL HOME DE LA PAGINA
function home(){
    location.href = "index.html"
}

// FUNCION PARA DIRECIONAR A LA INFORMACION DEL POSTRE NAPOLEON
function Information_napoleon() {
    location.href="info_napoleon.html"
}


function submit_enter(){
    document.addEventListener("keydown", function (event) {
        if (event.key == "Enter"){
            fetch(url)
            .then(response => {
                console.log("Estado "+ response.status + "HTTP")
                return response.json()
            }).then(postre => {
                resumen_compra(postre)
            }).catch(error => {
                console.error(error)
            })
        }
    })
}

function resumen_compra(postre){
    var cantidad = document.getElementById("contador").value;
    const precio = postre.precio
    const precio_productos = document.getElementById("precio_productos").innerText = "$ " + (precio*cantidad) + " COL"
    const total = document.getElementById("total").innerText = "$ " + ((precio*cantidad)+5000) + " COL"
}