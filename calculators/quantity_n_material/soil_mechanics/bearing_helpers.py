import math


def terzaghi_factors(phi_deg: float):
    """Return (Nc, Nq, Nγ) for given φ in degrees (Terzaghi approx)."""
    phi = math.radians(phi_deg)
    if phi <= 0:
        # φ = 0° clay
        Nq = 1.0
        Nc = 5.7
        N_gamma = 0.0
    else:
        Nq = math.e ** (math.pi * math.tan(phi)) * (math.tan(math.radians(45) + phi / 2) ** 2)
        Nc = (Nq - 1.0) / math.tan(phi)
        N_gamma = 2.0 * (Nq + 1.0) * math.tan(phi)
    return Nc, Nq, N_gamma
