from flask import Flask, request, render_template, redirect, url_for
import face_recognition
import cv2
import os
import numpy as np

app = Flask(__name__)

# Directory to store registered faces
FACE_DIR = "static/images/"

# Ensure the directory exists
if not os.path.exists(FACE_DIR):
    os.makedirs(FACE_DIR)

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    # Get the image data from the request
    img_data = request.form['imgData']
    img_data = img_data.split(",")[1]
    img_data = np.fromstring(base64.b64decode(img_data), np.uint8)
    img = cv2.imdecode(img_data, cv2.IMREAD_COLOR)

    # Get the student's name
    student_name = request.form['student_name']

    # Save the image
    face_path = os.path.join(FACE_DIR, f"{student_name}.jpg")
    cv2.imwrite(face_path, img)

    return "Registration successful!", 200

@app.route('/verify', methods=['POST'])
def verify():
    # Get the image data from the request
    img_data = request.form['imgData']
    img_data = img_data.split(",")[1]
    img_data = np.fromstring(base64.b64decode(img_data), np.uint8)
    input_img = cv2.imdecode(img_data, cv2.IMREAD_COLOR)

    # Load the known faces
    known_faces = []
    known_names = []

    for filename in os.listdir(FACE_DIR):
        if filename.endswith('.jpg'):
            image = face_recognition.load_image_file(os.path.join(FACE_DIR, filename))
            encoding = face_recognition.face_encodings(image)[0]
            known_faces.append(encoding)
            known_names.append(filename.split(".")[0])

    # Encode the input image
    input_encoding = face_recognition.face_encodings(input_img)

    if len(input_encoding) > 0:
        results = face_recognition.compare_faces(known_faces, input_encoding[0])
        for i, match in enumerate(results):
            if match:
                return f"Access granted to {known_names[i]}!", 200

    return "Access denied!", 403

if __name__ == '__main__':
    app.run(debug=True)
