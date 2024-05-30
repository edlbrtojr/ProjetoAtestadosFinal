// static/js/inicio.js

document.addEventListener('DOMContentLoaded', function() {
    const items = document.querySelectorAll('li');
    items.forEach(item => {
        item.addEventListener('click', () => {
            items.forEach(i => i.classList.remove('highlight'));
            item.classList.add('highlight');
        });
    });
});

// CSS para o destaque
li.highlight {
    background-color: #4caf50 !important;
    color: white;
}
