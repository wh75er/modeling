import sympy as sp

class Node:
    def __init__(self, power, value):
        self.power = power
        self.value = value

def getIntegral(x, power, previous):
    return pow(x, power+1) / (previous * (power+1))

def picard1(x, n):
    vector = [1]

    result = 0
    for i in range(1, n+1):
        previousValue = vector[i-1]
        newValue = previousValue * (i+1)
        vector.append(newValue)
        result += getIntegral(x, i, vector[i - 1])

    return result

# ------------------------------------------------------------------------------------------


def getNewNodes(vector):
    temp = []

    for j in range(len(vector)):
        for k in range(len(vector)):
            nd = Node(vector[j].power + vector[k].power, vector[j].value * vector[k].value)
            temp.append(nd)

    return temp


def integrate(vector):
    temp = []

    for i in vector:
        nd = Node(i.power + 1, i.value * (i.power + 1))
        temp.append(nd)

    return temp

def picard2(x, n):
    vector = [ Node(2, 1) ]

    vector = integrate(vector)

    for i in range(1, n):
        vector = getNewNodes(vector)
        vector.append(Node(2, 1))
        vector = integrate(vector)

    result = 0
    for i in vector:
        result += pow(x, i.power) / i.value

    return result
        
# ------------------------------------------------------------------------------------------
