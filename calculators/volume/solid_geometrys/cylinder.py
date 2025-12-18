from dataclasses import dataclass
import math

@dataclass
class CylinderInput:
    radius_m: float
    height_m: float

@dataclass
class CylinderOutput:
    volume_m3: float
    volume_litre: float

def calculate_cylinder(i: CylinderInput) -> CylinderOutput:
    v = math.pi * (i.radius_m ** 2) * i.height_m
    return CylinderOutput(volume_m3=v, volume_litre=v * 1000.0)
