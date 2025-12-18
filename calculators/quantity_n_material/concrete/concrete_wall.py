# calculators/concrete/concrete_wall.py

from dataclasses import dataclass

FT_TO_M = 0.3048


@dataclass
class ConcreteWallInput:
    length_ft: float
    height_ft: float
    thickness_ft: float
    cement_part: int
    sand_part: int
    aggregate_part: int
    density_kgm3: float = 2400.0
    cost_per_m3: float = 0.0


@dataclass
class ConcreteWallOutput:
    volume_m3: float
    cement_weight_kg: float
    sand_weight_kg: float
    aggregate_weight_kg: float
    total_cost: float


def calculate_concrete_wall(i: ConcreteWallInput) -> ConcreteWallOutput:
    L_m = i.length_ft * FT_TO_M
    H_m = i.height_ft * FT_TO_M
    t_m = i.thickness_ft * FT_TO_M

    volume_m3 = L_m * H_m * t_m

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

    return ConcreteWallOutput(
        volume_m3=volume_m3,
        cement_weight_kg=cement_weight_kg,
        sand_weight_kg=sand_weight_kg,
        aggregate_weight_kg=aggregate_weight_kg,
        total_cost=total_cost,
    )
