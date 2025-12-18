from dataclasses import dataclass
from typing import Dict

# Base unit = radian
# to_rad: multiply value by this factor to get radians
ANGLE_UNITS: Dict[str, float] = {
    "degree": 0.017453292519943295,  # pi/180
    "radian": 1.0,
    "grad": 0.015707963267948967,    # pi/200
}


@dataclass
class AngleInput:
    value: float
    from_unit: str
    to_unit: str


@dataclass
class AngleOutput:
    value_out: float


def convert_angle(i: AngleInput) -> AngleOutput:
    fu = i.from_unit.strip().lower()
    tu = i.to_unit.strip().lower()

    if fu not in ANGLE_UNITS:
        raise ValueError(f"Unsupported angle unit: {i.from_unit}")
    if tu not in ANGLE_UNITS:
        raise ValueError(f"Unsupported angle unit: {i.to_unit}")

    # Convert input → radians
    value_rad = i.value * ANGLE_UNITS[fu]

    # Convert radians → target
    value_out = value_rad / ANGLE_UNITS[tu]

    return AngleOutput(value_out=value_out)
