# Dinámica Molecular en Dos Dimensiones Y Tres  - Discos Sólidos

Proyecto de investigación para el proyecto final del curso **FS-0432: Física Computacional**.

## Descripción
Este proyecto simula un sistema de partículas esféricas discos sólidos interactuando en un espacio cúbico, bajo colisiones elásticas y rebotes en las paredes. Se estudian patrones de movimiento, distribución espacial y comportamiento colectivo usando simulación molecular básica.

## Objetivos

- Implementar clases y estructuras orientadas a objetos en python para representar partículas.
- Aplicar colisiones elásticas entre partículas y rebotes en paredes.
- Simular dinámicamente el sistema durante un tiempo dado.
- Generar histogramas espaciales y visualización de resultados por medio de matplotlib.
- Aplicar principios de paralelismo, eficiencia computacional y buenas prácticas con Git.

## Tecnicas y recursos utilizados 

- Python 3
- Jupyter Notebook
- NumPy
- Matplotlib
- Organización modular (`src/` con `sim.py`, `colisiones.py`, `simulador.py`)
- Git y GitHub

## Estructura del repositorio

```plaintext
DINAMICA-MOLECULAR/
├── src/
│   ├── sim.py              # Clase Particula y generación del sistema
│   ├── colisiones.py       # Lógica de colisiones entre partículas
│   └── simulador.py        # Bucle principal de simulación
│
├── notebook/
│   └── proyecto_final.ipynb  # Notebook principal con ejecución y visualización
│
├── docs/
│   ├── metodologia.md        # Documento explicativo del problema, recursos y enfoque
│   ├── graficos/             # Gráficos en PNG generados por la simulación
│   │   ├── Fig1.png
│   │   ├── Fig2.png
│   │   └── Fign.png
│   └── Reporte_final.pdf     # Reporte del proyecto en formato PDF
│
├── presentación/
│   └── Diapositivas.pdf      # Diapositivas utilizadas para la exposición final
│
├── .gitignore
├── LICENSE
└── README.md
