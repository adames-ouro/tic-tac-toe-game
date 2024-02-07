document.addEventListener("DOMContentLoaded", function() {
    // Reference to the reset button
    const resetButton = document.getElementById('reset-button');

    resetButton.addEventListener('click', function(e) {
        e.preventDefault(); // Prevent any default action

        // Send an AJAX request to reset the game
        fetch('/reset', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});
