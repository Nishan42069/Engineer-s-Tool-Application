# calculators/concrete/circle_tank.py

from dataclasses import dataclass
import math

FT_TO_M = 0.3048


@dataclass
class CircleTankInput:
    inner_diameter_ft: float
    wall_thickness_ft: float
    wall_height_ft: float
    base_thickness_ft: float
    cement_part: int
    sand_part: int
    aggregate_part: int
    density_kgm3: float = 2400.0
    cost_per_m3: float = 0.0


@dataclass
class CircleTankOutput:
    wall_volume_m3: float
    base_volume_m3: float
    total_volume_m3: float
    cement_weight_kg: float
    sand_weight_kg: float
    aggregate_weight_kg: float
    total_cost: float


def calculate_circle_tank_concrete(i: CircleTankInput) -> CircleTankOutput:
    inner_d_m = i.inner_diameter_ft * FT_TO_M
    wall_thick_m = i.wall_thickness_ft * FT_TO_M
    wall_h_m = i.wall_height_ft * FT_TO_M
    base_t_m = i.base_thickness_ft * FT_TO_M

    outer_d_m = inner_d_m + 2 * wall_thick_m

    # Wall volume ≈ (area_outer - area_inner) * height
    outer_area = math.pi * (outer_d_m / 2) ** 2
    inner_area = math.pi * (inner_d_m / 2) ** 2
    wall_volume_m3 = (outer_area - inner_area) * wall_h_m

    # Base slab volume = outer area * base thickness (using outer diameter)
    base_volume_m3 = outer_area * base_t_m

    total_volume_m3 = wall_volume_m3 + base_volume_m3

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

    return CircleTankOutput(
        wall_volume_m3=wall_volume_m3,
        base_volume_m3=base_volume_m3,
        total_volume_m3=total_volume_m3,
        cement_weight_kg=cement_weight_kg,
        sand_weight_kg=sand_weight_kg,
        aggregate_weight_kg=aggregate_weight_kg,
        total_cost=total_cost,
    )
