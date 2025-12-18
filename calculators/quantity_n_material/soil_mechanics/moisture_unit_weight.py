from dataclasses import dataclass


@dataclass
class MoistureUnitWeightInput:
    dry_unit_weight_kN_m3: float   # γ_d (kN/m³)
    water_content_percent: float   # w (%)


@dataclass
class MoistureUnitWeightOutput:
    bulk_unit_weight_kN_m3: float  # γ (kN/m³)


def calculate_moisture_unit_weight(i: MoistureUnitWeightInput) -> MoistureUnitWeightOutput:
    w = i.water_content_percent / 100.0
    gamma = i.dry_unit_weight_kN_m3 * (1.0 + w)
    return MoistureUnitWeightOutput(bulk_unit_weight_kN_m3=gamma)
