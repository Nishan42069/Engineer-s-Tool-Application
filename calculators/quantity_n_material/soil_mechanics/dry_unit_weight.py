from dataclasses import dataclass


@dataclass
class DryUnitWeightInput:
    bulk_unit_weight_kN_m3: float   # γ (kN/m³)
    water_content_percent: float    # w (%)


@dataclass
class DryUnitWeightOutput:
    dry_unit_weight_kN_m3: float    # γ_d (kN/m³)


def calculate_dry_unit_weight(i: DryUnitWeightInput) -> DryUnitWeightOutput:
    w = i.water_content_percent / 100.0
    if (1.0 + w) <= 0:
        raise ValueError("Water content must be greater than -100%.")
    gamma_d = i.bulk_unit_weight_kN_m3 / (1.0 + w)
    return DryUnitWeightOutput(dry_unit_weight_kN_m3=gamma_d)
