import tensorflow as tf

# Cargar el modelo
model = tf.keras.models.load_model("modelos/adivina_mi_dibujo.h5")


model.summary()
