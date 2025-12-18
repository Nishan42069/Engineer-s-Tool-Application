from dataclasses import dataclass
import math

@dataclass
class HalfSphereInput:
    radius_m: float

@dataclass
class HalfSphereOutput:
    volume_m3: float
    volume_litre: float

def calculate_half_sphere(i: HalfSphereInput) -> HalfSphereOutput:
    v = (2.0 / 3.0) * math.pi * (i.radius_m ** 3)
    return HalfSphereOutput(volume_m3=v, volume_litre=v * 1000.0)
