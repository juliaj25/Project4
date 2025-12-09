def pendulum_problem():
    """
    Problem:
    A point mass m is attached to a massless rod of length l and swings
    in a vertical plane under gravity g. Let θ(t) be the angle from the
    downward vertical.

    (a) Write down the kinetic energy T and potential energy V of the
        pendulum in terms of θ(t), dθ/dt, m, l, and g.

    (b) Form the Lagrangian and derive the equation of motion.

    (c) Use a small-angle approximation to obtain the linearized
        equation of motion.

    """
    t = sp.symbols('t')
    m, l, g = sp.symbols('m l g', positive=True)
    theta = sp.Function('theta')(t)

    # TODO 1: define theta_dot = dθ/dt
    theta_dot = 

    # TODO 2: kinetic energy T of a simple pendulum.
    # Hint: speed v of the mass is v = l * θ_dot
    T = 

    # TODO 3: potential energy V. Take V = 0 at the bottom.
    V = 

    # TODO 4: Lagrangian
    L = T - V

    print("Pendulum Lagrangian L(θ, θ̇):")
    sp.pprint(L)
    print()

    EL = 
    print("Euler–Lagrange equation for the pendulum:")
    sp.pprint(sp.Eq(EL, 0))
    print()

    # For interpretation, divide out the common factor ml:
    EL_simpler = 
    print("Dividing out ml:")
    sp.pprint(sp.Eq(EL_simpler, 0))
    print()

    # TODO 5: Small-angle approximation: replace sin(θ) by θ
    EL_small = 
    print("Small-angle approximation to the equation of motion:")
    sp.pprint(sp.Eq(EL_small, 0))
    print("\nCompare this to the SHO: it should look like θ¨ + (g/ℓ) θ = 0.")
