from dataclasses import dataclass
from typing import Dict

# Base unit = Pascal (Pa)
PRESSURE_UNITS: Dict[str, float] = {
    "Pa": 1.0,
    "kPa": 1_000.0,
    "MPa": 1_000_000.0,
    "bar": 100_000.0,
    "psi": 6_894.757293,
}

@dataclass
class PressureInput:
    value: float
    from_unit: str
    to_unit: str

@dataclass
class PressureOutput:
    value_out: float

def convert_pressure(i: PressureInput) -> PressureOutput:
    fu = i.from_unit.strip()
    tu = i.to_unit.strip()

    if fu not in PRESSURE_UNITS:
        raise ValueError(f"Unsupported pressure unit: {fu}")
    if tu not in PRESSURE_UNITS:
        raise ValueError(f"Unsupported pressure unit: {tu}")

    value_pa = i.value * PRESSURE_UNITS[fu]
    value_out = value_pa / PRESSURE_UNITS[tu]
    return PressureOutput(value_out=value_out)
