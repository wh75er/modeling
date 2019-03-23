import sympy as sp

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
        
    return y
 
