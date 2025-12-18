from dataclasses import dataclass

@dataclass
class TriangleInput:
    base_m: float
    height_m: float

@dataclass
class TriangleOutput:
    area_m2: float

def calculate_triangle(i: TriangleInput) -> TriangleOutput:
    return TriangleOutput(area_m2=0.5 * i.base_m * i.height_m)
