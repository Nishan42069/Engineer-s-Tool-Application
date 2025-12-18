from dataclasses import dataclass
import math

FT_TO_M = 0.3048


@dataclass
class CircleWallInput:
    diameter_ft: float
    height_ft: float
    thickness_ft: float
    brick_l: float = 0.229
    brick_w: float = 0.114
    brick_h: float = 0.076
    waste_percent: float = 5.0
    brick_cost: float = 0.0


@dataclass
class CircleWallOutput:
    bricks: float
    mortar_m3: float
    total_cost: float


def calculate_circle_wall_bricks(i: CircleWallInput) -> CircleWallOutput:
    D = i.diameter_ft * FT_TO_M
    H = i.height_ft * FT_TO_M
    T = i.thickness_ft * FT_TO_M

    circumference = math.pi * D
    wall_vol = circumference * H * T
    brick_vol = i.brick_l * i.brick_w * i.brick_h

    bricks = wall_vol / brick_vol
    bricks *= 1 + i.waste_percent / 100

    mortar = wall_vol * 0.25
    total_cost = bricks * i.brick_cost if i.brick_cost > 0 else 0

    return CircleWallOutput(bricks, mortar, total_cost)
