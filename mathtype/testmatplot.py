import string
import matplotlib.pyplot as plt
import numpy as np

if  __name__=='__main__':
    for line in open('data'):
        dot = line.split()
        plt.plot(dot[0],dot[1],'yo-')
    plt.title("demo")
    plt.ylabel("speed")
    plt.xlabel("time")
    plt.show()
    