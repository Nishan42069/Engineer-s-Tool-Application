from dataclasses import dataclass
from typing import Dict

# Base unit = second (sec)
TIME_UNITS: Dict[str, float] = {
    "sec": 1.0,
    "min": 60.0,
    "hour": 3600.0,
    "day": 86400.0,
}

@dataclass
class TimeInput:
    value: float
    from_unit: str
    to_unit: str

@dataclass
class TimeOutput:
    value_out: float

def convert_time(i: TimeInput) -> TimeOutput:
    fu = i.from_unit.strip()
    tu = i.to_unit.strip()

    if fu not in TIME_UNITS:
        raise ValueError(f"Unsupported time unit: {fu}")
    if tu not in TIME_UNITS:
        raise ValueError(f"Unsupported time unit: {tu}")

    value_sec = i.value * TIME_UNITS[fu]
    value_out = value_sec / TIME_UNITS[tu]
    return TimeOutput(value_out=value_out)
