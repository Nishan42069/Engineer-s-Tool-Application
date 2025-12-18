from dataclasses import dataclass
import math

MM_TO_M = 0.001

@dataclass
class RoundPipeInput:
    outer_diameter_mm: float
    thickness_mm: float
    length_m: float
    density_kgm3: float = 7850.0

@dataclass
class RoundPipeOutput:
    area_m2: float
    volume_m3: float
    weight_kg: float

def calculate_round_pipe(i: RoundPipeInput) -> RoundPipeOutput:
    Do = i.outer_diameter_mm * MM_TO_M
    t = i.thickness_mm * MM_TO_M
    Di = max(Do - 2.0 * t, 0.0)

    area = (math.pi / 4.0) * (Do * Do - Di * Di)
    volume = area * i.length_m
    weight = volume * i.density_kgm3

    return RoundPipeOutput(area_m2=area, volume_m3=volume, weight_kg=weight)
