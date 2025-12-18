from dataclasses import dataclass


@dataclass
class AsphaltInput:
    length_m: float
    width_m: float
    thickness_mm: float
    density_t_m3: float = 2.35


@dataclass
class AsphaltOutput:
    volume_m3: float
    tonnage_t: float


def calculate_asphalt(i: AsphaltInput) -> AsphaltOutput:
    t_m = i.thickness_mm / 1000.0
    V = i.length_m * i.width_m * t_m
    W = V * i.density_t_m3
    return AsphaltOutput(volume_m3=V, tonnage_t=W)
