from dataclasses import dataclass

@dataclass
class GabionInput:
    length_ft: float
    width_ft: float
    height_ft: float

def calculate_gabion(i: GabionInput) -> float:
    # Volume of gabion = length * width * height
    gabion_volume = i.length_ft * i.width_ft * i.height_ft
    return gabion_volume
