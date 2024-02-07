document.addEventListener("DOMContentLoaded", function() {

    document.querySelectorAll('.cell').forEach(cell => {
        cell.addEventListener('click', function() {
            const cellId = this.id;
            fetch('/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({cell_id: cellId})
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    // Update the board in the frontend based on response
                    console.log('Move successful', data);
                } else {
                    // Handle errors or invalid moves
                    console.error('Move failed', data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
    
});
