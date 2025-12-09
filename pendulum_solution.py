import sympy as sp

t = sp.symbols('t')

m, l, g = sp.symbols('m l g', positive=True)

theta = sp.Function('theta')(t)

theta_dot = sp.diff(theta, t)

T = sp.Rational(1, 2) * m * l**2 * theta_dot**2
V = m * g * l * (1 - sp.cos(theta))
L = T - V


dL_dtheta = sp.diff(L, theta)
dL_dthetadot = sp.diff(L, theta_dot)
d_dt_dL_dthetadot = sp.diff(dL_dthetadot, t)


EL = sp.simplify(d_dt_dL_dthetadot - dL_dtheta)
print("Euler–Lagrange equation:" )
print(EL)

EL_simpler = sp.simplify((EL) / (m * l))
print("Dividing out ml gives:")
print(EL_simpler)

EL_small = sp.simplify(EL_simpler.subs(sp.sin(theta), theta) / l)
print("Small-angle approximation (sin theta approx= theta):")
print(EL_small)

