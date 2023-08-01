
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_cylinder_and_plane(radius, height, plane_height, num_points=100):
    # Cilindro
    theta = np.linspace(0, 2 * np.pi, num_points)
    z = np.linspace(0, height, num_points)
    theta, z = np.meshgrid(theta, z)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Plano
    xx, yy = np.meshgrid(np.linspace(-1.5 * radius, 1.5 * radius, num_points),
                         np.linspace(-1.5 * radius, 1.5 * radius, num_points))
    zz = plane_height * np.ones_like(xx)  # Z del plano se ajusta a la altura deseada

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the cylinder
    ax.plot_surface(x, y, z, alpha=0.7)

    # Plot the plane
    ax.plot_surface(xx, yy, zz, color='r', alpha=0.4)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Cilindro con Plano en 3D')
    plt.show()

if __name__ == "__main__":
    radius = 1.0       # Radio del cilindro
    height = 3.0       # Altura del cilindro
    plane_height = 1.5 # Altura del plano (mayor a 0)
    plot_cylinder_and_plane(radius, height, plane_height)

