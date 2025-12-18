# calculators/concrete/dam_body.py

from dataclasses import dataclass

FT_TO_M = 0.3048


@dataclass
class DamBodyInput:
    top_width_ft: float
    base_width_ft: float
    height_ft: float
    length_ft: float            # longitudinal length of dam
    cement_part: int
    sand_part: int
    aggregate_part: int
    density_kgm3: float = 2400.0
    cost_per_m3: float = 0.0


@dataclass
class DamBodyOutput:
    volume_m3: float
    cement_weight_kg: float
    sand_weight_kg: float
    aggregate_weight_kg: float
    total_cost: float


def calculate_dam_body_concrete(i: DamBodyInput) -> DamBodyOutput:
    top_w_m = i.top_width_ft * FT_TO_M
    base_w_m = i.base_width_ft * FT_TO_M
    height_m = i.height_ft * FT_TO_M
    length_m = i.length_ft * FT_TO_M

    # Trapezoidal cross-section area
    cross_area_m2 = 0.5 * (top_w_m + base_w_m) * height_m
    volume_m3 = cross_area_m2 * length_m

    total_parts = i.cement_part + i.sand_part + i.aggregate_part
    if total_parts <= 0:
        raise ValueError("Mix ratio parts must be greater than zero.")

    cement_vol = volume_m3 * i.cement_part / total_parts
    sand_vol = volume_m3 * i.sand_part / total_parts
    agg_vol = volume_m3 * i.aggregate_part / total_parts

    cement_weight_kg = cement_vol * i.density_kgm3
    sand_weight_kg = sand_vol * i.density_kgm3
    aggregate_weight_kg = agg_vol * i.density_kgm3

    total_cost = volume_m3 * i.cost_per_m3 if i.cost_per_m3 > 0 else 0.0

    return DamBodyOutput(
        volume_m3=volume_m3,
        cement_weight_kg=cement_weight_kg,
        sand_weight_kg=sand_weight_kg,
        aggregate_weight_kg=aggregate_weight_kg,
        total_cost=total_cost,
    )
