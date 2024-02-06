document.addEventListener('DOMContentLoaded', (event) => {
    fetch('/usrmove', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ id: cellId }), // Assuming cellId is defined elsewhere
    })
    .then(response => response.json())
    .then(data => {
        const { mark, html_id, style } = data; // Destructuring for cleaner access

        // Get the element with the id from html_id
        const element = document.getElementById(html_id);
        if (element) { // Check if element exists to avoid null errors
            // Set the text content to mark
            element.textContent = mark;

            // Add the CSS class from style
            element.classList.add(style);
        } else {
            console.error('Element not found for html_id:', html_id);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
})