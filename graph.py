import matplotlib.pyplot as plt
import numpy as np

def graph(dict):
    #sort given dictionary into tuples and graph
    plt.plot(*zip(*sorted(dict.items())))
    plt.show()
