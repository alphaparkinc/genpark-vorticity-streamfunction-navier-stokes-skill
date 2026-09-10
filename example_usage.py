from client import VorticityStreamfunction2D

def main():
    print("=== Testing Vorticity-Streamfunction 2D Navier-Stokes Solver ===")
    ns = VorticityStreamfunction2D(nx=6, ny=6)

    # Induce localized rotational vorticity
    ns.omega[2][2] = 2.0
    ns.omega[3][3] = -2.0

    psi = ns.solve_poisson_jacobi(iterations=15)
    print("Streamfunction field psi after Poisson relaxation:")
    for row in psi:
        print(" ", [round(x, 3) for x in row])

    assert psi[2][2] > 0.0
    assert psi[3][3] < 0.0
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
