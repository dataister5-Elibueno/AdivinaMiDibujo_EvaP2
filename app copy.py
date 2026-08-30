from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import base64

app = Flask(__name__)
model = tf.keras.models.load_model("modelos/adivina_mi_dibujo.h5")

class_names = ["gato", "perro", "avion", "casa", "arbol"]


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['image']
    image_bytes = base64.b64decode(data.split(',')[1])
    img = Image.open(io.BytesIO(image_bytes)).convert('L').resize((28, 28))
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1) 
    prediction = model.predict(img_array)[0]
    top3 = np.argsort(prediction)[-3:][::-1]
    result = [{"label": int(i), "confidence": float(prediction[i])} for i in top3]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
