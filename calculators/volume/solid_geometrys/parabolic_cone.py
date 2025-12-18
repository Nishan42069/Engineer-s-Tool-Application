from dataclasses import dataclass
import math

@dataclass
class ParabolicConeInput:
    radius_m: float
    height_m: float

@dataclass
class ParabolicConeOutput:
    volume_m3: float
    volume_litre: float

def calculate_parabolic_cone(i: ParabolicConeInput) -> ParabolicConeOutput:
    v = 0.5 * math.pi * (i.radius_m ** 2) * i.height_m
    return ParabolicConeOutput(volume_m3=v, volume_litre=v * 1000.0)
