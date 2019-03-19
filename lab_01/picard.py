import sympy as sp

class equation():
    def __init__(self, pow_x=None, pow_y=None):
        self.pow_x = 1
        self.pow_y = 1
        if pow_x != None and pow_x != "":
            self.pow_x = pow_x
        if pow_y != None and pow_x != "":
            self.pow_y = pow_y

        self.equation = "x**" + str(pow_x) + " + y**" + str(pow_y) 

    def get_pow_x(self):
        return self.pow_x

    def get_pow_y(self):
        return self.pow_y
    

def picard(x0, v0, n, eq):
#   U'(x) = f(x, u);
#       x0 < x < xr;
#       v(x0) = v0;
#       approximation = n;
#
#       y0(t) = v0;
#
    
    y = v0
    x = sp.Symbol('x')
    pow_x = eq.get_pow_x()
    pow_y = eq.get_pow_y()

#   <<<< calculate approximation
    y = v0 + sp.integrate(pow(x, pow_x) , (x, x0, x))
    print(y)
    for i in range(n):
        y = v0 + sp.integrate(pow(x, pow_x) + pow(y, pow_y) , (x, x0, x))
        print(y)
        
    print()
    return y
        


if __name__ == "__main__":
    print()
    eq = equation(int(input("Input pow of x: ")), int(input("Input pow of y: ")))
    approximation = (int(input("Input approximation value: ")))

    res = picard(0, 0, approximation, eq)

    y = lambda x: eval(str(res))
    print(y(2))
