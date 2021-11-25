
function logIn(){
    nuevoCorreo = document.getElementById("correo").value
    if (nuevoCorreo.match('@tecnico.cl')){  
        window.location.href = "/tecnico" }
    else  if (nuevoCorreo.match('@chef.cl')){
        window.location.href = "/chef"
    }
    else if (nuevoCorreo.match('@administrador.cl')){
        window.location.href = "/administrador"
    }

}