from dataclasses import dataclass
from typing import Dict

# Base unit = Joule (J)
WORK_UNITS: Dict[str, float] = {
    "J": 1.0,
    "kJ": 1_000.0,
    "MJ": 1_000_000.0,
    "Wh": 3_600.0,
    "kWh": 3_600_000.0,
}

@dataclass
class WorkInput:
    value: float
    from_unit: str
    to_unit: str

@dataclass
class WorkOutput:
    value_out: float

def convert_work(i: WorkInput) -> WorkOutput:
    fu = i.from_unit.strip()
    tu = i.to_unit.strip()

    if fu not in WORK_UNITS:
        raise ValueError(f"Unsupported work/energy unit: {fu}")
    if tu not in WORK_UNITS:
        raise ValueError(f"Unsupported work/energy unit: {tu}")

    value_j = i.value * WORK_UNITS[fu]
    value_out = value_j / WORK_UNITS[tu]
    return WorkOutput(value_out=value_out)
