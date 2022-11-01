document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.close_button').forEach(button => {
        button.onclick = () => {
            const request = new XMLHttpRequest();
            request.open('POST', `/delete/${button.id}`);
            request.onload = () => {
                const entry = document.querySelector(`li[id="${button.id}"]`);
                document.querySelector('.list-group').removeChild(entry);
            }; 
            request.send();
        };
    });
});
