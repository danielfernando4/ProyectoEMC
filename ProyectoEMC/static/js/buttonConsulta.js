function setActiveButton(button, id) {
    const buttons = document.querySelectorAll('.custom-button');
    buttons.forEach(btn => btn.classList.remove('active'));
    button.classList.add('active');
    localStorage.setItem('activeButton', id);
}

document.addEventListener('DOMContentLoaded', (event) => {
    const activeButtonId = localStorage.getItem('activeButton');
    if (activeButtonId) {
        const activeButton = document.getElementById(activeButtonId);
        if (activeButton) {
            activeButton.classList.add('active');
        }
    } else {
        document.getElementById('boton2').classList.add('active');
    }
});
