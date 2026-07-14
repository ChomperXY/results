import argparse
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

read = argparse.ArgumentParser()

read.add_argument("filename")

read.add_argument("--xmin", type=float)

read.add_argument("--xmax", type=float)

args = read.parse_args()

tree = ET.parse(args.filename)
root = tree.getroot()

x = []
y = []

for value in root.find("xdata"):
    x.append(float(value.text))
for value in root.find("ydata"):
    y.append(float(value.text))
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.title("y=f(x)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

if args.xmin is not None:
    xmin = args.xmin
else:
    xmin = min(x)
if args.xmax is not None:
    xmax = args.xmax
else:
    xmax = max(x)
plt.xlim(xmin, xmax)

plt.show()