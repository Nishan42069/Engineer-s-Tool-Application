from dataclasses import dataclass


@dataclass
class PlasterInput:
    area_m2: float
    thickness_mm: float
    cement_part: int
    sand_part: int
    dry_factor: float = 1.3     # to go from wet to dry volume
    cement_density_kg_m3: float = 1440.0
    bag_weight_kg: float = 50.0


@dataclass
class PlasterOutput:
    wet_volume_m3: float
    dry_volume_m3: float
    cement_bags: float
    sand_volume_m3: float


def calculate_plaster(i: PlasterInput) -> PlasterOutput:
    t_m = i.thickness_mm / 1000.0
    wet_vol = i.area_m2 * t_m
    dry_vol = wet_vol * i.dry_factor

    total_parts = i.cement_part + i.sand_part
    if total_parts <= 0:
        raise ValueError("Mix ratio parts must be > 0.")

    cement_vol = dry_vol * i.cement_part / total_parts
    sand_vol = dry_vol * i.sand_part / total_parts

    cement_kg = cement_vol * i.cement_density_kg_m3
    cement_bags = cement_kg / i.bag_weight_kg

    return PlasterOutput(
        wet_volume_m3=wet_vol,
        dry_volume_m3=dry_vol,
        cement_bags=cement_bags,
        sand_volume_m3=sand_vol,
    )
