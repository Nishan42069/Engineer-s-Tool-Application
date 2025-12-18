from dataclasses import dataclass

FT_TO_M = 0.3048
BRICK_WITH_MORTAR_M3 = 0.20 * 0.10 * 0.10
BRICK_SOLID_M3 = 0.19 * 0.09 * 0.09


@dataclass
class ThreeRoomBricksInput:
    room1_length_ft: float
    room1_width_ft: float
    room2_length_ft: float
    room2_width_ft: float
    room3_length_ft: float
    room3_width_ft: float
    wall_height_ft: float
    wall_thickness_ft: float
    waste_percent: float = 5.0
    brick_cost: float = 0.0


@dataclass
class ThreeRoomBricksOutput:
    total_bricks: float
    mortar_m3: float
    total_cost: float


def calculate_three_room_bricks(i: ThreeRoomBricksInput) -> ThreeRoomBricksOutput:
    def perimeter(l_ft: float, b_ft: float) -> float:
        L = l_ft * FT_TO_M
        B = b_ft * FT_TO_M
        return 2.0 * (L + B)

    H = i.wall_height_ft * FT_TO_M
    T = i.wall_thickness_ft * FT_TO_M

    p1 = perimeter(i.room1_length_ft, i.room1_width_ft)
    p2 = perimeter(i.room2_length_ft, i.room2_width_ft)
    p3 = perimeter(i.room3_length_ft, i.room3_width_ft)

    total_perimeter = p1 + p2 + p3
    wall_volume = total_perimeter * H * T

    bricks_raw = wall_volume / BRICK_WITH_MORTAR_M3
    total_bricks = bricks_raw * (1.0 + i.waste_percent / 100.0)

    mortar_m3 = max(wall_volume - bricks_raw * BRICK_SOLID_M3, 0.0)
    total_cost = total_bricks * i.brick_cost if i.brick_cost > 0 else 0.0

    return ThreeRoomBricksOutput(
        total_bricks=total_bricks,
        mortar_m3=mortar_m3,
        total_cost=total_cost,
    )
