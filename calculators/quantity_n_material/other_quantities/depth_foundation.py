from dataclasses import dataclass


@dataclass
class DepthFoundationInput:
    allowable_bearing_kPa: float
    unit_weight_kN_m3: float
    factor_of_safety: float = 1.0


@dataclass
class DepthFoundationOutput:
    depth_m: float


def calculate_depth_foundation(i: DepthFoundationInput) -> DepthFoundationOutput:
    if i.unit_weight_kN_m3 <= 0:
        raise ValueError("Unit weight must be > 0.")
    q = i.allowable_bearing_kPa / i.factor_of_safety if i.factor_of_safety > 0 else i.allowable_bearing_kPa
    D = q / i.unit_weight_kN_m3
    return DepthFoundationOutput(depth_m=D)
