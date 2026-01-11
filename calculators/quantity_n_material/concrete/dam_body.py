from dataclasses import dataclass


@dataclass
class DamBodyInput:
    top_width_m: float
    base_width_m: float
    height_m: float
    length_m: float   # longitudinal length of dam

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
    # Trapezoidal cross-section area
    cross_area_m2 = 0.5 * (i.top_width_m + i.base_width_m) * i.height_m
    volume_m3 = cross_area_m2 * i.length_m

    total_parts = i.cement_part + i.sand_part + i.aggregate_part
    if total_parts <= 0:
        raise ValueError("Mix ratio parts must be greater than zero.")

    cement_vol = volume_m3 * i.cement_part / total_parts
    sand_vol = volume_m3 * i.sand_part / total_parts
    agg_vol = volume_m3 * i.aggregate_part / total_parts

    cement_weight = cement_vol * i.density_kgm3
    sand_weight = sand_vol * i.density_kgm3
    aggregate_weight = agg_vol * i.density_kgm3

    total_cost = volume_m3 * i.cost_per_m3 if i.cost_per_m3 > 0 else 0.0

    return DamBodyOutput(
        volume_m3=volume_m3,
        cement_weight_kg=cement_weight,
        sand_weight_kg=sand_weight,
        aggregate_weight_kg=aggregate_weight,
        total_cost=total_cost,
    )
