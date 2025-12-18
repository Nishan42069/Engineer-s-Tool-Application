from dataclasses import dataclass
from typing import Dict

# Base unit = Watt (W)
POWER_UNITS: Dict[str, float] = {
    "W": 1.0,
    "kW": 1_000.0,
    "MW": 1_000_000.0,
    "hp": 745.7,
}

@dataclass
class PowerInput:
    value: float
    from_unit: str
    to_unit: str

@dataclass
class PowerOutput:
    value_out: float

def convert_power(i: PowerInput) -> PowerOutput:
    fu = i.from_unit.strip()
    tu = i.to_unit.strip()

    if fu not in POWER_UNITS:
        raise ValueError(f"Unsupported power unit: {fu}")
    if tu not in POWER_UNITS:
        raise ValueError(f"Unsupported power unit: {tu}")

    value_w = i.value * POWER_UNITS[fu]
    value_out = value_w / POWER_UNITS[tu]
    return PowerOutput(value_out=value_out)
