import numpy as np
from src.colisiones import manejar_colision

def simular(particulas, t_total, dt, L):
    """
    Ejecuta la simulación del sistema de partículas durante el tiempo t_total.
    
    Parámetros:
        particulas (list): lista de objetos Particula
        t_total (float): tiempo total de simulación
        dt (float): paso de tiempo
        L (float): tamaño del cubo
    Retorna:
        posiciones (np.ndarray): array con las posiciones de todas las partículas en cada paso
    """
    N = len(particulas)
    posiciones = np.array([p.pos for p in particulas])
    T = 0

    while T < t_total:
        for p in particulas:
            p.mover()

        for p in particulas:
            p.rebotar_paredes()

        for i in range(N):
            for j in range(i+1, N):
                manejar_colision(particulas[i], particulas[j])

        posiciones = np.vstack([posiciones, np.array([p.pos for p in particulas])])
        T += dt

    return posiciones
