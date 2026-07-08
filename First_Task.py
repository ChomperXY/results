import numpy as np
import matplotlib.pyplot as plt

A = 9.66459
xmin = -10
xmax = 10
count = 200
x = np.linspace(xmin, xmax, count)
y = -np.abs(
    np.sin(x) *
    np.cos(A) *
    np.exp(np.abs(1 - np.sqrt(x**2 + A**2) / np.pi))
)
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.title("График функции")
plt.grid(True)
plt.show()
