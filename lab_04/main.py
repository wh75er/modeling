import data as d
from calculation import calculateY
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    y_axis = calculateY()
    
    x_axis = [ x for x in np.arange(d.x0, d.l+d.h, d.h)]

    print("Len of y : ", len(y_axis))
    print("Len of x : ", len(x_axis))

    plt.plot(x_axis, y_axis)
    plt.show()
        
