from dataclasses import dataclass
from typing import Dict

# Base unit = byte
# factor = number of bytes in 1 unit
DATA_UNITS: Dict[str, float] = {
    "byte": 1.0,
    "KB": 1024.0,
    "MB": 1024.0 ** 2,
    "GB": 1024.0 ** 3,
    "TB": 1024.0 ** 4,
}


@dataclass
class DataInput:
    value: float
    from_unit: str
    to_unit: str


@dataclass
class DataOutput:
    value_out: float


def convert_data(i: DataInput) -> DataOutput:
    fu = i.from_unit.strip()
    tu = i.to_unit.strip()

    if fu not in DATA_UNITS:
        raise ValueError(f"Unsupported data unit: {fu}")
    if tu not in DATA_UNITS:
        raise ValueError(f"Unsupported data unit: {tu}")

    # Convert to base unit (bytes)
    value_bytes = i.value * DATA_UNITS[fu]

    # Convert to target unit
    value_out = value_bytes / DATA_UNITS[tu]

    return DataOutput(value_out=value_out)
