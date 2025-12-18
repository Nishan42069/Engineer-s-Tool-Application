from dataclasses import dataclass


@dataclass
class BedVolumeInput:
    length_m: float
    width_m: float
    depth_m: float
    bulk_density_kN_m3: float = 0.0  # optional, for weight


@dataclass
class BedVolumeOutput:
    volume_m3: float
    weight_kN: float


def calculate_bed_volume(i: BedVolumeInput) -> BedVolumeOutput:
    vol = i.length_m * i.width_m * i.depth_m
    weight = vol * i.bulk_density_kN_m3 if i.bulk_density_kN_m3 > 0 else 0.0
    return BedVolumeOutput(volume_m3=vol, weight_kN=weight)
