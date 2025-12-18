from dataclasses import dataclass
from math import pi

FT_TO_M = 0.3048
BRICK_WITH_MORTAR_M3 = 0.20 * 0.10 * 0.10
BRICK_SOLID_M3 = 0.19 * 0.09 * 0.09


@dataclass
class FullCircleWallInput:
    inner_diameter_ft: float
    wall_thickness_ft: float
    wall_height_ft: float
    waste_percent: float = 5.0
    brick_cost: float = 0.0


@dataclass
class FullCircleWallOutput:
    bricks: float
    mortar_m3: float
    total_cost: float


def calculate_full_circle_wall_bricks(i: FullCircleWallInput) -> FullCircleWallOutput:
    d_inner_m = i.inner_diameter_ft * FT_TO_M
    t_m = i.wall_thickness_ft * FT_TO_M
    h_m = i.wall_height_ft * FT_TO_M

    r_inner = d_inner_m / 2.0
    r_outer = r_inner + t_m

    # Volume of circular ring wall
    volume_m3 = pi * (r_outer**2 - r_inner**2) * h_m

    bricks_raw = volume_m3 / BRICK_WITH_MORTAR_M3
    bricks = bricks_raw * (1.0 + i.waste_percent / 100.0)

    mortar_m3 = max(volume_m3 - bricks_raw * BRICK_SOLID_M3, 0.0)
    total_cost = bricks * i.brick_cost if i.brick_cost > 0 else 0.0

    return FullCircleWallOutput(
        bricks=bricks,
        mortar_m3=mortar_m3,
        total_cost=total_cost,
    )
