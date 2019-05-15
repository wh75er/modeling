import data as d
from calculation import calculateY
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    y_axis = calculateY()
    
    x_axis = [ x for x in np.arange(d.x0, d.l+d.h, d.h)]

    plt.plot(x_axis, y_axis)
    plt.show()
        
