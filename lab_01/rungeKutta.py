def rungeKuttaSecOrder(yp, x, h, f):
    z = f(x + h/2, yp + h/2*f(x, yp))
    return yp + h*z
