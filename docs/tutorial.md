# Explicación del Notebook 

Este archivo Jupyter Notebook contiene el desarrollo principal del proyecto de simulación de dinámica molecular con discos sólidos. Aquí se explican las secciones del notebook y cómo usarlo correctamente.

## Estructura general del notebook

1. **Importación de librerías**
   - Se importan `numpy`, `matplotlib.pyplot`, y los módulos creados en `src/`.

2. **Definición de parámetros del sistema**
   - `L`: tamaño del cubo simulado
   - `dt`: paso de tiempo
   - `t`: tiempo total de simulación
   - `N`: cantidad de partículas

3. **Generación de partículas**
   - Se usa `generar_posiciones(N)` desde `sim.py` para inicializar partículas con posiciones, radios, masas y velocidades aleatorias.
   - Se asegura que no haya solapamientos iniciales.

4. **Ejecución de la simulación**
   - Se llama a `simular(particulas, t, dt, L)` desde `simulador.py`, que ejecuta el bucle temporal completo.
   - Se recolectan todas las posiciones en un array para análisis posterior.

5. **Visualización**
   - Se genera un histograma 3D de las posiciones acumuladas (`np.histogramdd`).
   - Se grafican cortes planos del histograma: XY, XZ, YZ usando `matplotlib.pyplot.imshow`.

## Guía rápida para ejecutar el proyecto

Este proyecto está diseñado para correr desde Jupyter Notebook. A continuación se resumen los pasos necesarios para ejecutarlo correctamente.

---

### 1. Clonar el repositorio

bash:
git clone https://github.com/GContreras-hub/DINAMICA-MOLECULAR.git
cd DINAMICA-MOLECULAR

### 2. Instalar dependencias (de ser necesario)
bash:
pip install numpy matplotlib

### 3. Abrir el notebook
cd notebook
jupyter notebook

### 4. Abrir el archivo del proyecto
proyecto_final.ipynb

### 5. Ejecutar el notebook
- Ejecutá todas las celdas en orden, usando Shift + Enter.
- Al finalizar, se mostrarán los gráficos generados por la simulación.

### 6. Importar desde src/ (de ser necesario)
import sys
sys.path.append('../src')

### 7. Visualizar las graficas 
