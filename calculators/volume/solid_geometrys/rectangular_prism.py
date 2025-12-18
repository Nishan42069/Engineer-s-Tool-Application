from dataclasses import dataclass

@dataclass
class RectPrismInput:
    length_m: float
    width_m: float
    height_m: float

@dataclass
class RectPrismOutput:
    volume_m3: float
    volume_litre: float

def calculate_rectangular_prism(i: RectPrismInput) -> RectPrismOutput:
    v = i.length_m * i.width_m * i.height_m
    return RectPrismOutput(volume_m3=v, volume_litre=v * 1000.0)
