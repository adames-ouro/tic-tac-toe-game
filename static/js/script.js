document.addEventListener('DOMContentLoaded', function() {
    const settingsForm = document.getElementById('settings-form');
    const resetButton = document.getElementById('reset-button');
    const formVisibilityFlag = 'formVisibility';

    // Check if the form should be hidden on page load
    if (sessionStorage.getItem(formVisibilityFlag) === 'hidden') {
        settingsForm.style.display = 'none';
    }

    // Hide form on submit and set flag
    settingsForm.addEventListener('submit', function() {
        settingsForm.style.display = 'none';
        sessionStorage.setItem(formVisibilityFlag, 'hidden');
    });


    resetButton.addEventListener('click', function() {

        const cells = document.querySelectorAll('.cell');
        cells.forEach(function(cell) {
            cell.innerHTML = ''; // Clear the cell content
            // If you're using classes to indicate a mark (e.g., 'x-mark' or 'o-mark'), remove those classes
            cell.classList.remove('x-mark', 'o-mark');
        });

        document.getElementById('settings-form').style.display = 'block';
        // Make an AJAX call to reset the game state on the server first
        fetch('/reset', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                // Include CSRF token header if needed for your setup
            },
        })
        .then(response => response.json())
        .then(data => {
            console.log('Game reset:', data);
            // After successfully resetting the server state, clear sessionStorage and reload the page
            sessionStorage.removeItem(formVisibilityFlag);

            
            window.location.reload();
        })
        .catch((error) => {
            console.error('Error:', error);
            // Optionally handle the error state here
        });
    });

    var cells = document.querySelectorAll('.cell');
    for (var i = 0; i < cells.length; i++) {
        cells[i].addEventListener('click', function() {
            var cell_id = this.id;

            fetch('/player-move', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ cell_id: cell_id }),
            })
            .then(response => response.json())
            .then(data => {
                var selected_mark = data.selected_mark;
                this.innerHTML = selected_mark;
                if (selected_mark === 'X') {
                   this.classList.add('x-mark');
                } else if (selected_mark === 'O') {
                    this.classList.add('o-mark');
                }

                // Automatically update the board with PC's move
                var pcCellId = data.pc_cell;
                var pcSelectedMark = data.pc_mark;
                var pcCell = document.getElementById(pcCellId);

                if (pcCellId && pcSelectedMark) {
                    var pcCell = document.getElementById(pcCellId);
                    if (pcCell) {
                        pcCell.innerHTML = pcSelectedMark;
                        if (pcSelectedMark === 'X') {
                            pcCell.classList.add('x-mark');
                        } else if (pcSelectedMark === 'O') {
                            pcCell.classList.add('o-mark');
                        }
                    }
                } else {
                    // Handle scenario when PC has no move (e.g., game is over or board is full)
                    console.log("No move possible for PC or game over");
                }

            })
            .catch((error) => {
                console.error('Error:', error);
            });
        });
    }

});
