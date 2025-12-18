from dataclasses import dataclass

FT_TO_M = 0.3048


@dataclass
class BricksByVolumeInput:
    wall_length_ft: float
    wall_height_ft: float
    wall_thickness_ft: float
    brick_length_m: float = 0.229
    brick_width_m: float = 0.114
    brick_height_m: float = 0.076
    mortar_ratio_c: int = 1
    mortar_ratio_s: int = 4
    waste_percent: float = 5.0
    brick_cost: float = 0.0   # cost per brick


@dataclass
class BricksByVolumeOutput:
    total_bricks: float
    mortar_volume_m3: float
    total_cost: float


def calculate_bricks_by_volume(i: BricksByVolumeInput) -> BricksByVolumeOutput:
    L = i.wall_length_ft * FT_TO_M
    H = i.wall_height_ft * FT_TO_M
    T = i.wall_thickness_ft * FT_TO_M

    wall_volume = L * H * T
    brick_volume = i.brick_length_m * i.brick_width_m * i.brick_height_m

    bricks_required = wall_volume / brick_volume
    bricks_required *= (1 + i.waste_percent / 100)

    # Mortar approx 25% of wall volume (industry rule)
    mortar_volume = 0.25 * wall_volume

    total_cost = bricks_required * i.brick_cost if i.brick_cost > 0 else 0.0

    return BricksByVolumeOutput(
        total_bricks=bricks_required,
        mortar_volume_m3=mortar_volume,
        total_cost=total_cost,
    )
