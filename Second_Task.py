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

    fig = plt.figure(figsize=(14, 10))
    axes1 = fig.add_subplot(221, projection='3d')
    axes1.plot_surface(x, y, z, cmap='gray' )
    axes1.set_title('y=f(x)')
    axes1.set_xlabel('x1')
    axes1.set_ylabel('x2')
    axes1.set_zlabel('y=f(x1, x2)')
    
    axes2 = fig.add_subplot(222, projection='3d')
    axes2.plot_surface(x, y, z, cmap='gray')
    axes2.view_init(elev=90, azim=-90)
    axes2.set_title('Вид сверху')
    axes2.set_xlabel('x1')
    axes2.set_ylabel('x2')
    axes2.set_zlabel('y=f(x1, x2)')

    axes3 = fig.add_subplot(223)
    x20 = 1
    w1 = 1 + (x1 - 1) / 4
    w2 = 1 + (x20 - 1) / 4
    y1 = (np.sin(np.pi * w1))**2 + (w1 - 1)**2 * (1 + 10 * (np.sin(np.pi * w1 + 1))**2) + (w2 - 1)**2 * (1 + (np.sin(2 * np.pi * w2)**2))
    axes3.plot(x1, y1)
    axes3.set_title('y = f(x1, x20)')
    axes3.set_xlabel('x1')
    axes3.set_ylabel('y')
 

    plt.show()

