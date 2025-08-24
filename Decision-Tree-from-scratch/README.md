# 🌳 Modelo de Árbol de Decisión para el Diagnóstico de Cáncer de Pulmón

Este proyecto es una implementación de un modelo con el algoritmo de **Árboles de Decisión** hecho desde cero. Para predecir el diagnóstico de cáncer de pulmón a partir de datos de encuestas. El objetivo es crear un clasificador robusto y evaluar su rendimiento en una tarea crucial de diagnóstico médico.

El notebook cubre todo el flujo de trabajo de Machine Learning: desde la carga y el preprocesamiento de los datos, hasta el entrenamiento del modelo y la evaluación de su desempeño a través de métricas clave y una matriz de confusión.

---

## 🔬 Análisis Exploratorio de Datos (EDA) y Preprocesamiento

Antes de construir el modelo, se realizó un análisis inicial de los datos y un preprocesamiento esencial. Los pasos clave incluyeron:

1.  **Carga y Vista Previa de Datos**: El archivo `survey lung cancer.csv` fue cargado en un DataFrame de pandas para una inspección inicial de las variables.
2.  **Mapeo de Variables Categóricas**: Las variables `GENDER` (`M`, `F`) y `LUNG_CANCER` (`YES`, `NO`) fueron convertidas a un formato numérico (1, 0) para su uso en el modelo.
3.  **Análisis de la Estructura de Datos**: Se utilizó `df.info()` para confirmar que no había valores nulos y que todos los tipos de datos eran correctos para el análisis.

---

## 🛠️ Metodología y Componentes del Modelo

### 1. Preparación de Datos

Se realizó una preparación rigurosa para entrenar el modelo de forma correcta. Los pasos clave fueron:

- **Definición de Variables**: Se seleccionaron todas las columnas, excepto la última (`LUNG_CANCER`), como variables predictoras (`X`). La variable objetivo (`y`) fue `LUNG_CANCER`.
- **División de Datos**: Los datos se dividieron en un conjunto de entrenamiento (80%) y un conjunto de prueba (20%). Se fijó una semilla aleatoria (`random_state=4`) para garantizar la reproducibilidad del experimento.

### 2. Implementación del Modelo `DecisionTreeClassifier`

El modelo de **Árbol de Decisión** se implementó utilizando la clase `DecisionTreeClassifier` hecha desde cero. Los hiperparámetros del modelo fueron configurados de la siguiente manera:

- **`max_depth=5`**: La profundidad máxima del árbol se limitó a 5 para evitar el sobreajuste y mantener el modelo interpretable.
- **`min_samples_split=2`**: El número mínimo de muestras requeridas para dividir un nodo interno se estableció en 2.

---

## 📊 Resultados y Evaluación del Modelo

El modelo entrenado demostró un rendimiento notable en la clasificación del diagnóstico de cáncer de pulmón. La evaluación en el conjunto de prueba arrojó las siguientes métricas:

- **Accuracy (Precisión): 90.32%**: El modelo predijo correctamente el diagnóstico el 90.32% de las veces.
- **Precision (Precisión): 94.64%**: De todos los casos que el modelo predijo como positivos, el 94.64% eran realmente positivos.
- **F1 Score: 0.9464**: Este valor indica un excelente equilibrio entre la precisión y el recall del modelo.

### Matriz de Confusión

La matriz de confusión ofrece una visión detallada del rendimiento del modelo:

```
[[ 5  3]
[ 3 51]]
```

- **Verdaderos Negativos (TN = 5)**: El modelo predijo correctamente que 5 pacientes no tenían cáncer.
- **Falsos Positivos (FP = 3)**: El modelo predijo incorrectamente que 3 pacientes tenían cáncer.
- **Falsos Negativos (FN = 3)**: El modelo predijo incorrectamente que 3 pacientes no tenían cáncer.
- **Verdaderos Positivos (TP = 51)**: El modelo predijo correctamente que 51 pacientes sí tenían cáncer.

---

## 🚀 Conclusión

El modelo de Árbol de Decisión implementado demostró ser una solución efectiva para la tarea de diagnóstico de cáncer de pulmón. El alto rendimiento en las métricas de evaluación indica que el modelo es confiable para esta tarea de clasificación. Este proyecto sirve como un ejemplo claro de cómo se puede utilizar un modelo de árbol de decisión para resolver un problema de clasificación en el ámbito de la salud.

---

## 🛠️ Requisitos de Instalación

Para ejecutar este proyecto, necesitarás los requerimientos:

```bash
pip install -r requirements.txt
```
