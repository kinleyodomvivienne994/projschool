import numpy as np
import matplotlib.pyplot as plt

def draw_line(x1, y1, x2, y2):
    """
    Draw a line between two points using Matplotlib.
    
    Parameters:
    - x1, y1: the coordinates of the first point (x1, y1)
    - x2, y2: the coordinates of the second point (x2, y2)
    """
    plt.plot([x1, x2], [y1, y2])

draw_line(0, 0, 3, 4)

plt.show()
