const handleImage = (e) => {
    var reader = new FileReader();
    input_canvas.getContext('2d').clearRect(0, 0, input_canvas.width, input_canvas.height);
    hiddenCanvas.getContext('2d').clearRect(0, 0, hiddenCanvas.width, hiddenCanvas.height);
    reader.onload = function(event){
        var img = new Image();
        img.onload = () => {
            hiddenCanvas.width = img.width;
            hiddenCanvas.height = img.height;
            ctxHiddenCanvas.drawImage(img,0,0);
            putFromOneCanvasToAnother(hiddenCanvas, input_canvas)
            const el = document.querySelector('#download-btn')
            el.parentNode.replaceChild(el.cloneNode(true), el);
        }
        img.src = event.target.result;
    }
    reader.readAsDataURL(e.target.files[0]);
}

const imageLoader = document.getElementById('imageLoader');
imageLoader.addEventListener('change', handleImage, false);

var input_canvas = document.querySelector('#input-canvas');
input_canvas.width = input_canvas.clientWidth;
input_canvas.height = input_canvas.clientHeight;

const result_canvas = document.querySelector('#result-canvas');
result_canvas.width = result_canvas.clientWidth;
result_canvas.height = result_canvas.clientHeight;

const hiddenCanvas = document.querySelector('#hidden-canvas');
const ctxHiddenCanvas = hiddenCanvas.getContext('2d');

const putFromOneCanvasToAnother = (origin_canvas, destination_canvas) => {
    const width = origin_canvas.width
    const height = origin_canvas.height
    const ctx = destination_canvas.getContext('2d');
    if(width > height){
        let new_height = destination_canvas.width*(height/width)
        ctx.drawImage(origin_canvas, 0, 0, width, height, 0, (destination_canvas.height-new_height)/2, destination_canvas.width, new_height)
    }
    else if(width < height){
        let new_width = destination_canvas.height*(width/height)
        ctx.drawImage(origin_canvas, 0, 0, width, height, (destination_canvas.width-new_width)/2, 0, new_width, destination_canvas.height)
    }
    else{
        ctx.drawImage(origin_canvas, 0, 0, width, height, 0, 0, destination_canvas.width, destination_canvas.height)
    }
}

const downloadCanvasAsImage = (filename) => {

    let canvasImage = hiddenCanvas.toDataURL('image/png');
    
    let xhr = new XMLHttpRequest();
    xhr.responseType = 'blob';
    xhr.onload = function () {
        let a = document.createElement('a');
        a.href = window.URL.createObjectURL(xhr.response);
        a.download = filename;
        a.style.display = 'none';
        document.body.appendChild(a);
        a.click();
        a.remove();
    };
    xhr.open('GET', canvasImage); // This is to download the canvas Image
    xhr.send();
    notify('Make sure you copy your decryption hash. You will need it!')
}

const handleClick = () => {
    const formData = new FormData()
    formData.append('img', imageLoader.files[0])
    notify('Image is being processed. This may take a few minutes, so please wait <3')
    let baseURL = 'https://imcrypt.onrender.com'
    let endpoint = ''
    if(checkbox.checked) {endpoint = '/decrypt'; formData.append('hash', hash_el_input.value)}
    else {endpoint = '/encrypt'}
    axios.post(baseURL+endpoint, formData)
        .then(res => (res.data))
        .then((temp) => {
            img = temp.img
            const width = img[0].length
            const height = img.length
            aspect_ratio = height/width
            data = []
            for(let row of img){
                for(let col of row){
                    data.push(col[0])
                    data.push(col[1])
                    data.push(col[2])
                    data.push(255)
                }
            }
            data = new Uint8ClampedArray(data);
            data = new ImageData(data, width);
            hiddenCanvas.width = width;
            hiddenCanvas.height = height;
            ctxHiddenCanvas.putImageData(data, 0, 0);
            putFromOneCanvasToAnother(hiddenCanvas, result_canvas);
            if(temp.hash) hash_el_display.value = temp.hash;
            else hash_el_display.value = '';
            document.querySelector('#download-btn').addEventListener('click', () => handleDownload(temp.filename));
        })
        .catch(err => notify(err, true))
}

const handleDownload = (filename) => {
    downloadCanvasAsImage(filename)
}

document.querySelector('#convert').addEventListener('click', handleClick);