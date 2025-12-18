from dataclasses import dataclass
import math

@dataclass
class ConeInput:
    radius_m: float
    height_m: float

@dataclass
class ConeOutput:
    volume_m3: float
    volume_litre: float

def calculate_cone(i: ConeInput) -> ConeOutput:
    v = (1.0 / 3.0) * math.pi * (i.radius_m ** 2) * i.height_m
    return ConeOutput(volume_m3=v, volume_litre=v * 1000.0)
