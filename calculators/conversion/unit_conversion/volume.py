from dataclasses import dataclass

VOLUME_UNITS = {
    "cc": 1e-6,
    "liter": 0.001,
    "m³": 1.0,
    "cu.ft": 0.0283168,
    "cu.in": 1.6387e-5,
    "gallon (US)": 0.00378541,
}

@dataclass
class VolumeInput:
    value: float
    from_unit: str
    to_unit: str

def convert_volume(i: VolumeInput) -> float:
    base = i.value * VOLUME_UNITS[i.from_unit]
    return base / VOLUME_UNITS[i.to_unit]
