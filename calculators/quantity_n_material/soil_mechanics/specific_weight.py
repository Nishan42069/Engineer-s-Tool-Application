from dataclasses import dataclass


@dataclass
class SpecificWeightInput:
    weight_kN: float
    volume_m3: float


@dataclass
class SpecificWeightOutput:
    unit_weight_kN_m3: float


def calculate_specific_weight(i: SpecificWeightInput) -> SpecificWeightOutput:
    if i.volume_m3 <= 0:
        raise ValueError("Volume must be greater than zero.")
    gamma = i.weight_kN / i.volume_m3
    return SpecificWeightOutput(unit_weight_kN_m3=gamma)
