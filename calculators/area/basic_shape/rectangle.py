from dataclasses import dataclass

@dataclass
class RectangleInput:
    length_m: float
    width_m: float

@dataclass
class RectangleOutput:
    area_m2: float

def calculate_rectangle(i: RectangleInput) -> RectangleOutput:
    return RectangleOutput(area_m2=i.length_m * i.width_m)
