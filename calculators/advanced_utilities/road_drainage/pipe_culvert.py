from dataclasses import dataclass

@dataclass
class PipeCulvertInput:
    diameter_ft: float
    length_ft: float

def calculate_pipe_culvert(i: PipeCulvertInput) -> float:
    import math
    # Volume of pipe culvert = π * r² * h
    radius_ft = i.diameter_ft / 2
    culvert_volume = math.pi * (radius_ft ** 2) * i.length_ft
    return culvert_volume
