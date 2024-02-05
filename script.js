// Select all cells
var cells = document.querySelectorAll('.cell');

// Loop through each cell
for (var i = 0; i < cells.length; i++) {
    // Add click event listener to each cell
    cells[i].addEventListener('click', function() {
        // Do something when cell is clicked
        alert('Cell clicked!');
    });
}