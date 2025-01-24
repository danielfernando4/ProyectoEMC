document.addEventListener('DOMContentLoaded', function() {
    const menuItems = document.querySelectorAll('.menu ul li');

    menuItems.forEach(item => {
        // Al hacer clic en un <li>, se activa
        item.addEventListener('click', function() {
            // Primero eliminamos la clase 'active' de todos los elementos
            menuItems.forEach(i => i.classList.remove('active'));

            // Añadimos la clase 'active' al elemento actual
            item.classList.add('active');
        });
    });
});