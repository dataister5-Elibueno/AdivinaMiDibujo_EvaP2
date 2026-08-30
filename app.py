from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import base64

app = Flask(__name__)

# Verificar versión cargada
print(f"TensorFlow: {tf.__version__}")

# Cargar modelo
model = tf.keras.models.load_model(
    "modelos/adivina_mi_dibujo.h5",
    compile=False
)

class_names = ["apple", "car", "cat", "house", "tree"]

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    try:
        # Obtener imagen enviada desde JavaScript
        data = request.json['image']

        # Decodificar base64
        image_bytes = base64.b64decode(data.split(',')[1])

        # Procesar imagen
        img = (
            Image.open(io.BytesIO(image_bytes))
            .convert('L')
            .resize((28, 28))
        )

        # Convertir a array
        img_array = np.array(img, dtype=np.float32) / 255.0

        # Dar formato esperado por el modelo
        img_array = img_array.reshape(1, 28, 28, 1)

        # Predicción
        prediction = model.predict(img_array, verbose=0)[0]

        # Top 3 resultados
        top5 = np.argsort(prediction)[-5:][::-1]

        result = [
            {
                "class_id": int(i),
                "label": class_names[i],
                "confidence": round(float(prediction[i]), 4),
                "percentage": round(float(prediction[i]) * 100, 2)
            }
            for i in top5
        ]

        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True)