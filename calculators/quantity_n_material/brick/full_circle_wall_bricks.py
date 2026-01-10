from dataclasses import dataclass
from math import pi
from core.materials import MaterialQuantity

BRICK_WITH_MORTAR_M3 = 0.20 * 0.10 * 0.10
BRICK_SOLID_M3 = 0.19 * 0.09 * 0.09


@dataclass
class FullCircleWallInput:
    inner_diameter_m: float
    wall_thickness_m: float
    wall_height_m: float
    waste_percent: float = 5.0
    brick_unit_cost: float = 0.0
    mortar_unit_cost: float = 0.0


@dataclass
class FullCircleWallOutput:
    bricks: MaterialQuantity
    mortar: MaterialQuantity
    total_cost: float


def calculate_full_circle_wall_bricks(
    i: FullCircleWallInput,
) -> FullCircleWallOutput:
    r_inner = i.inner_diameter_m / 2.0
    r_outer = r_inner + i.wall_thickness_m

    # Volume of circular ring wall
    wall_volume = pi * (r_outer**2 - r_inner**2) * i.wall_height_m

    bricks_raw = wall_volume / BRICK_WITH_MORTAR_M3
    bricks_qty = bricks_raw * (1 + i.waste_percent / 100)

    mortar_m3 = max(
        wall_volume - bricks_raw * BRICK_SOLID_M3,
        0.0,
    )

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

    return FullCircleWallOutput(
        bricks=bricks,
        mortar=mortar,
        total_cost=total_cost,
    )
