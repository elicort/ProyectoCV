#! /home/bmo/Escritorio/PCV/ProyectoCV/Project/venv/bin/python3.10

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Cilindro

def plot_cilindro_y_plano(radio, altura, coef_plano, num_points=100):
    theta = np.linspace(0, 2 * np.pi, num_points)
    z = np.linspace(0, altura, num_points)
    theta, z = np.meshgrid(theta, z)
    x = radio * np.cos(theta)
    y = radio * np.sin(theta)

    # Plano personalizado
    a, b, c, d = coef_plano
    xx, yy = np.meshgrid(np.linspace(-1.5 * radio, 1.5 * radio, num_points),
                         np.linspace(-1.5 * radio, 1.5 * radio, num_points))
    zz = (-a * xx - b * yy - d) / c

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot cilindro
    ax.plot_surface(x, y, z, alpha=0.7)

    # Plot plano personalizado
    ax.plot_surface(xx, yy, zz, color='r', alpha=0.4)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Cilindro intersecado por el Plano ')
    plt.show()

def graficar(radio):
    altura = 10.0  # Altura del cilindro
    coef_plano = (1, 1, 2, -8)  # Coeficientes del plano x + y + 2z = 8
    plot_cilindro_y_plano(radio, altura, coef_plano)

