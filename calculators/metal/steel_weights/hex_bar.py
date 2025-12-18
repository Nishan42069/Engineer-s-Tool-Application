from dataclasses import dataclass
import math

MM_TO_M = 0.001

@dataclass
class HexBarInput:
    across_flats_mm: float
    length_m: float
    density_kgm3: float = 7850.0

@dataclass
class HexBarOutput:
    area_m2: float
    volume_m3: float
    weight_kg: float

def calculate_hex_bar(i: HexBarInput) -> HexBarOutput:
    f = i.across_flats_mm * MM_TO_M
    # Regular hex area with across-flats f: A = (sqrt(3)/2) * f^2
    area = (math.sqrt(3.0) / 2.0) * (f * f)
    volume = area * i.length_m
    weight = volume * i.density_kgm3
    return HexBarOutput(area_m2=area, volume_m3=volume, weight_kg=weight)
