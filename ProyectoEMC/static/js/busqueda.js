document.getElementById('searchInput').addEventListener('keyup', function() {
    const searchValue = this.value.toLowerCase();
    const rows = document.querySelectorAll('#clientesTable tbody tr');

    rows.forEach(row => {
        const idCell = row.querySelector('td').textContent.toLowerCase();
        if (idCell.includes(searchValue)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
});