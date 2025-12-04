import sympy as sp

t = sp.symbols('t')
m, k = sp.symbols('m k', positive=True)

x = sp.Function('x')(t)
xdot = sp.diff(x, t)


#Lagrangian of SHO
L = sp.Rational(1,2) * m * xdot**2 - sp.Rational(1,2) * k * x**2

#Takes partial derivatives
dL_dx = sp.diff(L, x)
dL_dxdot = sp.diff(L, xdot)
d_dt_dL_dxdot = sp.diff(dL_dxdot, t)


#Solves Euler Lagrange equation
EL = sp.simplify(d_dt_dL_dxdot - dL_dx)
print(EL)
