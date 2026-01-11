from dataclasses import dataclass


@dataclass
class RectangleTankInput:
    length_m: float
    width_m: float
    inner_height_m: float
    wall_thickness_m: float
    base_thickness_m: float

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


def calculate_rectangle_tank_concrete(
    i: RectangleTankInput,
) -> RectangleTankOutput:
    # Base slab
    base_volume = i.length_m * i.width_m * i.base_thickness_m

    # Walls (2 long + 2 short)
    wall_volume_long = 2 * (i.length_m * i.inner_height_m * i.wall_thickness_m)
    wall_volume_short = 2 * (i.width_m * i.inner_height_m * i.wall_thickness_m)
    wall_volume = wall_volume_long + wall_volume_short

    total_volume = base_volume + wall_volume

    total_parts = i.cement_part + i.sand_part + i.aggregate_part
    if total_parts <= 0:
        raise ValueError("Mix ratio parts must be greater than zero.")

    cement_vol = total_volume * i.cement_part / total_parts
    sand_vol = total_volume * i.sand_part / total_parts
    agg_vol = total_volume * i.aggregate_part / total_parts

    cement_weight = cement_vol * i.density_kgm3
    sand_weight = sand_vol * i.density_kgm3
    aggregate_weight = agg_vol * i.density_kgm3

    total_cost = total_volume * i.cost_per_m3 if i.cost_per_m3 > 0 else 0.0

    return RectangleTankOutput(
        wall_volume_m3=wall_volume,
        base_volume_m3=base_volume,
        total_volume_m3=total_volume,
        cement_weight_kg=cement_weight,
        sand_weight_kg=sand_weight,
        aggregate_weight_kg=aggregate_weight,
        total_cost=total_cost,
    )
