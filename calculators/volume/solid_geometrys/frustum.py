from dataclasses import dataclass
import math

@dataclass
class FrustumInput:
    radius_top_m: float
    radius_bottom_m: float
    height_m: float

@dataclass
class FrustumOutput:
    volume_m3: float
    volume_litre: float

def calculate_frustum(i: FrustumInput) -> FrustumOutput:
    R = i.radius_bottom_m
    r = i.radius_top_m
    h = i.height_m
    v = (1.0 / 3.0) * math.pi * h * (R*R + R*r + r*r)
    return FrustumOutput(volume_m3=v, volume_litre=v * 1000.0)
