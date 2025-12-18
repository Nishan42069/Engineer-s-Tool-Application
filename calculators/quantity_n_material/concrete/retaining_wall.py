# calculators/concrete/retaining_wall.py

from dataclasses import dataclass

FT_TO_M = 0.3048


@dataclass
class RetainingWallInput:
    wall_length_ft: float
    stem_thickness_ft: float
    stem_height_ft: float
    base_width_ft: float
    base_thickness_ft: float
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


def calculate_retaining_wall_concrete(i: RetainingWallInput) -> RetainingWallOutput:
    length_m = i.wall_length_ft * FT_TO_M
    stem_thick_m = i.stem_thickness_ft * FT_TO_M
    stem_h_m = i.stem_height_ft * FT_TO_M
    base_w_m = i.base_width_ft * FT_TO_M
    base_t_m = i.base_thickness_ft * FT_TO_M

    stem_volume_m3 = length_m * stem_thick_m * stem_h_m
    base_volume_m3 = length_m * base_w_m * base_t_m

    total_volume_m3 = stem_volume_m3 + base_volume_m3

    total_parts = i.cement_part + i.sand_part + i.aggregate_part
    if total_parts <= 0:
        raise ValueError("Mix ratio parts must be greater than zero.")

    cement_vol = total_volume_m3 * i.cement_part / total_parts
    sand_vol = total_volume_m3 * i.sand_part / total_parts
    agg_vol = total_volume_m3 * i.aggregate_part / total_parts

    cement_weight_kg = cement_vol * i.density_kgm3
    sand_weight_kg = sand_vol * i.density_kgm3
    aggregate_weight_kg = agg_vol * i.density_kgm3

    total_cost = total_volume_m3 * i.cost_per_m3 if i.cost_per_m3 > 0 else 0.0

    return RetainingWallOutput(
        stem_volume_m3=stem_volume_m3,
        base_volume_m3=base_volume_m3,
        total_volume_m3=total_volume_m3,
        cement_weight_kg=cement_weight_kg,
        sand_weight_kg=sand_weight_kg,
        aggregate_weight_kg=aggregate_weight_kg,
        total_cost=total_cost,
    )
