# Here the function is defined
import numpy as np


def linfit(xdat, ydat):
    # Here xbar and ybar are calculated
    xbar = np.sum(xdat)/len(xdat)
    ybar = np.sum(ydat)/len(ydat)

    # Insert calculation of m and c here. If nothing is here the data will be plotted with no linear fit
    m = (xdat - xbar)
    n = np.multiply(m, m)
    m = np.multiply(m, ydat)
    a = np.sum(m)
    b = np.sum(n)
    m = a/b

    c = ybar - (m * xbar)
    # Return your values as [m, c]
    return [m, c]


# Produce the plot - don't put this in the next code block
line()
