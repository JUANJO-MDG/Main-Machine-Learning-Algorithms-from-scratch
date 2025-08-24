# 🚀 Modelo K-Nearest Neighbors (KNN) Desde Cero para la Clasificación de Flores Iris

Este proyecto es una implementación completa y didáctica de un modelo de **K-Nearest Neighbors (KNN)** construido desde cero, utilizando únicamente la biblioteca NumPy. El objetivo es proporcionar un entendimiento profundo de cómo funciona este algoritmo de clasificación, aplicándolo al problema clásico de la clasificación de las especies de la flor Iris.

El proyecto abarca todas las etapas del ciclo de vida del aprendizaje automático: desde el análisis exploratorio de datos (EDA) y el preprocesamiento, hasta la implementación de un clasificador personalizado, el entrenamiento, la predicción y la evaluación exhaustiva del rendimiento.

---

## 📂 Estructura del Repositorio

- **`IRIS.csv`**: El conjunto de datos original, que contiene registros de diferentes especies de flores Iris.
- **`knn.ipynb`**: Un notebook de Jupyter con la implementación del modelo KNN, el entrenamiento y la evaluación del modelo.
- **`README.md`**: El archivo que estás leyendo, con toda la información sobre el proyecto.

---

## 🔬 Análisis Exploratorio de Datos (EDA)

Antes de construir el modelo, se realizó un análisis exploratorio de datos para comprender mejor las variables y su relación. Los pasos clave incluyeron:

1.  **Carga y Vista Previa**: Se cargó el archivo `IRIS.csv` en un DataFrame de pandas y se inspeccionaron las primeras filas para verificar la estructura.
2.  **Análisis de Correlación**: Se generó un mapa de calor (`heatmap`) para visualizar la matriz de correlación entre todas las variables. Esto permitió identificar las características con una alta correlación con la variable objetivo (`species`).

---

## 🛠️ Metodología y Componentes del Modelo

### 1. Preprocesamiento y Preparación de Datos

Se realizó un preprocesamiento riguroso para asegurar la calidad y la robustez del modelo. Los pasos clave fueron:

* **Definición de Variables**: Se seleccionaron las siguientes características (`X`) como variables predictoras: `sepal_length`, `sepal_width`, `petal_length`, y `petal_width`. La variable objetivo (`y`) fue `species`.
* **División de Datos**: Los datos se dividieron en un conjunto de entrenamiento (80%) y uno de prueba (20%) utilizando `train_test_split`.

### 2. Implementación de la Clase `KNNeightborsClasifier`

La clase **`KNNeightborsClasifier`** fue construida de forma modular, implementando cada componente necesario para el algoritmo.

* **Constructor (`__init__`)**: Inicializa el número de vecinos (`k`), la métrica de distancia y el tipo de tarea (`classification` o `regression`).
* **Función de Distancia (`_distance`)**: Implementa el cálculo de distancias. Se incluyen la distancia **Euclídea** y la distancia de **Manhattan**, lo que permite una mayor flexibilidad en la experimentación.
* **Método de Entrenamiento (`fit`)**: Un método simple que almacena los datos de entrenamiento en la clase para su uso posterior en la fase de predicción.
* **Método de Predicción (`predict`)**: Para cada punto de prueba, el método encuentra sus `k` vecinos más cercanos en el conjunto de entrenamiento, determina la clase más común entre ellos y asigna esa clase como la predicción final.
* **Métodos de Evaluación (`evaluate_classification`) o (`evaluate_regression`)**: Un método versátil que calcula y muestra métricas de rendimiento tanto para **clasificación** (Accuracy, Precision, Recall, F1-Score, Matriz de Confusión) como para **regresión** (MSE, MAE).
* **Visualización (`plot_predictions`)**: Un método para visualizar las predicciones del modelo en un gráfico de dispersión, lo que ayuda a entender el comportamiento del clasificador en un espacio de 2D.

---

## 📊 Resultados y Evaluación del Modelo

El modelo se entrenó con los datos de Iris, y la evaluación en el conjunto de prueba arrojó las siguientes métricas, demostrando un rendimiento excelente:

* **Accuracy (Precisión)**: Un valor de precisión muy alto, indicando que el modelo clasificó correctamente la gran mayoría de las instancias.
* **Precision (Precisión)**: De todas las predicciones positivas, la mayoría fueron correctas, lo que muestra un bajo número de falsos positivos.
* **Recall (Sensibilidad)**: El modelo fue capaz de identificar la mayoría de las instancias positivas, lo que minimiza los falsos negativos.
* **F1 Score**: Un valor alto que demuestra un buen equilibrio entre la precisión y el recall.

### Matriz de Confusión

La matriz de confusión proporciona una visión detallada de los resultados del modelo, mostrando la cantidad de predicciones correctas e incorrectas para cada clase, lo cual es fundamental para el análisis de los errores del modelo.

---

## 🚀 Conclusión

El modelo KNN implementado desde cero demostró ser un clasificador robusto y efectivo para el conjunto de datos de Iris. Este proyecto no solo cumple su función de clasificar las especies de flores, sino que también sirve como una excelente herramienta de aprendizaje para comprender los fundamentos de uno de los algoritmos de aprendizaje automático más intuitivos y populares.

---

## 🛠️ Requisitos de Instalación

Para ejecutar este proyecto, necesitarás instalar los `requirements.txt`:

```bash
pip install -r requirements.txt