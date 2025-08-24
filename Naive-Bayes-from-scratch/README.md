"""

# 🎓 Implementación de Naive Bayes para Clasificación Categórica

Este proyecto es una implementación **completa y didáctica** del algoritmo de clasificación **Naive Bayes** desde cero, utilizando la librería `pandas` para la manipulación de datos. A diferencia de las librerías de alto nivel como `scikit-learn`, esta implementación se centra en construir el modelo paso a paso para comprender a fondo sus principios matemáticos y la lógica de la programación.

El proyecto abarca la teoría fundamental del Teorema de Bayes y su suposición de "ingenuidad", y luego la traduce directamente en código funcional, incluyendo una técnica esencial para la robustez del modelo: el **suavizado de Laplace**.

---

## 🛠️ Metodología y Componentes del Modelo

El núcleo del proyecto es la clase `NaiveBayesClassifier`, diseñada para ser **modular, intuitiva y robusta**.

### 1. Implementación de la Clase `NaiveBayesClassifier`

La clase `NaiveBayesClassifier` se compone de métodos clave para el entrenamiento y la predicción:

- **Inicialización (`__init__`)** Define los atributos principales del modelo:
  - `alpha`: El parámetro de suavizado de Laplace, que evita probabilidades de cero.
  - `priors`: Un diccionario para almacenar las probabilidades a priori de cada clase.
  - `conditionals`: Un diccionario anidado para almacenar las probabilidades condicionales de cada característica.

---

### 2. Fases del Entrenamiento (`fit`)

El método `fit` es responsable de entrenar el modelo. Para ello, llama a dos funciones internas que calculan las probabilidades del dataset de entrenamiento:

- **Cálculo de Probabilidades a Priori (`_calculate_priors`)** Calcula la probabilidad base de cada clase, es decir, la frecuencia de cada clase en el conjunto de datos de entrenamiento.

- **Cálculo de Probabilidades Condicionales (`_calculate_conditionals`)** Calcula la probabilidad de que cada valor de característica ocurra, dado cada una de las clases. Aquí es donde se aplica la suposición de independencia de Naive Bayes. Además, se implementa el **suavizado de Laplace** para manejar valores no vistos, lo que asegura que ninguna probabilidad sea exactamente cero y evita errores de predicción.

---

### 3. Predicción (`predict`)

El método `predict` utiliza las probabilidades aprendidas para clasificar una nueva instancia:

1.  **Multiplicación de Probabilidades:** Para cada clase, el método multiplica la probabilidad a priori de la clase por las probabilidades condicionales de todas las características de la nueva instancia.
2.  **Selección de la Clase:** La clase con la probabilidad resultante más alta es seleccionada como la predicción final.

---

## 📊 Resultados y Evaluación del Modelo

- El clasificador aprende las relaciones entre las características categóricas y la clase de manera eficiente.
- El uso de `pandas` facilita el preprocesamiento de datos y el cálculo de las probabilidades.
- El suavizado de Laplace asegura que el modelo pueda hacer predicciones correctas incluso si la nueva instancia contiene un valor que no se vio durante el entrenamiento.

Ejemplo de resultado:

- **Nueva Instancia**: `{'outlook': 'overcast', 'temp': 'hot', 'humidity': 'normal'}`
- **Probabilidad Posterior**: `{'yes': 0.0426, 'no': 0.0047}`
- **Clase Predicha**: `yes`

---

## 🚀 Conclusión

Este proyecto demuestra que es posible implementar un algoritmo de machine learning robusto como Naive Bayes con conocimientos fundamentales de programación y estadística. Comprender los componentes internos de este modelo es crucial para cualquier científico de datos o ingeniero de machine learning, ya que ofrece una visión clara de cómo los datos se transforman en conocimiento predictivo.

---

## 🛠️ Requisitos de Instalación

Para ejecutar este proyecto, instala los `requirements.txt`:

```bash
pip install -r requirements.txt
```
