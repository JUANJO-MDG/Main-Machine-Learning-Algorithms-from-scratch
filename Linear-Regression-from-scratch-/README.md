# 📉 Implementación Desde Cero de la Regresión Lineal

Este proyecto es una **implementación completa y educativa de la Regresión Lineal** construida desde cero en Python. El objetivo principal es desmitificar este algoritmo fundamental de machine learning, permitiendo que comprendas su funcionamiento interno sin depender de librerías de alto nivel para el núcleo del cálculo. El notebook te guía paso a paso a través de la preparación de los datos, el entrenamiento del modelo, la evaluación de su rendimiento y la visualización de los resultados.

---

## 📌 Visión General del Proyecto

El corazón de este proyecto reside en entender la **Regresión Lineal** desde sus fundamentos matemáticos hasta su aplicación en código. El enfoque es puramente didáctico y se centra en los siguientes componentes clave:

- **Preparación de Datos**: Procesar y organizar los datos para que el modelo pueda utilizarlos de manera eficiente.
- **Implementación del Modelo**: Escribir las funciones principales de la regresión lineal desde cero, incluyendo el cálculo del gradiente y la actualización de los parámetros.
- **Métricas de Evaluación**: Calcular métricas de rendimiento como el **Error Cuadrático Medio (MSE)** y el **Coeficiente de Determinación (R²)** para evaluar la precisión del modelo.
- **Visualización**: Graficar la línea de mejor ajuste y el comportamiento del error durante el entrenamiento para una comprensión visual del proceso.

---

## 🛠️ Metodología y Componentes del Modelo

### 1. Fundamentos Matemáticos

El modelo opera bajo el principio de encontrar la línea que mejor se ajusta a los datos, minimizando la distancia vertical entre los puntos de datos y la línea.

- **Función de Hipótesis**: La predicción se basa en la fórmula de una línea recta:
  \[
  y = mx + b
  \]
  donde `m` es la pendiente (o vector de pesos, **w**) y `b` es el intercepto (o sesgo, **b**).
- **Función de Pérdida (MSE)**: Se utiliza el **Error Cuadrático Medio** para medir el error del modelo. La implementación busca minimizar este valor para encontrar los parámetros óptimos (`m` y `b`).

### 3. Entrenamiento

El entrenamiento es un proceso iterativo de optimización a través del **descenso de gradiente**. En cada iteración:

- Se calculan las predicciones del modelo.
- Se calcula la diferencia entre las predicciones y los valores reales.
- Se ajustan los parámetros (`m` y `b`) en la dirección opuesta al gradiente de la función de pérdida.
- El proceso se repite hasta alcanzar la convergencia.

### 4. Evaluación del Rendimiento

Después del entrenamiento, se evalúa el modelo utilizando:

- **Error Cuadrático Medio (MSE)**: Mide el promedio de los errores al cuadrado entre las predicciones y los valores reales.
- **Coeficiente de Determinación (R²)**: Un valor entre 0 y 1 que indica qué tan bien las variables independientes explican la variabilidad de la variable dependiente.

---

## 📚 Librerías y Requisitos

Para ejecutar este análisis, asegúrate de tener instalados los `requirements.txt`

```bash
pip install -r requirements.txt
```
