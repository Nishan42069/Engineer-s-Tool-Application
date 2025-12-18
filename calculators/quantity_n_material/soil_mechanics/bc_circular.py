from dataclasses import dataclass
from .bearing_helpers import terzaghi_factors


@dataclass
class BearingCapacityCircularInput:
    cohesion_kPa: float          # c (kPa)
    phi_deg: float               # φ (degrees)
    unit_weight_kN_m3: float     # γ (kN/m³)
    footing_diameter_m: float    # B (m)
    depth_foundation_m: float    # Df (m)
    factor_of_safety: float = 3.0


@dataclass
class BearingCapacityCircularOutput:
    q_ult_kPa: float
    q_allow_kPa: float


def calculate_bearing_capacity_circular(i: BearingCapacityCircularInput) -> BearingCapacityCircularOutput:
    Nc, Nq, N_gamma = terzaghi_factors(i.phi_deg)

    sc, sq, s_gamma = 1.3, 1.2, 0.6
    B = i.footing_diameter_m
    Df = i.depth_foundation_m
    gamma = i.unit_weight_kN_m3

    q_ult = sc * i.cohesion_kPa * Nc + gamma * Df * sq * Nq + 0.5 * gamma * B * s_gamma * N_gamma

    q_allow = q_ult / i.factor_of_safety if i.factor_of_safety > 0 else q_ult

    return BearingCapacityCircularOutput(q_ult_kPa=q_ult, q_allow_kPa=q_allow)
