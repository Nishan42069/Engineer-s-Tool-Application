from dataclasses import dataclass
from typing import Dict

# Base unit = liter
# factor = liters in 1 unit
FUEL_UNITS: Dict[str, float] = {
    "liter": 1.0,
    "ml": 0.001,
    "gallon": 3.78541,   # US gallon
}


@dataclass
class FuelInput:
    value: float
    from_unit: str
    to_unit: str


@dataclass
class FuelOutput:
    value_out: float


def convert_fuel(i: FuelInput) -> FuelOutput:
    fu = i.from_unit.strip()
    tu = i.to_unit.strip()

    if fu not in FUEL_UNITS:
        raise ValueError(f"Unsupported fuel unit: {fu}")
    if tu not in FUEL_UNITS:
        raise ValueError(f"Unsupported fuel unit: {tu}")

    # Convert to base unit (liter)
    value_liter = i.value * FUEL_UNITS[fu]

    # Convert to target unit
    value_out = value_liter / FUEL_UNITS[tu]

    return FuelOutput(value_out=value_out)
