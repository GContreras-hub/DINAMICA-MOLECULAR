import numpy as np
import matplotlib.pyplot as plt

# Parámetros
L = 1000
dt = 0.01

class Particula:
    def __init__(self, pos, vel, masa=1, radio=1):
        self.pos = np.array(pos, dtype=np.float64)
        self.vel = np.array(vel, dtype=np.float64)
        self.masa = masa
        self.radio = radio
        self.fuerza = np.zeros(3, dtype=np.float64)
    
    def mover(self):
        self.vel += (self.fuerza / self.masa) * dt
        self.pos += self.vel * dt
    
    def rebotar_paredes(self):
        for i in range(3):
            if self.pos[i] < self.radio:
                self.pos[i] = self.radio
                self.vel[i] *= -0.98
            elif self.pos[i] > L - self.radio:
                self.pos[i] = L - self.radio
                self.vel[i] *= -0.98
    
    def rebotar_particula(self, otra):
        r = otra.pos - self.pos
        d = np.linalg.norm(r)
        if d < self.radio + otra.radio:
            n = r / d
            dv = self.vel - otra.vel
            j = 2 * np.dot(dv, n) / (1/self.masa + 1/otra.masa)
            self.vel -= j * n / self.masa
            otra.vel += j * n / otra.masa
            overlap = (self.radio + otra.radio - d) * 0.5
            self.pos -= overlap * n
            otra.pos += overlap * n

def generar_posiciones(N):
    particulas = []
    i = 0


    while i < N:
        masa= np.random.uniform(250, 500)   #Rango de masas
        radio   = np.random.uniform(50, 150) #Rango de radios
        pos = np.array(np.random.uniform(radio, L - radio, 3)) #Rango de posiciones, no cambiar
        vel = np.random.uniform(5, 20, 3) #Rango de velocidades
        nueva = Particula(pos, vel, masa, radio) 
        if all(np.linalg.norm(nueva.pos - p.pos) > (nueva.radio + p.radio) for p in particulas):
            particulas.append(nueva)
            i += 1
    return particulas