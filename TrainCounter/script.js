const count_el = document.getElementById('counter');
count_el.innerText = 0;

function increment() {
    const count_el = document.getElementById('counter');
    let count = parseInt(count_el.innerText) + 1;
    count_el.innerText = count;
}

function reset() {
    const count_el = document.getElementById('counter');
    count_el.innerText = 0;
}