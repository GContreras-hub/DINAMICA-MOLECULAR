import numpy as np

def manejar_colision(p1, p2):
    """
    Maneja la colisión entre dos partículas elásticas esféricas.

    Modifica las velocidades y posiciones directamente.
    """
    r = p2.pos - p1.pos
    d = np.linalg.norm(r)
    if d < p1.radio + p2.radio:
        # Vector normal unitario
        n = r / d
        # Diferencia de velocidades
        dv = p1.vel - p2.vel
        # Cantidad de movimiento intercambiada (impulso)
        j = 2 * np.dot(dv, n) / (1/p1.masa + 1/p2.masa)
        # Actualización de velocidades
        p1.vel -= j * n / p1.masa
        p2.vel += j * n / p2.masa
        # Separar partículas para evitar solapamiento
        overlap = (p1.radio + p2.radio - d) * 0.5
        p1.pos -= overlap * n
        p2.pos += overlap * n
