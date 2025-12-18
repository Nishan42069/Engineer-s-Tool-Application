# calculators/concrete/round_pipe.py

from dataclasses import dataclass
import math

FT_TO_M = 0.3048


@dataclass
class RoundPipeInput:
    outer_diameter_ft: float
    concrete_thickness_ft: float    # thickness of concrete encasement
    length_ft: float
    cement_part: int
    sand_part: int
    aggregate_part: int
    density_kgm3: float = 2400.0
    cost_per_m3: float = 0.0


@dataclass
class RoundPipeOutput:
    volume_m3: float
    cement_weight_kg: float
    sand_weight_kg: float
    aggregate_weight_kg: float
    total_cost: float


def calculate_round_pipe_concrete(i: RoundPipeInput) -> RoundPipeOutput:
    outer_d_m = i.outer_diameter_ft * FT_TO_M
    thick_m = i.concrete_thickness_ft * FT_TO_M
    length_m = i.length_ft * FT_TO_M

    encased_outer_d = outer_d_m + 2 * thick_m

    v_outer = math.pi * (encased_outer_d / 2) ** 2 * length_m
    v_inner = math.pi * (outer_d_m / 2) ** 2 * length_m

    volume_m3 = v_outer - v_inner

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

    return RoundPipeOutput(
        volume_m3=volume_m3,
        cement_weight_kg=cement_weight_kg,
        sand_weight_kg=sand_weight_kg,
        aggregate_weight_kg=aggregate_weight_kg,
        total_cost=total_cost,
    )
