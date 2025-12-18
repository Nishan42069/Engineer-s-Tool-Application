from dataclasses import dataclass

GAMMA_W_KN_M3 = 9.81  # unit weight of water


@dataclass
class SaturatedUnitWeightInput:
    specific_gravity: float  # Gs
    void_ratio: float        # e
    gamma_w_kN_m3: float = GAMMA_W_KN_M3


@dataclass
class SaturatedUnitWeightOutput:
    saturated_unit_weight_kN_m3: float


def calculate_saturated_unit_weight(i: SaturatedUnitWeightInput) -> SaturatedUnitWeightOutput:
    if (1.0 + i.void_ratio) <= 0:
        raise ValueError("Void ratio + 1 must be > 0.")
    gamma_sat = (i.specific_gravity + i.void_ratio) / (1.0 + i.void_ratio) * i.gamma_w_kN_m3
    return SaturatedUnitWeightOutput(saturated_unit_weight_kN_m3=gamma_sat)
