document.addEventListener('DOMContentLoaded', (event) => {
    // Get selected mark from html form
    document.getElementById('settings-form').addEventListener('submit', function(event) {
        event.preventDefault();

        var selectedMark = document.querySelector('input[name="player1"]:checked').value;

        fetch('/endpoint', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ mark: selectedMark }),
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error('Error:', error);
        });
    });

    // Select all cells
    var cells = document.querySelectorAll('.cell');

    // Loop through each cell
    for (var i = 0; i < cells.length; i++) {
        // Add click event listener to each cell
        cells[i].addEventListener('click', function() {
            // Get cell id
            var cellId = this.id;

            // Send cell id to Python script
            fetch('main.py', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ id: cellId }),
            })
            .then(response => response.json())
            .then(data => {
                
                // Get the mark from the response
                var mark = data.mark;

                // Do something with the mark
                this.innerHTML = mark;

                // Add class to cell based on mark
                if (mark === 'X') {
                    this.classList.add('x-mark');
                } else if (mark === 'O') {
                    this.classList.add('o-mark');
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        });
    }
});