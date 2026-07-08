import numpy as np
import matplotlib.pyplot as plt
x1 = np.linspace (-10, 10, 100)
x2 = np.linspace (-10, 10, 100)
def makeData ():
    x, y = np.meshgrid(x1, x2)
    
    w1=1+(x-1)/4
    w2=1+(y-1)/4

    z = (np.sin(np.pi * w1))**2 + (w1 - 1)**2 * (1 + 10 * (np.sin(np.pi * w1 + 1))**2) + (w2 - 1)**2 * (1 + (np.sin(2 * np.pi * w2)**2))
    return  x, y, z

if __name__ == '__main__':
    x, y, z = makeData()

    fig = plt.figure()
    axes = fig.add_subplot(projection='3d')

    axes.plot_surface(x, y, z)
    plt.show()