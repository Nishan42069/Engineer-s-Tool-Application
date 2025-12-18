from dataclasses import dataclass
import math

MM_TO_M = 0.001

@dataclass
class RoundBarInput:
    diameter_mm: float
    length_m: float
    density_kgm3: float = 7850.0

@dataclass
class RoundBarOutput:
    area_m2: float
    volume_m3: float
    weight_kg: float

def calculate_round_bar(i: RoundBarInput) -> RoundBarOutput:
    d = i.diameter_mm * MM_TO_M
    r = d / 2.0
    area = math.pi * r * r
    volume = area * i.length_m
    weight = volume * i.density_kgm3
    return RoundBarOutput(area_m2=area, volume_m3=volume, weight_kg=weight)
