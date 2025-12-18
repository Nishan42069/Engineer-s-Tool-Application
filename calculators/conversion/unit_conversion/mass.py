from dataclasses import dataclass
from typing import Dict

# Base unit = kilogram (kg)
WEIGHT_UNITS: Dict[str, float] = {
    "mg": 1e-6,
    "g": 1e-3,
    "kg": 1.0,
    "tonne": 1000.0,
    "lb": 0.45359237,
}

@dataclass
class WeightInput:
    value: float
    from_unit: str
    to_unit: str

@dataclass
class WeightOutput:
    value_out: float

def convert_weight(i: WeightInput) -> WeightOutput:
    fu = i.from_unit.strip()
    tu = i.to_unit.strip()

    if fu not in WEIGHT_UNITS:
        raise ValueError(f"Unsupported weight unit: {fu}")
    if tu not in WEIGHT_UNITS:
        raise ValueError(f"Unsupported weight unit: {tu}")

    value_kg = i.value * WEIGHT_UNITS[fu]
    value_out = value_kg / WEIGHT_UNITS[tu]
    return WeightOutput(value_out=value_out)
