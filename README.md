# 📚 Implementación de Algoritmos de Machine Learning Desde Cero

Este repositorio es un viaje educativo a través de los fundamentos del **aprendizaje automático supervisado**. A diferencia de los enfoques convencionales que utilizan librerías de alto nivel como `scikit-learn`, este proyecto se enfoca en la implementación de los algoritmos más comunes **desde cero**, utilizando únicamente herramientas esenciales como `pandas` y `NumPy` como bases.

El objetivo principal es ir más allá del "cómo usar" y sumergirse en el "cómo funciona", traduciendo la teoría matemática y los conceptos estadísticos directamente en código funcional. Este enfoque permite una comprensión profunda de las fortalezas y debilidades de cada modelo, así como una visión clara de los procesos de optimización que tienen lugar "bajo el capó".

---

## 🛠️ Metodología y Componentes del Modelo

Cada algoritmo en este proyecto ha sido diseñado como una clase modular e intuitiva, reflejando las mejores prácticas de la programación orientada a objetos.

### 1. Enfoque General de Implementación

Para cada modelo, se siguen estos principios:

- **Fundamentos Matemáticos**: La implementación del código se basa directamente en las fórmulas de optimización, funciones de costo y teoremas que rigen el algoritmo.
- **Entrenamiento (`fit`)**: Un método clave que se encarga de todo el proceso de aprendizaje del modelo a partir de los datos.
- **Predicción (`predict`)**: Un método que utiliza los parámetros aprendidos para hacer predicciones sobre nuevas instancias.
- **Modularidad**: Cada algoritmo está encapsulado en su propia clase, haciendo el código limpio y fácil de reutilizar.

---

### 2. Algoritmos Implementados

Este proyecto cubre un espectro de modelos fundamentales de aprendizaje supervisado para tareas de **regresión** y **clasificación**.

#### Modelos de Regresión

- **Regresión Lineal Simple y Múltiple**: Se enfoca en predecir un valor continuo al encontrar la relación lineal óptima entre una o múltiples variables de entrada y una variable de salida. La implementación se centra en la minimización del **Error Cuadrático Medio (MSE)** a través de **descenso de gradiente**.

#### Modelos de Clasificación

- **Regresión Logística**: Aunque su nombre contiene la palabra "regresión", este modelo se utiliza para la **clasificación binaria**. A diferencia de la regresión lineal, utiliza una función **sigmoide** para transformar la salida en una probabilidad, lo que permite clasificar las instancias en dos clases distintas. La optimización se realiza minimizando la **función de pérdida de entropía cruzada**.

- **K-Vecinos Más Cercanos (KNN)**: Un algoritmo **no paramétrico** y de "aprendizaje perezoso". En lugar de aprender un modelo, simplemente almacena los datos de entrenamiento y clasifica una nueva instancia basándose en la mayoría de votos de sus 'K' vecinos más cercanos, calculando la **distancia** entre puntos.

- **Árboles de Decisión y Bosques Aleatorios**:

  - **Árboles de Decisión**: Construye una estructura de "si-entonces" para tomar decisiones, dividiendo los datos en ramas basadas en las características más informativas.
  - **Bosques Aleatorios**: Un **método de ensemble** que mejora la precisión y la robustez al combinar los resultados de múltiples árboles de decisión entrenados de forma independiente.

- **Máquinas de Vectores de Soporte (SVM)**: Un poderoso algoritmo que busca el **hiperplano** que maximiza el margen de separación entre las clases. La implementación se centra en resolver este **problema de optimización** para encontrar los parámetros `w` y `b` óptimos.

- **Naive Bayes**: Un clasificador **probabilístico** basado en el **Teorema de Bayes**. Su nombre se debe a la suposición "ingenua" de que todas las características son independientes entre sí, lo que lo hace computacionalmente muy eficiente y efectivo, especialmente en la clasificación de texto. La implementación incluye una técnica crucial: el **suavizado de Laplace** para manejar de manera robusta los datos que el modelo no ha visto previamente.

---

## 🧠 Conceptos Fundamentales Cubiertos

Al implementar estos modelos desde cero, se adquiere una comprensión profunda de los siguientes conceptos:

- **Descenso de Gradiente**: El motor de optimización detrás de los modelos de regresión y SVM, que ajusta iterativamente los parámetros para minimizar una función de pérdida.
- **Funciones de Pérdida**: Métricas como el **Error Cuadrático Medio**, la **Entropía Cruzada** y la **Hinge Loss** que cuantifican el error del modelo y guían el proceso de aprendizaje.
- **Vectorización**: El uso de operaciones matriciales de `NumPy` para realizar cálculos eficientes y evitar bucles lentos en Python.
- **Programación Orientada a Objetos (POO)**: La organización del código en clases modulares y reutilizables, lo que mejora la claridad y la escalabilidad.
- **Manejo de Datos Categóricos y Numéricos**: Cómo los diferentes algoritmos abordan distintos tipos de datos.

---

## 🚀 Conclusión

Este proyecto no es solo una colección de scripts; es una demostración de una comprensión sólida de los principios teóricos y prácticos del machine learning. Es un recurso valioso para aquellos que buscan consolidar sus conocimientos, entender cómo funcionan los modelos más allá de las librerías, y construir una base robusta para enfrentar problemas de datos más complejos.

---

## 🛠️ Requisitos de Instalación

Para ejecutar este proyecto, solo necesitas tener instaladas los requerimientos:

```bash
pip install -r requirements.txt
```
