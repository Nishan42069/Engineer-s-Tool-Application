from dataclasses import dataclass

FT_TO_M = 0.3048
BRICK_WITH_MORTAR_M3 = 0.20 * 0.10 * 0.10
BRICK_SOLID_M3 = 0.19 * 0.09 * 0.09


@dataclass
class TwoRoomBricksInput:
    room1_length_ft: float
    room1_width_ft: float
    room2_length_ft: float
    room2_width_ft: float
    wall_height_ft: float
    wall_thickness_ft: float
    waste_percent: float = 5.0
    brick_cost: float = 0.0


@dataclass
class TwoRoomBricksOutput:
    total_bricks: float
    mortar_m3: float
    total_cost: float


def calculate_two_room_bricks(i: TwoRoomBricksInput) -> TwoRoomBricksOutput:
    # Convert all dimensions
    L1 = i.room1_length_ft * FT_TO_M
    B1 = i.room1_width_ft * FT_TO_M
    L2 = i.room2_length_ft * FT_TO_M
    B2 = i.room2_width_ft * FT_TO_M
    H = i.wall_height_ft * FT_TO_M
    T = i.wall_thickness_ft * FT_TO_M

    perimeter1 = 2.0 * (L1 + B1)
    perimeter2 = 2.0 * (L2 + B2)

    total_perimeter = perimeter1 + perimeter2
    wall_volume = total_perimeter * H * T

    bricks_raw = wall_volume / BRICK_WITH_MORTAR_M3
    total_bricks = bricks_raw * (1.0 + i.waste_percent / 100.0)

    mortar_m3 = max(wall_volume - bricks_raw * BRICK_SOLID_M3, 0.0)
    total_cost = total_bricks * i.brick_cost if i.brick_cost > 0 else 0.0

    return TwoRoomBricksOutput(
        total_bricks=total_bricks,
        mortar_m3=mortar_m3,
        total_cost=total_cost,
    )
