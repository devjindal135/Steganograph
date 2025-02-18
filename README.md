# Steganography

Steganography is a Flask-based web application that allows users to encrypt and decrypt secret messages within images using pixel manipulation. The application features a futuristic cyberpunk-themed UI built with Tailwind CSS.

## Features
- **Encrypt Messages**: Hide secret messages inside images.
- **Decrypt Messages**: Retrieve hidden messages from encrypted images.
- **Password Protection**: Ensure security with a password requirement.

## Technologies Used
- **Flask** (Backend)
- **OpenCV** (Image Processing)
- **HTML, CSS, JavaScript** (Frontend)
- **Tailwind CSS & Bootstrap Icons** (Styling)

## Installation
### Prerequisites
- Python 3.x
- Flask
- OpenCV (`cv2`)

### Setup
```bash
git clone https://github.com/devjindal135/Stenograph.git
cd steganography
pip install flask opencv-python numpy
python app.py
```

Open `http://127.0.0.1:5000/` in your browser.

## Usage
### Encryption
1. Upload an image.
2. Enter a secret message and a password.
3. Click "ENCRYPT" to generate the encrypted image.
4. Download the encrypted image for sharing.

### Decryption
1. Upload the encrypted image.
2. Enter the correct password.
3. Click "DECRYPT" to reveal the hidden message.

## Deployment
This application can be deployed on platforms like Vercel, Heroku, or any Flask-compatible hosting service. Ensure `static/uploads` is writable and properly configured.
for review:
```
https://github.com/devjindal135/Stenography
```

## Author
Dev Jindal - Steganography

## Future Enhancements
- AES-based additional encryption for enhanced security.
- Improved error handling and UI feedback.
- Support for different image formats.

Feel free to contribute or suggest improvements!