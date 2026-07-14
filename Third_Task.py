import argparse
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

read = argparse.ArgumentParser()

read.add_argument("filename")

read.add_argument("--xmin", type=float)

read.add_argument("--xmax", type=float)

args = read.parse_args()

