from dataclasses import dataclass

AREA_UNITS = {
    "sq.mm": 1e-6,
    "sq.cm": 1e-4,
    "sq.m": 1.0,
    "sq.km": 1e6,
    "sq.ft": 0.092903,
    "sq.yard": 0.836127,
    "acre": 4046.856,
    "hectare": 10000.0,
}

@dataclass
class AreaInput:
    value: float
    from_unit: str
    to_unit: str

def convert_area(i: AreaInput) -> float:
    base = i.value * AREA_UNITS[i.from_unit]
    return base / AREA_UNITS[i.to_unit]
