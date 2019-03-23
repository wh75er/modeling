def euler_explicit(l, r, h, y0, f):
    if l > r:
        return -1

    y = [y0]
    while l < r:
        y.append(y[-1] + h*f(l, y[-1]))
        l += h

    return y


def euler(l, r, h, y0, f):
    if l > r:
        return -1

    y = [y0]
    while l < r:
        z = f(l, y[-1])
        y.append(y[-1]+h/2*(z+f(l, y[-1]+h*z)))
        l += h

    return y
