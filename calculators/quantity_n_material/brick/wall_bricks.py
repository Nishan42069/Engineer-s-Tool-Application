from dataclasses import dataclass
from core.materials import MaterialQuantity


@dataclass
class WallBricksInput:
    length_m: float
    height_m: float
    thickness_m: float

    brick_length_m: float = 0.229
    brick_width_m: float = 0.114
    brick_height_m: float = 0.076

    waste_percent: float = 5.0
    brick_unit_cost: float = 0.0
    mortar_unit_cost: float = 0.0


@dataclass
class WallBricksOutput:
    bricks: MaterialQuantity
    mortar: MaterialQuantity
    total_cost: float


def calculate_wall_bricks(i: WallBricksInput) -> WallBricksOutput:
    wall_volume = (
        i.length_m *
        i.height_m *
        i.thickness_m
    )

    brick_volume = (
        i.brick_length_m *
        i.brick_width_m *
        i.brick_height_m
    )

    bricks_raw = wall_volume / brick_volume
    bricks_qty = bricks_raw * (1 + i.waste_percent / 100)

    # Mortar ≈ 25% of masonry volume (site approximation)
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

    return WallBricksOutput(
        bricks=bricks,
        mortar=mortar,
        total_cost=total_cost,
    )
