import data as d
from functions import *
import numpy

"""
 _____ _
|_   _| |__   ___  _ __ ___   __ _ ___
  | | | '_ \ / _ \| '_ ` _ \ / _` / __|
  | | | | | | (_) | | | | | | (_| \__ \
  |_| |_| |_|\___/|_| |_| |_|\__,_|___/

       _                  _ _   _
  __ _| | __ _  ___  _ __(_) |_| |__  _ __ ___
 / _` | |/ _` |/ _ \| '__| | __| '_ \| '_ ` _ \
| (_| | | (_| | (_) | |  | | |_| | | | | | | | |
 \__,_|_|\__, |\___/|_|  |_|\__|_| |_|_| |_| |_|
         |___/

"""

def thomasAlgorithm(A, B, C, D, k0, m0, p0, kN, mN, pN):
    xi = [-m0/k0]
    eta = [p0/k0]

    for i in range(len(A)):
        xi.append( C[i] / (B[i] - A[i]*xi[i]) )
        eta.append( (D[i] + A[i]*eta[i]) / (B[i] - A[i]*xi[i]) )

    y = [(pN - mN*eta[-1]) / (kN + mN*xi[-1])]

    for i in reversed(range(1, len(A))):
        y.append( xi[i]*y[-1] + eta[i] )

    y.reverse()

    return y

def calculateY():

    A, B, C, D = getCoeffs()

    k0, m0, p0 = getLeftBoundaryCoeffs()
    kN, mN, pN = getRightBoundaryCoeffs()

    y = thomasAlgorithm(A, B, C, D, k0, m0, p0, kN, mN, pN)

    return y
