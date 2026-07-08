import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

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

root = ET.Element("data")
xval = ET.SubElement(root, "xdata")
yval = ET.SubElement(root, "ydata")
for xi, in zip(x):
    ET.SubElement(xval, "x").text = f"{xi:.4f}"
for yi, in zip(y):
    ET.SubElement(yval, "y").text = f"{yi:.4f}"
tree = ET.ElementTree(root)
tree.write("First_Task.xml", encoding="utf-8", xml_declaration=True)
