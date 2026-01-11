from dataclasses import dataclass


@dataclass
class RetainingWallInput:
    wall_length_m: float
    stem_thickness_m: float
    stem_height_m: float
    base_width_m: float
    base_thickness_m: float

    cement_part: int
    sand_part: int
    aggregate_part: int

    density_kgm3: float = 2400.0
    cost_per_m3: float = 0.0


@dataclass
class RetainingWallOutput:
    stem_volume_m3: float
    base_volume_m3: float
    total_volume_m3: float
    cement_weight_kg: float
    sand_weight_kg: float
    aggregate_weight_kg: float
    total_cost: float


def calculate_retaining_wall_concrete(
    i: RetainingWallInput,
) -> RetainingWallOutput:
    # Volumes
    stem_volume = i.wall_length_m * i.stem_thickness_m * i.stem_height_m
    base_volume = i.wall_length_m * i.base_width_m * i.base_thickness_m
    total_volume = stem_volume + base_volume

    total_parts = i.cement_part + i.sand_part + i.aggregate_part
    if total_parts <= 0:
        raise ValueError("Mix ratio parts must be greater than zero.")

    cement_vol = total_volume * i.cement_part / total_parts
    sand_vol = total_volume * i.sand_part / total_parts
    aggregate_vol = total_volume * i.aggregate_part / total_parts

    cement_weight = cement_vol * i.density_kgm3
    sand_weight = sand_vol * i.density_kgm3
    aggregate_weight = aggregate_vol * i.density_kgm3

    total_cost = total_volume * i.cost_per_m3 if i.cost_per_m3 > 0 else 0.0

    return RetainingWallOutput(
        stem_volume_m3=stem_volume,
        base_volume_m3=base_volume,
        total_volume_m3=total_volume,
        cement_weight_kg=cement_weight,
        sand_weight_kg=sand_weight,
        aggregate_weight_kg=aggregate_weight,
        total_cost=total_cost,
    )
