from dataclasses import dataclass

@dataclass
class PrismInput:
    base_area_m2: float
    length_m: float

@dataclass
class PrismOutput:
    volume_m3: float
    volume_litre: float

def calculate_prism(i: PrismInput) -> PrismOutput:
    v = i.base_area_m2 * i.length_m
    return PrismOutput(volume_m3=v, volume_litre=v * 1000.0)
