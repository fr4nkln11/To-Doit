document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.btn-close').forEach(button => {
        button.onclick = () => {
            const request = new XMLHttpRequest();
            request.open('POST', `/delete/${button.id}`);
            request.onload = () => {
                const entry = document.querySelector(`div[id="${button.id}"]`);
                document.querySelector('.list-group').removeChild(entry);
            }; 
            request.send();
        };
    });
});

document.querySelector('#add_task').addEventListener('click', () => {
    const new_entry = document.querySelector('#new_entry').value;
    
    const request = new XMLHttpRequest();
    request.open('POST', `/create/${new_entry}`);
    request.onload = () => {
        const response = request.responseText;
        alert(response)
    }
    request.send();
});
