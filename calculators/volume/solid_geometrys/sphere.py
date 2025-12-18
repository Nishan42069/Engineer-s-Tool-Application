from dataclasses import dataclass
import math

@dataclass
class SphereInput:
    radius_m: float

@dataclass
class SphereOutput:
    volume_m3: float
    volume_litre: float

def calculate_sphere(i: SphereInput) -> SphereOutput:
    v = (4.0 / 3.0) * math.pi * (i.radius_m ** 3)
    return SphereOutput(volume_m3=v, volume_litre=v * 1000.0)
