# calculators/concrete/square_column.py

from dataclasses import dataclass

FT_TO_M = 0.3048


@dataclass
class SquareColumnInput:
    length_ft: float          # column length (height) in feet
    width_ft: float           # column width in feet
    depth_ft: float           # column depth in feet
    cement_part: int          # cement in mix ratio
    sand_part: int            # sand in mix ratio
    aggregate_part: int       # aggregate in mix ratio
    density_kgm3: float = 2400.0
    cost_per_m3: float = 0.0  # Rs/m³ (optional)


@dataclass
class SquareColumnOutput:
    volume_m3: float
    cement_weight_kg: float
    sand_weight_kg: float
    aggregate_weight_kg: float
    total_cost: float


def calculate_square_column_concrete(i: SquareColumnInput) -> SquareColumnOutput:
    # Convert to meters
    length_m = i.length_ft * FT_TO_M
    width_m = i.width_ft * FT_TO_M
    depth_m = i.depth_ft * FT_TO_M

    volume_m3 = length_m * width_m * depth_m

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

    return SquareColumnOutput(
        volume_m3=volume_m3,
        cement_weight_kg=cement_weight_kg,
        sand_weight_kg=sand_weight_kg,
        aggregate_weight_kg=aggregate_weight_kg,
        total_cost=total_cost,
    )
