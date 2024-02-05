document.addEventListener('DOMContentLoaded', (event) => {
    // Select all cells
    var cells = document.querySelectorAll('.cell');

    // Loop through each cell
    for (var i = 0; i < cells.length; i++) {
        // Add click event listener to each cell
        cells[i].addEventListener('click', function() {
            // Add 'X' to the clicked cell
            this.innerHTML = 'X';
        });
    }
});