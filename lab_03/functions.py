from math import exp, log
import data as d

def alpha(x):
    return d.a_alpha/(x-d.b_alpha)

def k(x):
    return d.ak/(x-d.bk)

"""
 ____            _
| __ )  __ _ ___(_)___
|  _ \ / _` / __| / __|
| |_) | (_| \__ \ \__ \
|____/ \__,_|___/_|___/


"""

def u0(x):
    return d.F0/(2*d.l*d.k0) * (x-d.l)**2 + d.Tenv
def u0I(x):
    return d.F0/(d.l*d.k0) * (x-d.l)
def u0II(x):
    return d.F0/(d.l*d.k0)

def u1(x):
    return (x**2 - d.l**2)**2
def u1I(x):
    return 4*x**3 - 4*x*d.l**2
def u1II(x):
    return 12*x**2 - 4*d.l**2

def u2(x):
    return (x**3 - d.l**3)**3
def u2I(x):
    return 9*x**8 - 18*x**5*d.l**3 + 9*x**2*d.l**6
def u2II(x):
    return 72*x**7 - 90*x**4*d.l**3 + 18*x*d.l**6

def u3(x):
    return (x**4 - d.l**4)**4
def u3I(x):
    return 16*x**15 - 48*x**11*d.l**4 + 48*x**7*d.l**8 - d.l**12
def u3II(x):
    return 240*x**14 - 528*x**10*d.l**4 + 336*x**6*d.l**8

