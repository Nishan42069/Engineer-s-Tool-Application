from dataclasses import dataclass
from core.materials import MaterialQuantity

# Standard brick volumes (physical constants)
BRICK_WITH_MORTAR_M3 = 0.20 * 0.10 * 0.10
BRICK_SOLID_M3 = 0.19 * 0.09 * 0.09


@dataclass
class BrickWallSupportInput:
    support_width_m: float
    support_projection_m: float
    support_height_m: float
    number_of_supports: int
    waste_percent: float = 5.0
    brick_unit_cost: float = 0.0
    mortar_unit_cost: float = 0.0


@dataclass
class BrickWallSupportOutput:
    bricks: MaterialQuantity
    mortar: MaterialQuantity
    total_cost: float


def calculate_brick_wall_support(i: BrickWallSupportInput) -> BrickWallSupportOutput:
    volume_single = (
        i.support_width_m *
        i.support_projection_m *
        i.support_height_m
    )

    total_volume = volume_single * max(i.number_of_supports, 0)

    bricks_raw = total_volume / BRICK_WITH_MORTAR_M3
    bricks_qty = bricks_raw * (1 + i.waste_percent / 100)

    mortar_m3 = max(
        total_volume - bricks_raw * BRICK_SOLID_M3,
        0.0
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

    return BrickWallSupportOutput(
        bricks=bricks,
        mortar=mortar,
        total_cost=total_cost,
    )
