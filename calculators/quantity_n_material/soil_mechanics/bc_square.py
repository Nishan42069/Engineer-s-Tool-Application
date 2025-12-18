from dataclasses import dataclass
from .bearing_helpers import terzaghi_factors


@dataclass
class BearingCapacitySquareInput:
    cohesion_kPa: float
    phi_deg: float
    unit_weight_kN_m3: float
    footing_width_m: float
    depth_foundation_m: float
    factor_of_safety: float = 3.0


@dataclass
class BearingCapacitySquareOutput:
    q_ult_kPa: float
    q_allow_kPa: float


def calculate_bearing_capacity_square(i: BearingCapacitySquareInput) -> BearingCapacitySquareOutput:
    Nc, Nq, N_gamma = terzaghi_factors(i.phi_deg)

    sc, sq, s_gamma = 1.3, 1.2, 0.8
    B = i.footing_width_m
    Df = i.depth_foundation_m
    gamma = i.unit_weight_kN_m3

    q_ult = sc * i.cohesion_kPa * Nc + gamma * Df * sq * Nq + 0.5 * gamma * B * s_gamma * N_gamma
    q_allow = q_ult / i.factor_of_safety if i.factor_of_safety > 0 else q_ult

    return BearingCapacitySquareOutput(q_ult_kPa=q_ult, q_allow_kPa=q_allow)
