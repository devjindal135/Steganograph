from flask import Flask, request, jsonify, send_from_directory
import os
import cv2
import numpy as np

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# XOR encryption function
def xor_encrypt(message, password):
    return [ord(c) ^ ord(password[i % len(password)]) for i, c in enumerate(message)]

# XOR decryption function
def xor_decrypt(encrypted_values, password):
    return "".join(chr(c ^ ord(password[i % len(password)])) for i, c in enumerate(encrypted_values))

# Encrypt message into image
def encrypt_image(img_path, message, password):
    img = cv2.imread(img_path)
    height, width, _ = img.shape
    max_length = height * width * 3  # Max characters we can store

    encrypted_message = xor_encrypt(message + "##END##", password)

    if len(encrypted_message) > max_length:
        return None  # Message too long

    m, n, z = 0, 0, 0
    for value in encrypted_message:
        img[n, m, z] = value  # Store encrypted ASCII value
        n = (n + 1) % height
        m = (m + 1) % width
        z = (z + 1) % 3

    encrypted_path = os.path.join(UPLOAD_FOLDER, 'encrypted.png')
    cv2.imwrite(encrypted_path, img)
    return encrypted_path

# Decrypt message from image
def decrypt_image(img_path, password):
    img = cv2.imread(img_path)
    height, width, _ = img.shape
    encrypted_values = []
    max_length = height * width * 3  # Prevent infinite loop

    m, n, z = 0, 0, 0
    for _ in range(max_length):  # Limit extraction to prevent infinite loop
        value = img[n, m, z]
        encrypted_values.append(value)  # Retrieve stored ASCII value

        n = (n + 1) % height
        m = (m + 1) % width
        z = (z + 1) % 3

        # Attempt to decrypt and check for ending
        decrypted_message = xor_decrypt(encrypted_values, password)
        if decrypted_message.endswith("##END##"):
            return decrypted_message.replace("##END##", "")

    return None  # If no valid message is found, assume incorrect password

@app.route("/")
def index():
    return send_from_directory('static', 'index.html')

@app.route("/encrypt", methods=["POST"])
def encrypt():
    file = request.files['image']
    password = request.form['password']
    message = request.form['message']

    img_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(img_path)

    encrypted_img_path = encrypt_image(img_path, message, password)

    if encrypted_img_path:
        return jsonify({"success": True, "image_url": f"/{encrypted_img_path}"})
    return jsonify({"success": False, "error": "Message too long!"})

@app.route("/decrypt", methods=["POST"])
def decrypt():
    file = request.files['image']
    password = request.form['password']
    
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(img_path)

    message = decrypt_image(img_path, password)

    if message is None:
        return jsonify({"success": True, "error": "Incorrect password!"})

    return jsonify({"success": True, "message": message})

if __name__ == "__main__":
    app.run(debug=True)
