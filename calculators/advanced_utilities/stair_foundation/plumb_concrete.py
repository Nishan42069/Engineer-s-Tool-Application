from dataclasses import dataclass

@dataclass
class PlumbConcreteInput:
    length_ft: float
    width_ft: float
    thickness_ft: float

def calculate_plumb_concrete(i: PlumbConcreteInput) -> float:
    # Volume of plumb concrete = length * width * thickness
    volume = i.length_ft * i.width_ft * i.thickness_ft
    return volume
