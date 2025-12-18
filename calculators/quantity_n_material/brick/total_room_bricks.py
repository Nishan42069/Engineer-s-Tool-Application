from dataclasses import dataclass

FT_TO_M = 0.3048

# Approximate brick sizes (including mortar)
BRICK_WITH_MORTAR_M3 = 0.20 * 0.10 * 0.10
BRICK_SOLID_M3 = 0.19 * 0.09 * 0.09


@dataclass
class TotalRoomBricksInput:
    room_length_ft: float
    room_width_ft: float
    wall_height_ft: float
    wall_thickness_ft: float
    waste_percent: float = 5.0
    brick_cost: float = 0.0  # Rs per brick


@dataclass
class TotalRoomBricksOutput:
    total_bricks: float
    mortar_volume_m3: float
    total_cost: float


def calculate_total_room_bricks(i: TotalRoomBricksInput) -> TotalRoomBricksOutput:
    # Convert to meters
    L = i.room_length_ft * FT_TO_M
    B = i.room_width_ft * FT_TO_M
    H = i.wall_height_ft * FT_TO_M
    T = i.wall_thickness_ft * FT_TO_M

    # Approx total wall length = 2(L + B)
    perimeter_m = 2.0 * (L + B)
    wall_volume_m3 = perimeter_m * H * T

    # Brick count (without waste)
    bricks_raw = wall_volume_m3 / BRICK_WITH_MORTAR_M3
    total_bricks = bricks_raw * (1.0 + i.waste_percent / 100.0)

    # Mortar volume (approx)
    mortar_volume_m3 = max(
        wall_volume_m3 - bricks_raw * BRICK_SOLID_M3,
        0.0,
    )

    total_cost = total_bricks * i.brick_cost if i.brick_cost > 0 else 0.0

    return TotalRoomBricksOutput(
        total_bricks=total_bricks,
        mortar_volume_m3=mortar_volume_m3,
        total_cost=total_cost,
    )
