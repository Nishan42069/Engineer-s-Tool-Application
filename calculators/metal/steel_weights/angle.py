from dataclasses import dataclass

MM_TO_M = 0.001

@dataclass
class AngleInput:
    leg_a_mm: float     # a
    leg_b_mm: float     # b
    thickness_mm: float # t
    length_m: float
    density_kgm3: float = 7850.0

@dataclass
class AngleOutput:
    area_m2: float
    volume_m3: float
    weight_kg: float

def calculate_angle(i: AngleInput) -> AngleOutput:
    a = i.leg_a_mm * MM_TO_M
    b = i.leg_b_mm * MM_TO_M
    t = i.thickness_mm * MM_TO_M

    # area ≈ a*t + b*t - t*t (overlap)
    area = (a * t) + (b * t) - (t * t)

    volume = area * i.length_m
    weight = volume * i.density_kgm3
    return AngleOutput(area_m2=area, volume_m3=volume, weight_kg=weight)
