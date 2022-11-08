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
        
    let createCard = (t_id) => {
        let new_card = document.createElement('div');
        new_card.id = t_id
        new_card.className = "card mb-2 shadow-sm"
        
        let new_card_content = '<li class="list-group-item py-0 border-0 d-flex justify-content-between align-items-center">' +
    	    	'<div class="pretty p-icon p-toggle p-plain px-1">' +
                    '<input class="form-check-input me-1" type="checkbox" value="" aria-label="...">' +
                    '<div class="state p-off">' +
                        '<i class="bi bi-circle"></i>' +
                    '</div>' +
                    '<div class="state p-on">' +
                        '<i class="bi bi-check-circle-fill"></i>' +
                    '</div>' +
                '</div>' +
                '<div class="card-body lh-sm px-0"></div>' +
                '<button type="button" class="btn btn-sm close-btn px-2"><i class="bi bi-x-lg"></i></button>' +
            '</li>'
        
        new_card.innerHTML = new_card_content;
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