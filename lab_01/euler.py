def euler_explicit(yp, x, h, f):
    return yp + h*f(x, yp)


def euler(yp, x, h, f):
    z = f(x, yp)
    return yp + h/2*(z+f(x, yp+h*z))
