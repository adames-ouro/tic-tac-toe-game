// get user mark
document.addEventListener('DOMContentLoaded', (event) => {
    // Add event listener to the settings form
    document.getElementById('settings-form').addEventListener('submit', function(event) {

        // Prevent the default form submission
        event.preventDefault();

        // Get the selected mark (X or O)
        var selectedMark = document.querySelector('input[name="player1"]:checked').value;

        if (selectedMark === 'O') {
            // First, make a request to the /usr route to get the user's data (X or O)
            fetch('/usr', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ mark: selectedMark }),
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);

                // Get the a corner
                var elements = ['cell-0', 'cell-2', 'cell-6', 'cell-8'];
                var randomIndex = Math.floor(Math.random() * elements.length); // Generate a random index
                var chosenElement = elements[randomIndex]; // Use the random index to pick an element
                var cell = document.getElementById(chosenElement); // mark that conrner

                // Get the submit and reset button elements
                var submitButton = document.querySelector('#settings-form input[type="submit"]');
                var resetButton = document.getElementById('reset-button');

                // Add a click event listener to the submit button
                submitButton.addEventListener('click', function(event) {
                    // Prevent the form from being submitted in the traditional way
                    event.preventDefault();

                    // Add 'X' to the cell element
                    cell.textContent = 'X';
            
                    // Apply the .x-mark CSS class to the cell-4 element
                    cell.classList.add('x-mark');

                    // Disable the submit button
                    submitButton.disabled = true;
                });

                // Add a click event listener to the reset button
                resetButton.addEventListener('click', function() {
                    // Enable the submit button
                    submitButton.disabled = false;
                });

            });
            }
    });
});


// Add a click event listener to the reset button
document.addEventListener('DOMContentLoaded', (event) => {
    // Get the reset button element
    var resetButton = document.getElementById('reset-button');
    resetButton.addEventListener('click', function() {
        // Make a request to the /reset route to reset the game state
        fetch('/reset', {
            method: 'POST',
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);

            // Get all the cells
            var cells = document.querySelectorAll('.cell');

            // Loop through each cell
            for (var i = 0; i < cells.length; i++) {
                // Clear the text content of the cell
                cells[i].textContent = '';

                // Remove the .x-mark class from the cell
                cells[i].classList.remove('x-mark');
            }
            // Get the radio buttons
            var radioButtons = document.querySelectorAll('#settings-form input[type="radio"]');

            // Loop through each radio button
            for (var i = 0; i < radioButtons.length; i++) {
                // Remove the checked value from the radio button
                radioButtons[i].checked = false;
            }
        });
    });
});
