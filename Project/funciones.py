#! /home/bmo/Escritorio/PCV/ProyectoCV/Project/venv/bin/python3.10

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_cilindro_y_plano(radio, altura, coef_plano, num_points=100):
    
        fig, (ax1, ax2) = plt.subplot(1, 2)
        
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

        fig_ci = plt.figure()
        ax1 = fig_ci.add_subplot(111, projection='3d')

        # Plot cilindro
        ax1.plot_surface(x, y, z, alpha=0.7)

        # Plot plano personalizado
        ax1.plot_surface(xx, yy, zz, color='r', alpha=0.4)

        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.set_zlabel('Z')
        ax1.set_title('Cilindro intersecado por el Plano ')
        
        # Definimos las funciones paramétricas x(t), y(t) y z(t)
        x_param = lambda t: radio*np.cos(t)
        y_param = lambda t: radio*np.sin(t)
        z_param = lambda t: (radio/2)*(np.sin(t)-np.cos(t))

        # Rango de t
        rango_t = (0, 2*np.pi)
        
        t = np.linspace(rango_t[0], rango_t[1], num_points)
        x = x_param(t)
        y = y_param(t)
        z = z_param(t)

        fig_curva = plt.figure()
        ax2 = fig_curva.add_subplot(111, projection='3d')

        ax2.plot(x, y, z, label='Curva paramétrica')
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_zlabel('Z')
        ax2.set_title('Curva Paramétrica')
        ax2.legend()
        
        
        
        plt.show()
        
        
if __name__== "__main__":
    altura = 10.0  # Altura del cilindro
    coef_plano = (1, 1, 2, -8)  # Coeficientes del plano x + y + 2z = 8
    plot_cilindro_y_plano(2, altura, coef_plano)
    