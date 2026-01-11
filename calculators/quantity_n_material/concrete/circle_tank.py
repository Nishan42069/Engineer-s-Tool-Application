from dataclasses import dataclass
import math


@dataclass
class CircleTankInput:
    inner_diameter_m: float
    wall_thickness_m: float
    wall_height_m: float
    base_thickness_m: float

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
    outer_diameter_m = i.inner_diameter_m + 2 * i.wall_thickness_m

    outer_area = math.pi * (outer_diameter_m / 2) ** 2
    inner_area = math.pi * (i.inner_diameter_m / 2) ** 2

    wall_volume = (outer_area - inner_area) * i.wall_height_m
    base_volume = outer_area * i.base_thickness_m

    total_volume = wall_volume + base_volume

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

    return CircleTankOutput(
        wall_volume_m3=wall_volume,
        base_volume_m3=base_volume,
        total_volume_m3=total_volume,
        cement_weight_kg=cement_weight,
        sand_weight_kg=sand_weight,
        aggregate_weight_kg=aggregate_weight,
        total_cost=total_cost,
    )
