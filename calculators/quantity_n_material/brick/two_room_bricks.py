from dataclasses import dataclass
from core.materials import MaterialQuantity

BRICK_WITH_MORTAR_M3 = 0.20 * 0.10 * 0.10
BRICK_SOLID_M3 = 0.19 * 0.09 * 0.09


@dataclass
class TwoRoomBricksInput:
    room1_length_m: float
    room1_width_m: float
    room2_length_m: float
    room2_width_m: float
    wall_height_m: float
    wall_thickness_m: float
    waste_percent: float = 5.0
    brick_unit_cost: float = 0.0
    mortar_unit_cost: float = 0.0


@dataclass
class TwoRoomBricksOutput:
    bricks: MaterialQuantity
    mortar: MaterialQuantity
    total_cost: float


def calculate_two_room_bricks(
    i: TwoRoomBricksInput,
) -> TwoRoomBricksOutput:
    def perimeter(length_m: float, width_m: float) -> float:
        return 2.0 * (length_m + width_m)

    p1 = perimeter(i.room1_length_m, i.room1_width_m)
    p2 = perimeter(i.room2_length_m, i.room2_width_m)

    total_perimeter = p1 + p2
    wall_volume = (
        total_perimeter *
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

    return TwoRoomBricksOutput(
        bricks=bricks,
        mortar=mortar,
        total_cost=total_cost,
    )
