<<<<<<< HEAD
# Proyecto Final — Adivina mi Dibujo

Este proyecto implementa un sistema de Inteligencia Artificial basado en Redes Convolucionales (CNN) que predice en tiempo real qué objeto está siendo dibujado por el usuario en un lienzo interactivo, se aplica los conceptos recibidos en clase sobre regresión lineal, redes neuronales profundas, CNN y Transfer Learning.

## Objetivo General

Diseñar, entrenar y desplegar un modelo CNN capaz de clasificar dibujos en tiempo real entre 5 categorías distintas, mostrando las tres predicciones más probables con su nivel de confianza


## Contexto del Proyecto

- Limitaciones de la **regresión lineal**.  
- las **redes neuronales profundas**.  
- Implementación de modelos en **Python con Keras**.  
- Construcción de **Redes Convolucionales (CNN)** y aplicación de **Transfer Learning** para clasificación de imágenes.

Este proyecto aplica conocimientos en un entorno real y tangible, demostrando el funcionamiento del modelo en tiempo real.
desde google colab: https://colab.research.google.com/drive/17DiiSN2G8GBUt43VYAjjl6sXrssD0wkx?usp=sharing

## Requisitos Técnicos
•	Python 3.10+
•	TensorFlow / Keras
•	Flask
•	NumPy
•	OpenCV
•	Quick, Draw! Dataset (subconjunto de 5 categorías)

## Instalación de dependencias:
Ejecución del Proyecto
Clonar el repositorio: https://github.com/dataister5-Elibueno/AdivinaMiDibujo_EvaP2.git
Activa el entorno virtual:   venv\Scripts\activate
Ejecuta la aplicación: python app.py
Abre el navegador en: http://127.0.0.1:5000


## Uso de Librerías y Entorno

1. Activar entorno virtual:
   ```bash
   venv\Scripts\activate

## Funcionamiento
•	El usuario dibuja con el mouse en el lienzo (canvas).
•	El sistema captura el dibujo y lo envía al modelo CNN. predecir
•	Se muestran las tres predicciones más probables con su porcentaje de confianza. esatdistica
•	La interfaz puede mover el resultado según el nivel de certeza.

# Arquitectura del Modelo
•	Conv2D (32 filtros, kernel 3x3)
•	MaxPooling2D (2x2)
•	Conv2D (64 filtros)
•	Flatten + Dense (128 neuronas, ReLU)
•	Dense final (Softmax, 5 clases) Entrenado con optimizador Adam, pérdida categorical_crossentropy, y 20 épocas.
# Métricas
•	Accuracy de validación: 82%
•  Matriz de confusión arroja errores frecuentes en dibujos incompletos o con trazos similares y muestra confusión entre gato_carro y casa_arbol, lo que evidencia áreas de mejora

# Link Video : https://ister-my.sharepoint.com/:v:/g/personal/bety_bueno_ister_edu_ec/IQDIOkNijmPdT4keQpQTrfDBAYXZbeT_-i-3s1o2sMjFdI8?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=Aelxok

Autor: Elisabeth Bueno
Ister Proyecto individual
=======
# AdivinaMiDibujo_EvaP2
Evaluacion del P2 asignatura Introduccion a la Inteligencia Artificial
>>>>>>> 6088d25ad622f1da2340672375a3c88acabd98ff
