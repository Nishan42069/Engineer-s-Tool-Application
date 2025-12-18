from dataclasses import dataclass

@dataclass
class BoxCulvertInput:
    length_ft: float
    width_ft: float
    height_ft: float

def calculate_box_culvert(i: BoxCulvertInput) -> float:
    # Volume of box culvert = length * width * height
    culvert_volume = i.length_ft * i.width_ft * i.height_ft
    return culvert_volume
