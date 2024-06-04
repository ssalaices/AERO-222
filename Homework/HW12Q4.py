import numpy as np
from numpy import cos, sin, pi, sqrt, absolute
from sympy import symbols

N = 5
b = 1 # span is a symbol that will eventually be cancelled out
cnot = (2*b)/9 
ctip = b/9

a = symbols("a")

B_matrix = np.empty((5,5)) # info to calculate the coefficients
coefficients = np.empty((5,1)) # answers 
alpha_m = np.empty((5,1)) # angle information containing alpha as a symbol

def theta_m(m):
    return ((2*m - 1) * pi)/(2*N)

def chord_m(theta): #describes the span of the wing
    return cnot - (cnot - ctip)*absolute(cos(theta))

# creates the thetas and chords that will be used in the double for loop
thetaList = [theta_m(m) for m in range(1, N + 1)]
chordList = [chord_m(theta) for theta in thetaList]
alpha_m = [(a + (2*(pi/180))) for i in range(5)]

# magic of programming
# using index notation according to equation E.18 
for m in range(0, N): # will be used for indexing theta & chord
    #retrieval
    theta = thetaList[m]
    chord = chordList[m]

    for n in range(1, N+1): # for calculations not indexing
        B_matrix[m, n-1] = sin(n*theta) * ((2*b)/(pi*chord) + n/sin(theta))

coefficients = np.linalg.inv(B_matrix) @ alpha_m

for n in range(1, N+1):
    print(f"A{n} = {coefficients[n-1]}")