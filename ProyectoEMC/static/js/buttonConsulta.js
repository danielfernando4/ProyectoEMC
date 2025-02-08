function setActiveButton(button, id) {
    const buttons = document.querySelectorAll('.custom-button');
    buttons.forEach(btn => btn.classList.remove('active'));
    button.classList.add('active');

    const pageKey = `activeButton_${window.location.pathname}`;
    localStorage.setItem(pageKey, id);
}

document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.custom-button');
    buttons.forEach(btn => btn.classList.remove('active'));

    const pageKey = `activeButton_${window.location.pathname}`;
    let activeButtonId = localStorage.getItem(pageKey);

    if (!activeButtonId) {
        activeButtonId = 'boton2'; 
        localStorage.setItem(pageKey, 'boton2');
    }

    const activeButton = document.getElementById(activeButtonId);
    if (activeButton) {
        activeButton.classList.add('active');

        const formId = `form-${activeButtonId}`;
        const form = document.getElementById(formId);
        if (form) {
            form.submit();
        }
    }
});
