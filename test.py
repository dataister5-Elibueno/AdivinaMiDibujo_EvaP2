import numpy as np
import tensorflow as tf

# Cargar dataset
data = np.load("data/quickdraw_dataset.npy")
labels = np.load("data/quickdraw_labels.npy")

print("Dataset cargado correctamente:")
print("Shape de data:", data.shape)
print("Shape de labels:", labels.shape)

# Cargar modelo entrenado
model = tf.keras.models.load_model("model/adivina_mi_dibujo.h5")
print("Modelo cargado correctamente.")
