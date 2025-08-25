"""

# 🚗💨 Análisis y Predicción de Emisiones de Vehículos (2000-2022)

Este proyecto es un **análisis exhaustivo y didáctico** enfocado en la comprensión y predicción del **consumo de combustible** y las **emisiones de CO2** de vehículos. El núcleo del proyecto es la implementación de un modelo de **regresión lineal múltiple** para desentrañar las relaciones entre las características de los vehículos y su impacto en el medio ambiente. A diferencia de un simple uso de librerías, este enfoque paso a paso muestra el proceso completo de un proyecto de ciencia de datos, desde la exploración inicial hasta el modelado predictivo.

El objetivo principal es responder a la pregunta: ¿qué atributos de un vehículo son los factores más influyentes en su eficiencia y sus emisiones?

---

## 🛠️ Metodología y Componentes del Modelo

El proyecto sigue una metodología de ciencia de datos clara y estructurada, garantizando que cada paso, desde el preprocesamiento hasta el modelado, sea transparente y reproducible.

### 1. Exploración y Preprocesamiento de Datos (EDA)

Esta fase es crucial para asegurar la calidad de los datos y obtener una comprensión inicial de las variables. Los pasos incluyen:

- **Carga y Estructura**: Cargar el conjunto de datos `Fuel_Consumption_2000-2022.csv` y examinar su estructura, incluyendo los tipos de datos y la presencia de valores nulos.
- **Análisis Descriptivo**: Resumir las principales tendencias y distribuciones de las variables numéricas para identificar la escala y el rango de cada característica.
- **Visualización**: Utilizar gráficos de dispersión e histogramas para visualizar la distribución de las variables y detectar correlaciones, como la fuerte relación entre el `ENGINE SIZE` y las `EMISSIONS`.

### 2. Modelado de Regresión Lineal Múltiple

Una vez que los datos están limpios y se entienden sus relaciones, se procede a la implementación del modelo predictivo:

- **Selección de Características**: Se seleccionan las variables más relevantes (`YEAR`, `ENGINE SIZE`, `CYLINDERS`, `EMISSIONS` y `FUEL CONSUMPTION`) para construir un modelo predictivo robusto.
- **Implementación del Modelo**: Se utiliza la **regresión lineal múltiple** para encontrar la ecuación lineal que mejor se ajusta a los datos y predice el consumo de combustible y las emisiones basándose en las características seleccionadas. Este modelo es ideal para comprender cómo cada variable predictora contribuye a la variable objetivo.

---

## 📊 Datos y Variables

El conjunto de datos contiene información detallada sobre el consumo de combustible y las emisiones de una amplia gama de vehículos a lo largo de más de dos décadas.

Las **variables predictoras** clave para el modelo incluyen:

- **`YEAR`**: Año del modelo.
- **`ENGINE SIZE`**: Tamaño del motor en litros.
- **`CYLINDERS`**: Número de cilindros del motor.

Las **variables objetivo** son:

- **`FUEL CONSUMPTION`**: Consumo de combustible combinado en L/100 km.

---

## 🚀 Conclusión

Este proyecto demuestra una comprensión profunda del ciclo de vida de un proyecto de ciencia de datos, desde la fase inicial de análisis exploratorio hasta la implementación de un modelo de machine learning. Al centrarse en la **regresión lineal múltiple**, el proyecto muestra cómo un algoritmo clásico puede ser utilizado de manera efectiva para extraer insights valiosos y construir un modelo predictivo que resuelva un problema relevante en el mundo real.

---

## 📚 Librerías y Requisitos

Para ejecutar este análisis, asegúrate de tener instalados los `requirements.txt`

```bash
pip install -r requirements.txt
```
