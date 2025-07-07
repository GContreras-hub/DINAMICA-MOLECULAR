# Metodología del Proyecto

## Enunciado del problema

Utilizando las ecuaciones de cinematica, elabore un programa en dos dimensiones con 4 discos solidos de radio r que se mueven sin friccion ni momento angular dentro de una caja de longitud unitaria. A estos discos se les puede asociar una energía cinetica inicial aleatoria, resultando así una distribucion de velocidades aleatoria para el sistema.
---

## Herramientas utilizadas

- **Lenguaje principal**: Python 3
- **Entorno de ejecución**: Jupyter Notebook
- **Librerías**: 
  - NumPy: para operaciones vectoriales y generación aleatoria
  - Matplotlib: para visualización de resultados
- **Organización modular del código**: 
  - `src/sim.py`: clase `Particula` y generación de condiciones iniciales
  - `src/colisiones.py`: gestión de colisiones entre partículas
  - `src/simulador.py`: ciclo de simulación y recolección de datos
- **Control de versiones**: Git y GitHub

---

## Implementación

1. Se definió una clase `Particula` con atributos como posición, velocidad, masa y radio.
2. Se inicializaron múltiples partículas en posiciones aleatorias sin superposición, respetando el tamaño del recipiente.
3. Se simularon colisiones entre partículas con conservación del momento y energía.
4. Se recolectaron todas las posiciones en un arreglo durante la simulación.
5. Se generaron histogramas tridimensionales (`np.histogramdd`) y visualizaciones por cortes planos (XY, XZ, YZ).

---

## Decisiones técnicas y optimizaciones

- Se usó programación orientada a objetos para encapsular la lógica de cada partícula.
- Se aplicó una verificación de solapamiento durante la creación inicial para evitar interpenetraciones.
- Se modularizó el código para permitir la reutilización de funciones y facilitar pruebas.
- El sistema puede escalar a más partículas con cambios mínimos en los parámetros.

---

## Metodología de trabajo

- El proyecto fue desarrollado en etapas:
  1. Pruebas iniciales de partículas individuales.
  2. Implementación de colisiones entre pares.
  3. Recolección de datos y visualización.
  4. Modularización del código.
  5. Documentación y presentación final.
  6. Se usó Git para el control de versiones y GitHub para alojamiento y colaboración.

---

## Resultados esperados

- Distribuciones de partículas que reflejan el comportamiento dinámico del sistema.
- Visualización de zonas de mayor densidad por medio de histogramas.
- Posibilidad de ajustar parámetros (N, masa, velocidad) para estudiar distintas condiciones físicas.

---

## Archivos generados

- Notebook interactivo: `notebook/proyecto_final.ipynb`
- Gráficos en `docs/graficos/`
- Diapositivas para presentación en `presentación/`
- Reporte PDF final con documentación y visualización

---

## Conclusión

El proyecto permitió aplicar múltiples técnicas vistas en el curso de Fisica Computacional: FS-0432, incluyendo simulación física, análisis numérico, organización modular del código, uso eficiente de memoria y control de versiones. Además, ofreció una experiencia práctica en el diseño, ejecución y presentación de una investigación computacional.
