from dataclasses import dataclass

MM_TO_M = 0.001

@dataclass
class SquareTubingInput:
    outer_side_mm: float
    thickness_mm: float
    length_m: float
    density_kgm3: float = 7850.0

@dataclass
class SquareTubingOutput:
    area_m2: float
    volume_m3: float
    weight_kg: float

def calculate_square_tubing(i: SquareTubingInput) -> SquareTubingOutput:
    a = i.outer_side_mm * MM_TO_M
    t = i.thickness_mm * MM_TO_M
    ai = max(a - 2.0 * t, 0.0)

    area = a * a - ai * ai
    volume = area * i.length_m
    weight = volume * i.density_kgm3
    return SquareTubingOutput(area_m2=area, volume_m3=volume, weight_kg=weight)
