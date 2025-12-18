from dataclasses import dataclass
from typing import Dict

# Base unit = m/s
SPEED_UNITS: Dict[str, float] = {
    "m/s": 1.0,
    "km/h": 0.2777777778,
    "mph": 0.44704,
}

@dataclass
class SpeedInput:
    value: float
    from_unit: str
    to_unit: str

@dataclass
class SpeedOutput:
    value_out: float

def convert_speed(i: SpeedInput) -> SpeedOutput:
    fu = i.from_unit.strip()
    tu = i.to_unit.strip()

    if fu not in SPEED_UNITS:
        raise ValueError(f"Unsupported speed unit: {fu}")
    if tu not in SPEED_UNITS:
        raise ValueError(f"Unsupported speed unit: {tu}")

    value_ms = i.value * SPEED_UNITS[fu]
    value_out = value_ms / SPEED_UNITS[tu]
    return SpeedOutput(value_out=value_out)
