from picard import *
from euler import *
from rungeKutta import rungeKuttaSecOrder
from prettytable import PrettyTable

#
#   Cauchy problem resolving:
#
#   U'(x) = f(x, u);
#       x0 < x < xr;
#       v(x0) = v0;
#       approximation = n;
#
#       y0(t) = v0;
#


class equation():
    def __init__(self, pow_x=None, pow_y=None):
        self.pow_x = 1
        self.pow_y = 1
        if pow_x != None and pow_x != "":
            self.pow_x = pow_x
        if pow_y != None and pow_x != "":
            self.pow_y = pow_y

        self.equation = "x**" + str(self.pow_x) + " + y**" + str(self.pow_y)
        self.func = lambda x, y: eval(self.equation)

    def get_pow_x(self):
        return self.pow_x

    def get_pow_y(self):
        return self.pow_y

    def get_func(self):
        return self.func

    def calculate(self, x, y):
        return self.func(x, y)

def createTable(eq, approximation, left, right, h):
    picard_ap = picard(0, 0, approximation, eq)

    picard_f = lambda x: eval(str(picard_ap))

    table = PrettyTable()
    table.field_names = ["X", "Picard method", "Explicit Euler method", "Unexplicit Euler method", "Runge-Kutta method"]
    yp_eulerExp = 0
    yp_euler = 0
    yp_runge = 0
    x = left
    while x <= right:
        yp_eulerExp = euler_explicit(yp_eulerExp, x, h, eq.get_func())
        yp_euler = euler(yp_euler, x, h, eq.get_func())
        yp_runge = rungeKuttaSecOrder(yp_runge, x, h, eq.get_func())

        table.add_row(["{:.1f}".format(x), "{:.4f}".format(picard_f(x))
                        , "{:.4f}".format(yp_eulerExp)
                        , "{:.4f}".format(yp_euler)
                        , "{:.4f}".format(yp_runge)])
        x+=h

    print("Table for Y' = ", eq.equation, " equation")
    print(table)


if __name__ == "__main__":
    print()
    #eq = equation(int(input("Input pow of x: ")), int(input("Input pow of y: ")))
    eq = equation()
    eq2 = equation(2, 2)
    approximation = (int(input("Input approximation value: ")))
    #approximation = 5

    print()
    left = (float(input("Input left border: ")))
    right = (float(input("Input right border: ")))
    h = (float(input("Input step: ")))

    createTable(eq, approximation, left, right, h)
    createTable(eq2, approximation, left, right, h)
