from dataclasses import dataclass
import math

@dataclass
class CircleInput:
    radius_m: float

@dataclass
class CircleOutput:
    area_m2: float

def calculate_circle(i: CircleInput) -> CircleOutput:
    area = math.pi * (i.radius_m ** 2)
    return CircleOutput(area_m2=area)
