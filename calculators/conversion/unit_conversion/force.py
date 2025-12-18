from dataclasses import dataclass
from typing import Dict

# Base unit = Newton (N)
# factor = number of Newtons in 1 unit
FORCE_UNITS: Dict[str, float] = {
    "N": 1.0,
    "kN": 1000.0,
    "kgf": 9.80665,
    "lbf": 4.44822,
}


@dataclass
class ForceInput:
    value: float
    from_unit: str
    to_unit: str


@dataclass
class ForceOutput:
    value_out: float


def convert_force(i: ForceInput) -> ForceOutput:
    fu = i.from_unit.strip()
    tu = i.to_unit.strip()

    if fu not in FORCE_UNITS:
        raise ValueError(f"Unsupported force unit: {fu}")
    if tu not in FORCE_UNITS:
        raise ValueError(f"Unsupported force unit: {tu}")

    # Convert to base unit (Newton)
    value_newton = i.value * FORCE_UNITS[fu]

    # Convert to target unit
    value_out = value_newton / FORCE_UNITS[tu]

    return ForceOutput(value_out=value_out)
