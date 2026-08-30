import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical

# Cargar datos desde modeloColab
X = np.load("modeloColab/quickdraw_dataset.npy")
y = np.load("modeloColab/quickdraw_labels.npy")

# Normalizar imágenes
X = X / 255.0
X = X.reshape(-1, 28, 28, 1)
y = to_categorical(y)

# Crear modelo CNN
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D((2,2)),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(y.shape[1], activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=10, batch_size=64, validation_split=0.2)
model.save("adivina_mi_dibujo.h5")
