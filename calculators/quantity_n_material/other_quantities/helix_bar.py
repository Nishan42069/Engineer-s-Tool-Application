from dataclasses import dataclass
import math


@dataclass
class HelixBarInput:
    core_diameter_mm: float      # diameter to helix centre
    pitch_mm: float              # vertical spacing
    column_height_mm: float      # height of helix
    bar_diameter_mm: float       # helix bar dia
    extra_length_mm: float = 0.0 # hooks, overlap, etc.


@dataclass
class HelixBarOutput:
    turns: float
    bar_length_m: float
    unit_weight_kg_per_m: float
    total_weight_kg: float


def calculate_helix_bar(i: HelixBarInput) -> HelixBarOutput:
    if i.pitch_mm <= 0:
        raise ValueError("Pitch must be greater than zero.")
    if i.core_diameter_mm <= 0:
        raise ValueError("Core diameter must be greater than zero.")

    turns = i.column_height_mm / i.pitch_mm
    D_m = i.core_diameter_mm / 1000.0
    p_m = i.pitch_mm / 1000.0

    length_per_turn = math.sqrt((math.pi * D_m) ** 2 + p_m ** 2)
    extra_m = i.extra_length_mm / 1000.0
    total_length_m = turns * length_per_turn + extra_m

    unit_w = (i.bar_diameter_mm ** 2) / 162000.0  # kg/m (d^2/162, but mm to m)
    total_w = total_length_m * unit_w

    return HelixBarOutput(
        turns=turns,
        bar_length_m=total_length_m,
        unit_weight_kg_per_m=unit_w,
        total_weight_kg=total_w,
    )
