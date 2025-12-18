from dataclasses import dataclass

MM_TO_M = 0.001

@dataclass
class SquareBarInput:
    side_mm: float
    length_m: float
    density_kgm3: float = 7850.0

@dataclass
class SquareBarOutput:
    area_m2: float
    volume_m3: float
    weight_kg: float

def calculate_square_bar(i: SquareBarInput) -> SquareBarOutput:
    a = i.side_mm * MM_TO_M
    area = a * a
    volume = area * i.length_m
    weight = volume * i.density_kgm3
    return SquareBarOutput(area_m2=area, volume_m3=volume, weight_kg=weight)
