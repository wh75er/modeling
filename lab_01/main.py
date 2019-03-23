from picard import *
from euler import *
from prettytable import PrettyTable

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


if __name__ == "__main__":
    print()
    #eq = equation(int(input("Input pow of x: ")), int(input("Input pow of y: ")))
    eq = equation()
    #approximation = (int(input("Input approximation value: ")))
    approximation = 5

    left = (float(input("Input left border: ")))
    right = (float(input("Input right border: ")))
    h = (float(input("Input step: ")))

    picard_ap = picard(0, 0, approximation, eq)

    picard_f = lambda x: eval(str(picard_ap))
    euler_roots = euler_explicit(left, right, h, 0, eq.get_func())
    eulerM_roots = euler(left, right, h, 0, eq.get_func())

    table = PrettyTable()
    table.field_names = ["X", "Picard method", "Euler method", "Modified Euler method", "Runge-Kutta method"]
    k = 0
    x = left
    while x <= right:
        table.add_row(["{:.1f}".format(x), "{:.4f}".format(picard_f(x))
                        , "{:.4f}".format(euler_roots[k])
                        , "{:.4f}".format(eulerM_roots[k])
                        , 0])
        k+=1
        x+=h

    print(table)
