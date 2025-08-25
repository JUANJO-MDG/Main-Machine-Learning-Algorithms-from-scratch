# 🚀 Modelo de Regresión Logística Desde Cero para el Diagnóstico de Cáncer de Mama

Este proyecto es una implementación completa y didáctica de un modelo de **Regresión Logística** construido desde cero, sin el uso de librerías de Machine Learning de alto nivel como scikit-learn para el algoritmo central. El objetivo es proporcionar un entendimiento profundo de cómo funciona este algoritmo de clasificación, aplicándolo al problema crucial del diagnóstico de cáncer de mama.

El proyecto abarca todas las etapas del ciclo de vida del aprendizaje automático: desde el análisis exploratorio de datos y el preprocesamiento, hasta el entrenamiento, la visualización de la convergencia y la evaluación exhaustiva del rendimiento del modelo.

---

## 🔬 Análisis Exploratorio de Datos (EDA)

Antes de construir el modelo, se realizó un análisis exploratorio de datos para comprender mejor las variables y su relación. Los pasos clave incluyeron:

1.  **Carga y Vista Previa**: Se cargó el archivo `Breast_cancer_data.csv` en un DataFrame de pandas y se inspeccionaron las primeras filas para verificar la estructura.
2.  **Análisis de Correlación**: Se generó un mapa de calor (`heatmap`) para visualizar la matriz de correlación entre todas las variables. Esto permitió identificar las características con una alta correlación con la variable objetivo (`diagnosis`).
3.  **Visualización de la Distribución**: Se crearon gráficos de caja (`boxplots`) para cada característica con el fin de examinar la distribución de los datos, identificar la presencia de valores atípicos (outliers) y entender la variabilidad de cada variable.

---

## 🛠️ Metodología y Componentes del Modelo

### 1. Preprocesamiento y Preparación de Datos

Se realizó un preprocesamiento riguroso para asegurar la calidad y la robustez del modelo. Los pasos clave fueron:

- **Definición de Variables**: Se seleccionaron las siguientes características (`X`) como variables predictoras: `mean_radius`, `mean_texture`, `mean_perimeter`, `mean_area` y `mean_smoothness`. La variable objetivo (`y`) fue `diagnosis` (donde `0` = benigno, `1` = maligno).
- **División de Datos**: Los datos se dividieron en un conjunto de entrenamiento (70%) y uno de prueba (30%) utilizando `train_test_split`. Una semilla aleatoria (`random_state=42`) se fijó para garantizar la reproducibilidad de la división.
- **Estandarización de Características**: Se aplicó `StandardScaler` para estandarizar las características de entrada. Este paso es fundamental para los modelos basados en descenso de gradiente, ya que las variables con diferentes escalas pueden afectar la convergencia del algoritmo.

### 2. Implementación de la Clase `LogisticRegression`

La clase **`LogisticRegression`** fue construida de forma modular, implementando cada componente matemático necesario para el algoritmo.

- **Constructor (`__init__`)**: Inicializa la tasa de aprendizaje (`lr`), el número de épocas (`epochs`), los pesos (`weights`), el sesgo (`bias`) y la historia del costo (`cost_history`).
- **Función Sigmoide (`_sigmoid`)**: Esta función de activación es el corazón de la regresión logística. Convierte la salida lineal en una probabilidad entre 0 y 1.
- **Función de Pérdida (`_loss_function`)**: Se implementó la **entropía cruzada binaria**, que es la función de pérdida estándar para problemas de clasificación. Su objetivo es penalizar al modelo por predicciones incorrectas, guiando el proceso de optimización.
- **Método de Entrenamiento (`fit`)**: Utiliza el algoritmo de **descenso de gradiente** para minimizar la función de pérdida. En cada época, calcula las predicciones, los gradientes y actualiza los pesos y el sesgo. La historia del costo se almacena para su posterior visualización.
- **Método de Predicción (`predict`)**: Realiza predicciones sobre nuevos datos, convirtiendo las probabilidades en clases binarias (0 o 1) utilizando un umbral de `0.5`.
- **Visualización (`plot_cost_history`)**: Muestra cómo el costo del modelo disminuye con cada época, un indicador clave de que el proceso de optimización está funcionando correctamente.
- **Evaluación (`evaluate`)**: Calcula un conjunto completo de métricas de rendimiento (`Accuracy`, `Precision`, `Recall`, `F1 Score`) y la matriz de confusión.

---

## 📊 Resultados y Evaluación del Modelo

El modelo se entrenó con una tasa de aprendizaje de `0.02` y `10000` épocas. La evaluación en el conjunto de prueba arrojó las siguientes métricas, demostrando un rendimiento excepcional en la clasificación:

- **Accuracy (Precisión): 95.32%**: El modelo acertó en la predicción del diagnóstico el 95.32% de las veces.
- **Precision (Precisión): 97.17%**: De todos los casos que el modelo predijo como positivos, el 97.17% eran realmente positivos. Esto indica un bajo número de **falsos positivos**.
- **Recall (Sensibilidad): 95.00%**: El modelo fue capaz de identificar el 95% de todos los casos positivos reales. Este es un resultado crucial en el contexto de diagnóstico médico, ya que un alto recall minimiza los **falsos negativos**, que pueden ser errores de alta gravedad.
- **F1 Score: 96.00%**: Este valor demuestra un excelente equilibrio entre la precisión y el recall, lo que indica un rendimiento robusto del modelo.

### Matriz de Confusión

La matriz de confusión proporciona una visión detallada de los resultados del modelo:

```
[[60   3]
[  5 103]]
```

- **Verdaderos Negativos (TN = 60)**: El modelo predijo correctamente que 60 pacientes no tenían cáncer.
- **Verdaderos Positivos (TP = 103)**: El modelo predijo correctamente que 103 pacientes sí tenían cáncer.
- **Falsos Positivos (FP = 3)**: El modelo predijo incorrectamente que 3 pacientes tenían cáncer (errores de Tipo I).
- **Falsos Negativos (FN = 5)**: El modelo predijo incorrectamente que 5 pacientes no tenían cáncer (errores de Tipo II).

---

## 🚀 Conclusión

El modelo de Regresión Logística desarrollado desde cero demostró ser muy efectivo para la tarea de diagnóstico de cáncer de mama, logrando un alto rendimiento en todas las métricas. La alta sensibilidad (recall) es particularmente notable, ya que minimiza el riesgo de pasar por alto un diagnóstico positivo, un aspecto crítico en el sector de la salud.

Este proyecto sirve como una excelente base para entender cómo funcionan los algoritmos de clasificación de aprendizaje automático y cómo se implementan sus componentes desde sus principios matemáticos.

---

## 🛠️ Requisitos de Instalación

Para ejecutar este proyecto, necesitarás instalar los requirements.txt:

```bash
pip install -r requirements.txt
```
