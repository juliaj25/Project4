
"""
Problem statement for the class:

A point mass m is attached to a massless rod of length l and swings
in a vertical plane under gravity g. Let θ(t) be the angle from the
downward vertical.

(a) Write down the kinetic energy T and potential energy V of the
    pendulum in terms of θ(t), dθ/dt, m, l, and g.

(b) Form the Lagrangian L = T − V and use the euler lagrange 
    equation to derive the equation of motion.

(c) Use a small-angle approximation sin θ ≈ θ to obtain the linearized
    equation of motion.

"""
import sympy as sp
t = sp.symbols('t')
m, l, g = sp.symbols('m l g', positive=True)
theta = sp.Function('theta')(t)

# TODO 1: define theta_dot = dθ/dt
theta_dot = 

# TODO 2: kinetic energy T of a simple pendulum.
# Hint: speed v of the mass is v = l * θ_dot
T = 

# TODO 3: potential energy V. Take V = 0 at the bottom.
# A convenient choice is V = m g l (1 − cos θ)
V = 

# TODO 4: Lagrangian
L = T - V

# TODO 5: Solve Euler-Lagrange

dL_dtheta = 
dL_dthetadot = 
d_dt_dL_dthetadot = 

EL = 
print("Euler–Lagrange equation for the pendulum:")
print(EL)

# Divide out the common factor ml
EL_simpler = 
print("Dividing out ml:")
print(EL_simpler)

# TODO 6: Small-angle approximation: replace sin(θ) by θ
EL_small = 
print("Small-angle approximation to the equation of motion:")
print(EL_small)



