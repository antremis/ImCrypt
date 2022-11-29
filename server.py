from flask import Flask, request, jsonify, make_response, send_file
from flask_cors import CORS
import numpy as np
from ImageEncryption import encrypt, decrypt
from PIL import Image

app = Flask(__name__)
CORS(app)

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'false')
    return response

@app.route("/api/encrypt", methods = ['POST'])
def encryptImage():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    elif request.method == "POST":
        if 'img' not in request.files:
            return jsonify({"message" : "Please send image with the tag of 'img'"}), 400
        img = request.files['img']
        filename = img.filename
        if filename == '':
            return jsonify({"message" : "No Image Selected"}), 400
        filetype = img.filename.split('.')[-1]
        if filetype not in ['jpg', 'png', 'wfif', 'jpeg']:
            return jsonify({"message" : "Image type not supported"}), 400
        
        img = np.array(Image.open(img.stream).convert('L'))
        enc_img, hash = encrypt(img)
        return jsonify({"message" : "Encrypted", 'img':enc_img, 'hash':hash, "filename" : f'encrypted_{filename}'}), 200
    else :
        return jsonify({"message" : "Unsupported Request Method"}), 405

@app.route('/api/decrypt', methods=['POST'])
def decryptImage():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    elif request.method == "POST":
        if 'img' not in request.files:
            return jsonify({"message" : "Please send image with the tag of 'img'"}), 400
        img = request.files['img']
        filename = img.filename
        if filename == '':
            return jsonify({"message" : "No Image Selected"}), 400
        filetype = img.filename.split('.')[-1]
        if filetype not in ['jpg', 'png', 'wfif', 'jpeg']:
            return jsonify({"message" : "Image type not supported"}), 400
        
        if 'hash' not in request.form:
            return jsonify({"message" : "Please send hash with the tag of 'hash'"}), 400

        hash = request.form['hash']
        img = np.array(Image.open(img.stream).convert('L'))
        dec_img = decrypt(img, hash)
        return jsonify({"message" : "Decrypted", 'img':dec_img, "filename" : f'decrypted_{filename}'}), 200
    else :
        return jsonify({"message" : "Unsupported Request Method"}), 405
    
if __name__ == '__main__':
    app.run(debug=True)