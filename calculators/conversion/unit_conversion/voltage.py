from dataclasses import dataclass
from typing import Dict

# Base unit = Volt (V)
VOLTAGE_UNITS: Dict[str, float] = {
    "mV": 0.001,
    "V": 1.0,
    "kV": 1000.0,
}

@dataclass
class VoltageInput:
    value: float
    from_unit: str
    to_unit: str

@dataclass
class VoltageOutput:
    value_out: float

def convert_voltage(i: VoltageInput) -> VoltageOutput:
    fu = i.from_unit.strip()
    tu = i.to_unit.strip()

    if fu not in VOLTAGE_UNITS:
        raise ValueError(f"Unsupported voltage unit: {fu}")
    if tu not in VOLTAGE_UNITS:
        raise ValueError(f"Unsupported voltage unit: {tu}")

    value_v = i.value * VOLTAGE_UNITS[fu]
    value_out = value_v / VOLTAGE_UNITS[tu]
    return VoltageOutput(value_out=value_out)
