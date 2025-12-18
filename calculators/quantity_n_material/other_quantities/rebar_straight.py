from dataclasses import dataclass


@dataclass
class RebarStraightInput:
    bar_diameter_mm: float
    bar_length_m: float
    number_of_bars: int


@dataclass
class RebarStraightOutput:
    total_length_m: float
    unit_weight_kg_m: float
    total_weight_kg: float


def calculate_rebar_straight(i: RebarStraightInput) -> RebarStraightOutput:
    total_len = i.bar_length_m * i.number_of_bars
    unit_w = (i.bar_diameter_mm ** 2) / 162000.0  # kg/m
    total_w = total_len * unit_w

    return RebarStraightOutput(
        total_length_m=total_len,
        unit_weight_kg_m=unit_w,
        total_weight_kg=total_w,
    )
