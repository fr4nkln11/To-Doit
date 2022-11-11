let update_badge = () => {
    let count = document.querySelectorAll('.card').length;
    if(count == 1){
        document.querySelector('.badge').innerHTML = `${count} task`;
    }else{
        document.querySelector('.badge').innerHTML = `${count} tasks`;
    };
};

let card_delete = (task_id) => {
    
    fetch('/delete',{
        headers: {
            'Content-Type':'application/json'
        },
        method: 'POST',
        body: JSON.stringify({
            'task_id': task_id
        }),
    }).then(() => {
        document.querySelector(`div[id="${task_id}"]`).remove();
        update_badge();
    });
};

document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.close-btn').forEach(button => {
        button.onclick = () => {card_delete(button.id)};
    });
    update_badge();
});

document.querySelector('#add_task').addEventListener('submit', () => {
    event.preventDefault();
    const new_task = document.querySelector('#task_input').value;
        
    async function createCard(t_id){
        let new_card = document.createElement('div');
        new_card.id = t_id
        new_card.className = "card mb-2 shadow-sm"
        
        await fetch('/create').then((response) => {
            return response.text();
        }).then((html) => {
            new_card.innerHTML = html
        });
        
        new_card.children[0].children[1].innerHTML = new_task
        new_card.children[0].children[2].id = t_id
        
        document.querySelector('.list-group').prepend(new_card);
        update_badge();
        new_card.children[0].children[2].onclick = () => {card_delete(t_id);};
        
    };
    
    fetch('/create',{
        headers: {
            'Content-Type':'application/json'
        },
        method: 'POST',
        body: JSON.stringify({
            'new_task': new_task
        }),
    }).then((response) => {
        return response.text();
    }).then((id) => {
        createCard(id)
    });
    
    document.querySelector('#task_input').value = '';
});