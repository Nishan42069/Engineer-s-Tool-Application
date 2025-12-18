from dataclasses import dataclass

MM_TO_M = 0.001

@dataclass
class FlatInput:
    width_mm: float
    thickness_mm: float
    length_m: float
    density_kgm3: float = 7850.0

@dataclass
class FlatOutput:
    area_m2: float
    volume_m3: float
    weight_kg: float

def calculate_flat(i: FlatInput) -> FlatOutput:
    w = i.width_mm * MM_TO_M
    t = i.thickness_mm * MM_TO_M
    area = w * t
    volume = area * i.length_m
    weight = volume * i.density_kgm3
    return FlatOutput(area_m2=area, volume_m3=volume, weight_kg=weight)
