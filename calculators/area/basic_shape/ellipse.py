from dataclasses import dataclass
import math

@dataclass
class EllipseInput:
    semi_major_a_m: float
    semi_minor_b_m: float

@dataclass
class EllipseOutput:
    area_m2: float

def calculate_ellipse(i: EllipseInput) -> EllipseOutput:
    area = math.pi * i.semi_major_a_m * i.semi_minor_b_m
    return EllipseOutput(area_m2=area)
