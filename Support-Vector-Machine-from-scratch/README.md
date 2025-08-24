# ⚔️ Implementación Desde Cero de una Máquina de Vectores de Soporte (SVM)

Este proyecto es una implementación **completa y didáctica** de una **Máquina de Vectores de Soporte (SVM)** desde cero, utilizando únicamente `NumPy` para el cálculo matricial y `Matplotlib/Seaborn` para la visualización.  
A diferencia de las librerías de alto nivel como `scikit-learn`, aquí se construye paso a paso el algoritmo, entendiendo cómo funcionan los componentes internos.

El proyecto cubre todas las etapas esenciales: preprocesamiento de etiquetas, definición de la función de pérdida (Hinge Loss), cálculo de gradientes, descenso de gradiente para optimizar los parámetros y visualización del error durante el entrenamiento.

---

## 🛠️ Metodología y Componentes del Modelo

El núcleo del proyecto es la clase `SVM`, diseñada para ser **modular, intuitiva y cercana a la formulación matemática**.

### 1. Implementación de la Clase `SVM`

La clase `SVM` consta de varios métodos clave:

- **Inicialización (`__init__`)**  
  Define los hiperparámetros principales:
  - `lr`: Tasa de aprendizaje para el descenso de gradiente.
  - `lambda_param`: Parámetro de regularización (\(\lambda\)) para controlar el sobreajuste.
  - `n_iters`: Número de iteraciones de entrenamiento.

---

### 2. Funciones Internas

- **Cálculo de Scores (`_scores`)**  
  Implementa la función de decisión:  
  \[
  f(x) = w \cdot x + b
  \]  
  donde `w` es el vector de pesos y `b` el sesgo.

- **Función de Pérdida Hinge (`_hinge_loss`)**  
  Define el costo que guía el aprendizaje:  
  \[
  L(w, b) = \frac{1}{n}\sum\_{i=1}^n \max(0, 1 - y_i f(x_i)) + \frac{\lambda}{2}\|w\|^2
  \]
  - El término \(\max(0, 1 - y_i f(x_i))\) penaliza las muestras mal clasificadas o cercanas al margen.
  - El término \(\frac{\lambda}{2}\|w\|^2\) es la regularización que evita que los pesos crezcan demasiado.

---

### 3. Entrenamiento (`fit`)

El entrenamiento sigue los pasos del **descenso de gradiente**:

1. Conversión de etiquetas → aseguramos que sean \(-1\) y \(+1\).
2. Inicialización de parámetros en cero (`w`, `b`).
3. En cada iteración:
   - Se calculan los _scores_ y los _margins_.
   - Se evalúa la función de pérdida y se guarda en el historial.
   - Se calculan los gradientes de \(w\) y \(b\).
   - Se actualizan los parámetros restando el gradiente escalado por la tasa de aprendizaje.

Esto refleja la optimización de la función de costo hasta converger.

---

### 4. Visualización del Entrenamiento (`plot_loss`)

Permite graficar cómo disminuye la pérdida a lo largo de las iteraciones, verificando que el modelo efectivamente aprende.

---

## 📊 Resultados y Evaluación del Modelo

- El modelo aprende correctamente a separar los datos al optimizar los parámetros \(w\) y \(b\).
- La gráfica de _loss_ demuestra la convergencia progresiva de la función de costo.
- El modelo puede generalizar a datos de prueba, alcanzando precisiones muy altas en datasets simples.

Ejemplo típico de desempeño:

- **Precisión en entrenamiento**: ~100%
- **Precisión en test**: ~100% (en datasets sintéticos linealmente separables).

---

## 🚀 Conclusión

Este proyecto muestra cómo una SVM puede implementarse desde cero de manera clara y didáctica, conectando directamente las fórmulas matemáticas con su traducción a código.  
Al comprender el proceso paso a paso, se logra una visión profunda del algoritmo y sus fundamentos en optimización.

---

## 🛠️ Requisitos de Instalación

Para ejecutar este proyecto, instala los `requirements.txt`:

```bash
pip install -r requirements.txt
```
