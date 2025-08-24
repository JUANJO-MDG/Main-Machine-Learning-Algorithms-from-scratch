# 🌲 Implementación Desde Cero de un Bosque Aleatorio para el Diagnóstico de Cáncer de Mama

Este proyecto es una implementación completa y didáctica de un modelo de **Bosque Aleatorio** (Random Forest) construido íntegramente desde cero. A diferencia de las soluciones que utilizan librerías de alto nivel como `scikit-learn` para el algoritmo principal, este proyecto se enfoca en la creación de los componentes fundamentales, incluyendo la clase de **Árbol de Decisión**, para ofrecer una comprensión profunda del funcionamiento interno del algoritmo.

El proyecto abarca todas las etapas del ciclo de vida del aprendizaje automático: desde el preprocesamiento de los datos y la construcción de las clases `DecisionTreeClassifier` y `RandomForest`, hasta la evaluación exhaustiva del rendimiento del modelo.

---

## 🛠️ Metodología y Componentes del Modelo

El núcleo de este proyecto reside en la implementación de dos clases principales: `DecisionTreeClassifier` y `RandomForest`.

### 1. Implementación de la Clase `DecisionTreeClassifier` (Desde Cero)

La clase `DecisionTreeClassifier` fue construida de forma modular, replicando el proceso matemático y lógico de un árbol de decisión. Los pasos clave incluyen:

- **Cálculo de la Entropía (`_calculate_entropy`)**: Se implementó una función para calcular la entropía, que es la medida de la incertidumbre o el desorden de las etiquetas de un conjunto de datos.
- **Ganancia de Información (`_information_gain`)**: Se creó una función para calcular la ganancia de información, una métrica utilizada para determinar el mejor atributo para dividir los datos en cada paso del crecimiento del árbol.
- **Búsqueda de la Mejor División (`_best_split`)**: El algoritmo recorre todas las características y umbrales para encontrar la división que maximiza la ganancia de información.
- **Crecimiento Recursivo del Árbol (`_grow_tree`)**: El árbol se construye de manera recursiva, creando nodos hijos hasta que se cumplen las condiciones de parada, como alcanzar la profundidad máxima o un número mínimo de muestras.

### 2. Implementación de la Clase `RandomForest` (Desde Cero)

La clase `RandomForest` fue diseñada para orquestar múltiples instancias de la clase `DecisionTreeClassifier` implementada de forma personalizada. Su funcionamiento se basa en dos conceptos clave:

- **Bootstrapping**: El método `_bootstrap_samples` crea subconjuntos de datos aleatorios con reemplazo para entrenar cada uno de los árboles del bosque, asegurando que cada árbol vea un conjunto de datos ligeramente diferente.
- **Predicción por Votación**: El método `predict` recopila las predicciones de cada árbol individual y utiliza una votación por mayoría (`_most_common`) para determinar la predicción final del modelo.

---

## 📊 Resultados y Evaluación del Modelo

El modelo se entrenó con 50 árboles (`n_trees=50`), una profundidad máxima de 10 (`max_depth=10`) y un mínimo de 2 muestras para la división (`min_samples_split=2`). La evaluación en el conjunto de prueba arrojó las siguientes métricas, demostrando un rendimiento excepcional en la clasificación:

- **Accuracy (Precisión): 97.90%**: El modelo acertó en la predicción del diagnóstico el 97.90% de las veces.
- **Precision (Precisión): 97.67%**: De todos los casos que el modelo predijo como positivos, el 97.67% eran realmente positivos.
- **F1 Score: 98.2456%**: Este valor demuestra un excelente equilibrio entre la precisión y el _recall_, lo que indica un rendimiento robusto del modelo.

### Matriz de Confusión

La matriz de confusión proporciona una visión detallada de los resultados del modelo:

```
[[56  2]
[ 1 84]]
```

- **Verdaderos Negativos (TN = 56)**: El modelo predijo correctamente que 56 pacientes no tenían cáncer.
- **Falsos Positivos (FP = 2)**: El modelo predijo incorrectamente que 2 pacientes tenían cáncer (errores de Tipo I).
- **Falsos Negativos (FN = 1)**: El modelo predijo incorrectamente que 1 paciente no tenía cáncer (error de Tipo II), lo que demuestra la alta sensibilidad del modelo.
- **Verdaderos Positivos (TP = 84)**: El modelo predijo correctamente que 84 pacientes sí tenían cáncer.

---

## 🚀 Conclusión

El modelo de Bosque Aleatorio desarrollado desde cero demostró ser altamente efectivo para el diagnóstico de cáncer de mama. La alta precisión y el bajo número de falsos negativos son particularmente notables, destacando la robustez y confiabilidad del modelo para una tarea tan crítica. Este proyecto sirve como una excelente base para entender cómo funcionan los algoritmos de ensamblaje y cómo se implementan sus componentes desde sus principios matemáticos.

---

## 🛠️ Requisitos de Instalación

Para ejecutar este proyecto, necesitarás instalar los `requirements.txt`:

```bash
pip install -r requirements.txt
```

Nota: scikit-learn se utiliza únicamente para las funciones de evaluación (métricas), no para la implementación del algoritmo central, que se construyó de forma manual.
