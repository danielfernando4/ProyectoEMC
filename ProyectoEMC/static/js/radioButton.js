document.querySelectorAll('input[name="radio"]').forEach(radio => {
    radio.addEventListener('change', function() {
        const form = document.getElementById('myForm');
        const accionInput = document.getElementById('accionInput');
        const selectedValue = document.querySelector('input[name="radio"]:checked').value;

        // Remover las clases de todos los labels
        document.querySelectorAll('label').forEach(label => {
            label.classList.remove('selected-label');
        });

        // Agregar la clase al label seleccionado
        const selectedLabel = this.closest('label');
        selectedLabel.classList.add('selected-label');

        // Configurar la acción basado en el valor seleccionado
        if (selectedValue === 'locales') {
            form.action = "/catalogo-main";
            accionInput.value = "consultar_locales"; // Definir acción
            form.method = "GET"; // Usar GET para locales
            form.submit(); // Enviar formulario automáticamente
        } else if (selectedValue === 'generales') {
            form.action = "/catalogo-main";
            accionInput.value = "consultar_oficinas"; // Definir acción
            form.method = "POST"; // Usar POST para generales
            form.submit(); // Enviar formulario automáticamente
        }

        console.log("Selected value:", selectedValue);
        console.log("Accion:", accionInput.value);
        console.log("Form action:", form.action);
        console.log("Form method:", form.method);
        form.submit();
    });
});
