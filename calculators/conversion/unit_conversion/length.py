from dataclasses import dataclass

LENGTH_UNITS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "inch": 0.0254,
    "ft": 0.3048,
    "yard": 0.9144,
    "mile": 1609.344,
}

@dataclass
class LengthInput:
    value: float
    from_unit: str
    to_unit: str

def convert_length(i: LengthInput) -> float:
    base_m = i.value * LENGTH_UNITS[i.from_unit]
    return base_m / LENGTH_UNITS[i.to_unit]
