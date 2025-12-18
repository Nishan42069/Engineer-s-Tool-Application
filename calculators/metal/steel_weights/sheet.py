from dataclasses import dataclass

MM_TO_M = 0.001

@dataclass
class SheetInput:
    length_m: float
    width_m: float
    thickness_mm: float
    density_kgm3: float = 7850.0

@dataclass
class SheetOutput:
    area_m2: float
    volume_m3: float
    weight_kg: float

def calculate_sheet(i: SheetInput) -> SheetOutput:
    t = i.thickness_mm * MM_TO_M
    area = i.length_m * i.width_m
    volume = area * t
    weight = volume * i.density_kgm3
    return SheetOutput(area_m2=area, volume_m3=volume, weight_kg=weight)
