import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

A = 9.66459
xmin = -10
xmax = 10
count = 200
x = np.linspace(xmin, xmax, count)
y = -np.abs(np.sin(x) * np.cos(A) * np.exp(np.abs(1 - np.sqrt(x**2 + A**2) / np.pi)))

plt.plot(x, y)
plt.show()

root = ET.Element("data")
xdata = ET.SubElement(root, "xdata")
for value in x:
    elem = ET.SubElement(xdata, "x")
    elem.text = f"{value:.2f}"

ydata = ET.SubElement(root, "ydata")
for value in y:
    elem = ET.SubElement(ydata, "y")
    elem.text = f"{value:.2f}"
tree = ET.ElementTree(root)
ET.indent(tree, space="    ", level=0)
tree.write("First_Task.xml", encoding="utf-8", xml_declaration=True)