# calculators/concrete/rectangle_tank.py

from dataclasses import dataclass

FT_TO_M = 0.3048


@dataclass
class RectangleTankInput:
    length_ft: float
    width_ft: float
    inner_height_ft: float
    wall_thickness_ft: float
    base_thickness_ft: float
    cement_part: int
    sand_part: int
    aggregate_part: int
    density_kgm3: float = 2400.0
    cost_per_m3: float = 0.0


@dataclass
class RectangleTankOutput:
    wall_volume_m3: float
    base_volume_m3: float
    total_volume_m3: float
    cement_weight_kg: float
    sand_weight_kg: float
    aggregate_weight_kg: float
    total_cost: float


def calculate_rectangle_tank_concrete(i: RectangleTankInput) -> RectangleTankOutput:
    L_m = i.length_ft * FT_TO_M
    B_m = i.width_ft * FT_TO_M
    H_m = i.inner_height_ft * FT_TO_M
    t_wall_m = i.wall_thickness_ft * FT_TO_M
    t_base_m = i.base_thickness_ft * FT_TO_M

    # base slab
    base_volume_m3 = L_m * B_m * t_base_m

    # walls: 2 along L, 2 along B
    wall_volume_long = 2 * (L_m * H_m * t_wall_m)
    wall_volume_short = 2 * (B_m * H_m * t_wall_m)
    wall_volume_m3 = wall_volume_long + wall_volume_short

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

    return RectangleTankOutput(
        wall_volume_m3=wall_volume_m3,
        base_volume_m3=base_volume_m3,
        total_volume_m3=total_volume_m3,
        cement_weight_kg=cement_weight_kg,
        sand_weight_kg=sand_weight_kg,
        aggregate_weight_kg=aggregate_weight_kg,
        total_cost=total_cost,
    )
