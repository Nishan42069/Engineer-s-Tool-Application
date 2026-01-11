from dataclasses import dataclass
import math


@dataclass
class RoundPipeInput:
    outer_diameter_m: float
    encasement_thickness_m: float
    length_m: float

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


def calculate_round_pipe_concrete(
    i: RoundPipeInput,
) -> RoundPipeOutput:
    outer_radius = i.outer_diameter_m / 2.0
    encased_radius = outer_radius + i.encasement_thickness_m

    v_outer = math.pi * encased_radius**2 * i.length_m
    v_inner = math.pi * outer_radius**2 * i.length_m

    volume_m3 = max(v_outer - v_inner, 0.0)

    total_parts = i.cement_part + i.sand_part + i.aggregate_part
    if total_parts <= 0:
        raise ValueError("Mix ratio parts must be greater than zero.")

    cement_vol = volume_m3 * i.cement_part / total_parts
    sand_vol = volume_m3 * i.sand_part / total_parts
    aggregate_vol = volume_m3 * i.aggregate_part / total_parts

    cement_weight = cement_vol * i.density_kgm3
    sand_weight = sand_vol * i.density_kgm3
    aggregate_weight = aggregate_vol * i.density_kgm3

    total_cost = volume_m3 * i.cost_per_m3 if i.cost_per_m3 > 0 else 0.0

    return RoundPipeOutput(
        volume_m3=volume_m3,
        cement_weight_kg=cement_weight,
        sand_weight_kg=sand_weight,
        aggregate_weight_kg=aggregate_weight,
        total_cost=total_cost,
    )
