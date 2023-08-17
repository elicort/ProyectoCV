#! /home/bmo/Escritorio/PCV/ProyectoCV/Project/venv/bin/python3.10

import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    
    #Cilindro -> x^2 + y^2 = radio^2
    #Plano -> x + y + 2z = 8
    
    
    #Pedimos al usuario ingresar
    #valores del radio y el numero de subintervalos    
        
    radio_cilindro = float(input("Ingrese el radio del cilindro x^2 + y^2 = r^2 : \n"))
    print("Radio: ", radio_cilindro)
    
    particiones = int(input("Ingrese el numero de n particiones: \n"))
    print("Subintervalos: ", particiones)
    
        
    #GRAFICADOR
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
        
        plt.subplots_adjust(bottom=0.20)  # Espacio para el subtítulo
        plt.figtext(0.5, 0.05, r'$x^2 + y^2 =$'+ str(radio_cilindro) + r'$^2$'+'\n'+r'$x + y + 2z = 8$', fontsize=12, ha='center')
        
        plt.suptitle("aqui")
        
        plt.show()

    def graficar(radio):
        altura = 10.0  # Altura del cilindro
        coef_plano = (1, 1, 2, -8)  # Coeficientes del plano x + y + 2z = 8
        plot_cilindro_y_plano(radio, altura, coef_plano)


    #Funcion para calcular longitud de curva
    #Suma de Riemann


    def longitud_curva(radio, n):
        np = (n**2)+n
        resultado = (math.sqrt(5-math.sin(np)))*(math.pi)*radio
        
        print("Longitud de curva: ", resultado)
        
    
    
    
    # Mostrar interseccion de curva    
    # Definimos las funciones paramétricas x(t), y(t) y z(t)
    x_param = lambda t: radio_cilindro*np.cos(t)
    y_param = lambda t: radio_cilindro*np.sin(t)
    z_param = lambda t: (radio_cilindro/2)*(np.sin(t)-np.cos(t))

    # Rango de t
    rango_t = (0, 2*np.pi)
    
    def graf_curva(x_param, y_param, z_param, rango_t, num_points=100):
        t = np.linspace(rango_t[0], rango_t[1], num_points)
        x = x_param(t)
        y = y_param(t)
        z = z_param(t)

        fig_curva = plt.figure()
        ax = fig_curva.add_subplot(111, projection='3d')

        ax.plot(x, y, z, label='Curva paramétrica')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Curva Paramétrica')
        ax.legend()
        
        plt.subplots_adjust(bottom=0.15)  
        plt.figtext(0.5, 0.05, 'r(t)=('+str(radio_cilindro)+'cos(t),'+str(radio_cilindro)+'sen(t), 8-'
                    + str(radio_cilindro/2)+'(cost(t)+sen(t))', fontsize=12, ha='center')
        
        graficar(radio_cilindro)
        
        plt.show()
        
    #Muestra longitud de la curva
    longitud_curva(radio_cilindro, particiones)
    
    #Muestra las graficas
    graf_curva(x_param, y_param, z_param, rango_t)

    
    
if __name__== "__main__":
    main()
    
