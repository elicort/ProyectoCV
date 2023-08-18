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

    # Rango de t
    rango_t = (0, 2*np.pi)

    # Definimos las funciones paramétricas x(t), y(t) y z(t)
    def parametros(t):
        x_param = radio_cilindro*np.cos(t)
        y_param = radio_cilindro*np.sin(t)
        z_param = (radio_cilindro/2)*(np.sin(t)-np.cos(t))

        return x_param, y_param, z_param
 
    #Funcion para calcular longitud de curva
    #Suma de Riemann
    def longitud_curva(parametros, rango_t, particiones):
        a, b = rango_t
        delta_t = (b - a) / particiones
        total= 0.0
    
        for i in range(particiones):
            t1 = a + i * delta_t
            t2 = a + (i + 1) * delta_t
            x1, y1, z1 = parametros(t1)
            x2, y2, z2 = parametros(t2)
            
            longitud = np.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
            total += longitud

            total_integrado= (radio_cilindro/2)*14.01417

        print("Aproximación de la longitud de arco: ", total)
    
        print("Longitud de curva calculada con integral: ",total_integrado )
        

    # Mostrar interseccion de curva     
    def graf_curva(parametros, rango_t, num_points=100):
        t = np.linspace(rango_t[0], rango_t[1], num_points)
        x, y, z = parametros(t)

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
        
        altura = 5.0*radio_cilindro  # Altura del cilindro
        plano = (1, 1, 2, -8)  # Coeficientes del plano x + y + 2z = 8
        plot_cilindro_y_plano(radio_cilindro, altura, plano)
        
        plt.show()

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
        plt.figtext(0.5, 0.05, r'$x^2 + y^2 =$'+ str(radio_cilindro) + 
                    r'$^2$'+'\n'+r'$x + y + 2z = 8$', fontsize=12, ha='center')
        plt.show()
        
    
    #Muestra longitud de la curva
    longitud_curva(parametros, rango_t, particiones)
    #Muestra las graficas
    graf_curva(parametros, rango_t)

    
if __name__== "__main__":
    main()
    
