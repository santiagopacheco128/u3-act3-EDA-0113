import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Santiago Pacheco 0113
print("Santiago Pacheco 0113")
print("UIII Act3 colocar puntos a una imagen")

mi_imagen = cv2.imread("img-0113.webp")
mi_imagen_rgb = cv2.cvtColor(mi_imagen, cv2.COLOR_BGR2RGB)

plt.imshow(mi_imagen_rgb)
plt.title("Imagen y Santiago Pacheco 0113")
plt.show()

print("+-+-+-+-+ puntos en la imagen +-+-+-+-+")

plt.imshow(mi_imagen_rgb)

# Puntos distribuidos por el cuerpo del personaje
x = [410, 390, 475, 330, 250, 550, 400, 300, 510, 420]
y = [180, 470, 475, 520, 620, 620, 720, 750, 800, 900]

plt.scatter(x, y, s=40, c="red")
plt.show()

print("+-+-+-+-+ cuadro en la imagen +-+-+-+-+")

plt.imshow(mi_imagen_rgb)

# Cuadro centrado en la cara
x = [280, 280, 540, 540, 280]
y = [380, 640, 640, 380, 380]

plt.plot(x, y, c="blue")
plt.show()

print("+-+-+-+-+ circulo en la imagen +-+-+-+-+")

plt.imshow(mi_imagen_rgb)

N = 30  # Lados del poligono

x = np.zeros((N+1,))
y = np.zeros((N+1,))

(xc, yc) = (410, 510)  # Centro de la cara
r = 125  # Radio del circulo

for i in range(N+1):
    t = 2*np.pi/N*i
    x[i] = xc + r*np.cos(t)
    y[i] = yc + r*np.sin(t)

plt.plot(x, y, c="green")
plt.show()