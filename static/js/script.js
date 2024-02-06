document.addEventListener('DOMContentLoaded', (event) => {

    // Get the submit and reset button elements
    var submitButton = document.querySelector('#settings-form input[type="submit"]');
    var resetButton = document.getElementById('reset-button');

    // Get a corner
    var elements = ['cell-0', 'cell-2', 'cell-6', 'cell-8'];
    var randomIndex = Math.floor(Math.random() * elements.length); // Generate a random index
    var chosenElement = elements[randomIndex]; // Use the random index to pick an element
    var cell = document.getElementById(chosenElement); // mark that corner

    // Add a click event listener to the submit button
    submitButton.addEventListener('click', function(event) {

        // Prevent the form from being submitted in the traditional way
        event.preventDefault();

        // Get the selected mark (X or O)
        var selectedMark = document.querySelector('input[name="player1"]:checked').value;

        // First, make a request to the /usr route to get the user's data (X or O)
        fetch('/usr', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }, 
            body: JSON.stringify({ mark: selectedMark, cell: chosenElement }),
        })
        .then(response => response.json())
        .then(data => {console.log(data);})

        if (selectedMark === 'O') {
            // Add 'X' to the cell element
            cell.textContent = 'X';

            // Apply the .x-mark CSS class
            cell.classList.add('x-mark');

            // Disable the submit button
            submitButton.disabled = true;
        }
        else{
            // Disable the submit button
            submitButton.disabled = true;            
        }

    });

    // Add a click event listener to the reset button
    resetButton.addEventListener('click', function() {
        // Enable the submit button
        submitButton.disabled = false;
    });

    // Add a click event listener to the reset button
    resetButton.addEventListener('click', function() {
        // Make a request to the /reset route to reset the game state
        fetch('/reset', {
            method: 'POST',
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);

            // Refresh the page
            location.reload();
        });
    });

    // Add a click event listener to each cell
    var cells = document.querySelectorAll('.cell');
    for (var i = 0; i < cells.length; i++) {
        cells[i].addEventListener('click', function() {
            var cellId = this.id;

            fetch('/usrmove', {  // Changed route to '/main.py'
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ id: cellId }),
            })
            .then(response => response.json())
            .then(data => {
                var mark = data.mark;
                this.innerHTML = mark;
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

    document.querySelectorAll('.cell').forEach(cell => {
        cell.addEventListener('click', function() {
            if(this.innerHTML !== '') return; // Prevent marking an already marked cell
            
            // Fetch request to get the next move from the server
            fetch('/pcmove', {
                method: 'GET',  // Changed to GET if no data is sent to the server
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Use the 'data' from the server to update the UI
                let cell = document.getElementById(data.html_id);
                if(cell.innerHTML === '') {
                    cell.innerHTML = data.mark;
                    cell.classList.add(data.style);
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        });
    });
});