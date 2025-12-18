from dataclasses import dataclass


@dataclass
class SubmergedUnitWeightInput:
    saturated_unit_weight_kN_m3: float
    gamma_w_kN_m3: float = 9.81


@dataclass
class SubmergedUnitWeightOutput:
    submerged_unit_weight_kN_m3: float


def calculate_submerged_unit_weight(i: SubmergedUnitWeightInput) -> SubmergedUnitWeightOutput:
    gamma_sub = i.saturated_unit_weight_kN_m3 - i.gamma_w_kN_m3
    return SubmergedUnitWeightOutput(submerged_unit_weight_kN_m3=gamma_sub)
