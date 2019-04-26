from picard import *
from euler import *
from rungeKutta import rungeKuttaSecOrder
from prettytable import PrettyTable

from os import system

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

def f1(x, y):
    return x + y

def f2(x, y):
    return x**2 + y**2

def createTable(eq, approximation, left, right, h):
    func = f1
    picard = picard1
    if(eq.get_pow_x == 2):
        func = f2
        picard = picard2

    table = PrettyTable()
    table.field_names = ["X", "Picard method", "Explicit Euler method", "Unexplicit Euler method", "Runge-Kutta method"]
    yp_eulerExp = 0
    yp_euler = 0
    yp_runge = 0
    x = left
    while x <= right:
        print("\rprocessing...{:.0f}%".format((x*100)/right), end="\n"); 
        yp_eulerExp = euler_explicit(yp_eulerExp, x, h, func)
        yp_euler = euler(yp_euler, x, h, func)
        yp_runge = rungeKuttaSecOrder(yp_runge, x, h, func)

        table.add_row(["{:.1f}".format(x), "{:.4f}".format(picard(x, approximation))
                        , "{:.4f}".format(yp_eulerExp)
                        , "{:.4f}".format(yp_euler)
                        , "{:.4f}".format(yp_runge)])
        x+=h

    print("Table for Y' = ", eq.equation, " equation")
    print(table)


if __name__ == "__main__":
    print()
    #eq = equation(int(input("Input pow of x: ")), int(input("Input pow of y: ")))
    #eq = equation()
    eq2 = equation(2, 2)
    #approximation = (int(input("Input approximation value: ")))
    approximation = 2

    print()
    left = (float(input("Input left border: ")))
    right = (float(input("Input right border: ")))
    h = (float(input("Input step: ")))

    #createTable(eq, approximation, left, right, h)
    createTable(eq2, approximation, left, right, h)
