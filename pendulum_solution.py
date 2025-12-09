"""
Solution
"""
def pendulum_solution():
    t = sp.symbols('t')
    m, l, g = sp.symbols('m l g', positive=True)
    theta = sp.Function('theta')(t)
    theta_dot = sp.diff(theta, t)

    T = sp.Rational(1, 2) * m * l**2 * theta_dot**2
    V = m * g * l * (1 - sp.cos(theta))
    L = T - V

    print("=== Simple pendulum solution ===")
    print("Lagrangian L = T − V:")
    sp.pprint(L)
    print()

    EL = euler_lagrange(L, theta, t)
    print("Euler–Lagrange equation:")
    sp.pprint(sp.Eq(EL, 0))
    print()

    EL_simpler = sp.simplify(EL / (m * l))
    print("Dividing out ml gives:")
    sp.pprint(sp.Eq(EL_simpler, 0))
    print()

    EL_small = sp.simplify(EL_simpler.subs(sp.sin(theta), theta) / l)
    print("Small-angle approximation (sin θ ≈ θ):")
    sp.pprint(sp.Eq(EL_small, 0))
    print("\nThis has the same form as the SHO with ω^2 = g/l.\n")
