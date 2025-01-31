document.querySelectorAll('.search__input').forEach(input => {
    input.addEventListener('keyup', function() {
        console.log('Keyup event triggered'); // Depuración
        const searchValue = this.value.toLowerCase();
        let tableId;

        if (this.id === 'searchInputClientes') {
            tableId = 'clientesTable';
        } else if (this.id === 'searchInputContratos') {
            tableId = 'contratosTable';
        } else if (this.id === 'searchInputCatalogo') {
            tableId = 'catalogoTable';
        } else if (this.id === 'searchInputEmpleados') {
            tableId = 'empleadosTable';
        } else if (this.id === 'searchInputOficinas') {         
            tableId = 'oficinaTable';
        } else if (this.id === 'searchInputProveedores') {
            tableId = 'proveedoresTable';
        } else if (this.id === 'searchInputServicios') {    
            tableId = 'serviciosTable';
        }

        const rows = document.querySelectorAll(`#${tableId} tbody tr`);

        console.log(`Searching in ${tableId} for: ${searchValue}`); // Depuración

        rows.forEach(row => {
            const cells = row.querySelectorAll('td');
            let found = false;

            cells.forEach(cell => {
                if (cell.textContent.toLowerCase().includes(searchValue)) {
                    found = true;
                }
            });

            if (found) {
                row.style.display = '';
                console.log(`Found match in row: ${row.innerHTML}`); // Depuración
            } else {
                row.style.display = 'none';
            }
        });
    });
});
