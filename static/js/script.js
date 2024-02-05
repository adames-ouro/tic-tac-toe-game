document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('settings-form').addEventListener('submit', function(event) {
        event.preventDefault();

        var selectedMark = document.querySelector('input[name="player1"]:checked').value;

        fetch('/main.py', {  // Changed route to '/main.py'
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ mark: selectedMark , board: { row: 1, col: 1, value: 'X' } }),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            document.getElementById('grid').classList.remove('disabled');
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });



    var cells = document.querySelectorAll('.cell');

    for (var i = 0; i < cells.length; i++) {
        cells[i].addEventListener('click', function() {
            var cellId = this.id;

            fetch('/main.py', {  // Changed route to '/main.py'
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
});