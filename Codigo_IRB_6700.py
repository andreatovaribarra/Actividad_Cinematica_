import sympy as sp
from sympy.matrices import rot_axis3

import matplotlib.pyplot as plt
import numpy as np

from spatialmath import *
from spatialmath.base import *

# Definir símbolos
theta, d, a, alpha = sp.symbols('theta, d, a, alpha')

# Matriz RzTzTxRx
TDH = trotz(theta) @ transl(0,0, d) @ transl(a,0,0) @ trotx(alpha)
#sp.pprint(TDH)
print(type(TDH))

# Declarandola explicitamente
T = sp.Matrix([
    [sp.cos(theta), -sp.sin(theta) * sp.cos(alpha), sp.sin(theta) * sp.sin(alpha), a * sp.cos(theta)],
    [sp.sin(theta), sp.cos(theta) * sp.cos(alpha), -sp.cos(theta) * sp.sin(alpha), a * sp.sin(theta)],
    [0, sp.sin(alpha), sp.cos(alpha), d],
    [0, 0, 0, 1]
])
#sp.pprint(T)
print(type(T))

theta_1, theta_2, theta_3, theta_4, theta_5, theta_6 = sp.symbols('theta_1, theta_2, theta_3, theta_4, theta_5, theta_6')

#Tabla DH
T01 = T.subs({d: 0.78, a: 0.35, alpha: sp.pi/2})
T01 = T01.subs({theta: theta_1})
#sp.pprint(T01)

T12 = T.subs({d: 0, a: 1.145, alpha: 0})
T12 = T12.subs({theta: theta_2}) #theta_2 + sp.pi/2
#sp.pprint(T12)

T23 = T.subs({d: 0, a:0.2, alpha: sp.pi/2})
T23 = T23.subs({theta: theta_3})
#sp.pprint(T23)

T34 = T.subs({d: 1.2125, a: 0, alpha: -sp.pi/2})
T34 = T34.subs({theta: theta_4})
#sp.pprint(T34)

T45 = T.subs({d: 0, a: 0, alpha: sp.pi/2})
T45 = T45.subs({theta: theta_5})
#sp.pprint(T45)

T56 = T.subs({d: 0.22, a: 0, alpha: 0})
T56 = T56.subs({theta: theta_6})
#sp.pprint(T56)

T06 = T01 @ T12 @ T23 @ T34 @ T45 @ T56
T06_s = T06.applyfunc(sp.simplify)
#sp.pprint(T06_s)

#Para modificar ángulos
joint1 = np.deg2rad(0)
joint2 = np.deg2rad(0) + sp.pi/2
joint3 = np.deg2rad(0)
joint4 = np.deg2rad(0)
joint5 = np.deg2rad(0)
joint6 = np.deg2rad(0)

T06_solved = T06.subs({theta_1: joint1, theta_2: joint2, theta_3: joint3, theta_4: joint4, theta_5: joint5, theta_6: joint6})
sp.pprint(T06_solved)