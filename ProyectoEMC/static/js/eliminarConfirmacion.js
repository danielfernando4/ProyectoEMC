let formToSubmit = null; 

function mostrarModal(event, form) {
    event.preventDefault(); 
    formToSubmit = form; 
    document.getElementById("confirmModal").style.display = "flex";
}


function cerrarModal() {
    document.getElementById("confirmModal").style.display = "none";
}


function confirmarEliminacion() {
    if (formToSubmit) {
        formToSubmit.submit(); 
    }
    cerrarModal();
}

document.getElementById("confirmButton").addEventListener("click", confirmarEliminacion);
document.getElementById("cancelButton").addEventListener("click", cerrarModal);
