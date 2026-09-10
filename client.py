class VorticityStreamfunction2D:
    """
    2D Navier-Stokes Vorticity-Streamfunction Solver.
    Poisson equation: d^2 psi / dx^2 + d^2 psi / dy^2 = -omega.
    """
    def __init__(self, nx=6, ny=6, dx=1.0):
        self.nx = nx
        self.ny = ny
        self.dx = dx
        self.psi = [[0.0]*ny for _ in range(nx)]
        self.omega = [[0.0]*ny for _ in range(nx)]

    def solve_poisson_jacobi(self, iterations=10):
        dx2 = self.dx * self.dx
        for _ in range(iterations):
            new_psi = [row[:] for row in self.psi]
            for i in range(1, self.nx - 1):
                for j in range(1, self.ny - 1):
                    new_psi[i][j] = 0.25 * (self.psi[i+1][j] + self.psi[i-1][j] +
                                            self.psi[i][j+1] + self.psi[i][j-1] +
                                            dx2 * self.omega[i][j])
            self.psi = new_psi
        return self.psi
