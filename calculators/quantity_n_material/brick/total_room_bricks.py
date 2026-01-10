from dataclasses import dataclass
from core.materials import MaterialQuantity

BRICK_WITH_MORTAR_M3 = 0.20 * 0.10 * 0.10
BRICK_SOLID_M3 = 0.19 * 0.09 * 0.09


@dataclass
class TotalRoomBricksInput:
    room_length_m: float
    room_width_m: float
    wall_height_m: float
    wall_thickness_m: float
    waste_percent: float = 5.0
    brick_unit_cost: float = 0.0
    mortar_unit_cost: float = 0.0


@dataclass
class TotalRoomBricksOutput:
    bricks: MaterialQuantity
    mortar: MaterialQuantity
    total_cost: float


def calculate_total_room_bricks(
    i: TotalRoomBricksInput,
) -> TotalRoomBricksOutput:
    # Total wall perimeter
    perimeter_m = 2.0 * (i.room_length_m + i.room_width_m)

    wall_volume = (
        perimeter_m *
        i.wall_height_m *
        i.wall_thickness_m
    )

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

    return TotalRoomBricksOutput(
        bricks=bricks,
        mortar=mortar,
        total_cost=total_cost,
    )
