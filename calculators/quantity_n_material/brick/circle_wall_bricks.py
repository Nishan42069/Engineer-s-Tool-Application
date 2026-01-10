from dataclasses import dataclass
import math
from core.materials import MaterialQuantity


@dataclass
class CircleWallInput:
    diameter_m: float
    height_m: float
    thickness_m: float

    brick_length_m: float = 0.229
    brick_width_m: float = 0.114
    brick_height_m: float = 0.076

    waste_percent: float = 5.0
    brick_unit_cost: float = 0.0
    mortar_unit_cost: float = 0.0


@dataclass
class CircleWallOutput:
    bricks: MaterialQuantity
    mortar: MaterialQuantity
    total_cost: float


def calculate_circle_wall_bricks(i: CircleWallInput) -> CircleWallOutput:
    circumference = math.pi * i.diameter_m
    wall_volume = circumference * i.height_m * i.thickness_m

    brick_volume = (
        i.brick_length_m *
        i.brick_width_m *
        i.brick_height_m
    )

    bricks_raw = wall_volume / brick_volume
    bricks_qty = bricks_raw * (1 + i.waste_percent / 100)

    # Mortar ≈ 25% of masonry volume (common site approximation)
    mortar_m3 = 0.25 * wall_volume

    bricks = MaterialQuantity(
        quantity=bricks_qty,
        unit="nos",
        unit_cost=i.brick_unit_cost,
    )

    mortar = MaterialQuantity(
        quantity=mortar_m3,
        unit="m³",
        unit_cost=i.mortar_unit_cost,
    )

    total_cost = bricks.total_cost + mortar.total_cost

    return CircleWallOutput(
        bricks=bricks,
        mortar=mortar,
        total_cost=total_cost,
    )
