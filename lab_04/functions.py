from math import exp, log
import data as d
from numpy import arange

"""
"""

def alpha(x):
    return d.a_alpha/(x-d.b_alpha)

def k(x):
    return d.ak/(x-d.bk)

def p(x):
    return (2 * alpha(x)) / d.R

def f(x):
    return (2*alpha(x)) / d.R * d.Tenv

"""
  ____            __  __
 / ___|___   ___ / _|/ _|___
| |   / _ \ / _ \ |_| |_/ __|
| |__| (_) |  __/  _|  _\__ \
 \____\___/ \___|_| |_| |___/

"""

def getHalfLeft(x):
    return (2 * k(x) * k(x-d.h)) / (k(x) + k(x-d.h))

def getHalfRight(x):
    return (2 * k(x) * k(x+d.h)) / (k(x) + k(x+d.h))

def getCoeffs():
    A = []
    B = []
    C = []
    D = []

    for x in arange(d.x0, d.l+d.h, d.h):
        A.append( getHalfLeft(x) / d.h )
        C.append( getHalfRight(x) / d.h )
        B.append( A[-1] + C[-1] + p(x) * d.h)
        D.append( f(x) * d.h )
    
    return A, B, C, D

def getLeftBoundaryCoeffs():
    xHalf = getHalfRight(d.x0)
    p1 = p(d.x0 + d.h)
    f1 = f(d.x0 + d.h)

    p0 = p(d.x0)
    f0 = f(d.x0)

    pHalf = (p0 + p1) / 2

    k0 = xHalf + d.h**2 * pHalf / 8 + d.h**2 * p0 / 4
    m0 = d.h**2 * pHalf / 8 - xHalf
    P0 = d.h * d.F0 + d.h**2 * (3 * f0 + f1) / 4

    return k0, m0, P0

def getRightBoundaryCoeffs():
    xHalf = getHalfLeft(d.l)
    pHalf = p(d.l - d.h)
    fHalf = f(d.l - d.h)

    kN = -xHalf / d.h - d.alphaN - (p(d.l) * d.h) / 4 - d.h * (pHalf + p(d.l)) / 16
    mN = xHalf / d.h - d.h * (pHalf + p(d.l)) / 16
    pN = -d.alphaN * d.Tenv - d.h * (3 * f(d.l) + fHalf) / 8

    return kN, mN, pN
