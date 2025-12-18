from dataclasses import dataclass

FT_TO_M = 0.3048
BRICK_WITH_MORTAR_M3 = 0.20 * 0.10 * 0.10
BRICK_SOLID_M3 = 0.19 * 0.09 * 0.09


@dataclass
class BrickWallSupportInput:
    support_width_ft: float
    support_projection_ft: float
    support_height_ft: float
    number_of_supports: int
    waste_percent: float = 5.0
    brick_cost: float = 0.0


@dataclass
class BrickWallSupportOutput:
    bricks: float
    mortar_m3: float
    total_cost: float


def calculate_brick_wall_support(i: BrickWallSupportInput) -> BrickWallSupportOutput:
    w = i.support_width_ft * FT_TO_M
    p = i.support_projection_ft * FT_TO_M
    h = i.support_height_ft * FT_TO_M

    volume_single = w * p * h
    total_volume = volume_single * max(i.number_of_supports, 0)

    bricks_raw = total_volume / BRICK_WITH_MORTAR_M3
    bricks = bricks_raw * (1.0 + i.waste_percent / 100.0)

    mortar_m3 = max(total_volume - bricks_raw * BRICK_SOLID_M3, 0.0)
    total_cost = bricks * i.brick_cost if i.brick_cost > 0 else 0.0

    return BrickWallSupportOutput(
        bricks=bricks,
        mortar_m3=mortar_m3,
        total_cost=total_cost,
    )
