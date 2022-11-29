const checkbox = document.querySelector('#toggle');
const toggle = document.querySelector('.toggle');
const hash_el_display = document.querySelector('#display-hash');
const hash_el_input = document.querySelector('#input-hash');
const notice = document.querySelector('#notice');

const notify = (text, isError) => {
    if(isError) notice.classList.add('error');
    notice.innerHTML = text;
    setTimeout(() => {
        notice.innerHTML = '';
        notice.classList.remove('error');
    }, 5000);
}

checkbox.addEventListener('click', () => {
    toggle.classList.toggle('switch');
    hash_el_display.classList.toggle('hidden');
    hash_el_input.classList.toggle('hidden');
    input_canvas.getContext('2d').clearRect(0, 0, input_canvas.width, input_canvas.height);
    result_canvas.getContext('2d').clearRect(0, 0, result_canvas.width, result_canvas.height);
    hiddenCanvas.getContext('2d').clearRect(0, 0, hiddenCanvas.width, hiddenCanvas.height);
})

hash_el_display.addEventListener('click', () => {
    navigator.clipboard.writeText(hash_el_display.value);
    notify('Copied!')
})