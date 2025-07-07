# Parámetros utilizados para las Figuras
## Variables
- **L: Lado del cubo** 
- **dt: Cambio del tiempo** 
- **N: Número de partículas**  
- **t: Tiempos de simulación** 
- **m_min: Masa minima** 
- **m_max: Masa maxima** 
- **r_min: Radio minimo** 
- **r_max: Radio maximo** 
- **v_min: Velocidad minima** 
- **v_max: Velocidad maxima** 

## Para las figuras 1, 2, 3

- **L** = 250  
- **dt** = 1  
- **N** = 200  
- **t** = 10000  

## Para las Figuras 4, 5, 6

- **L** = 1 
- **dt** = 0.01
- **N** = 4 
- **t** = 10
- **m_min** = 25
- **m_max** = 50
- **r_min** = 0.01
- **r_max** = 0.2
- **v_min** = 1
- **v_max** = 0.01

### Códigos de generación:

```python
masa = np.random.uniform(25, 50)  
radio = np.random.uniform(0.01, 0.05)  
posicion = np.array(np.random.uniform(radio, L - radio, 3))  
velocidad = np.random.uniform(0.3, 3, 3)
```
