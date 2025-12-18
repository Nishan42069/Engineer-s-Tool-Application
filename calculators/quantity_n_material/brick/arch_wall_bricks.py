from dataclasses import dataclass

FT_TO_M = 0.3048
BRICK_WITH_MORTAR_M3 = 0.20 * 0.10 * 0.10
BRICK_SOLID_M3 = 0.19 * 0.09 * 0.09


@dataclass
class ArchWallBricksInput:
    wall_length_ft: float
    wall_height_ft: float
    wall_thickness_ft: float
    arch_span_ft: float
    arch_rise_ft: float
    waste_percent: float = 5.0
    brick_cost: float = 0.0


@dataclass
class ArchWallBricksOutput:
    bricks: float
    mortar_m3: float
    total_cost: float


def calculate_arch_wall_bricks(i: ArchWallBricksInput) -> ArchWallBricksOutput:
    L = i.wall_length_ft * FT_TO_M
    H = i.wall_height_ft * FT_TO_M
    T = i.wall_thickness_ft * FT_TO_M
    span = i.arch_span_ft * FT_TO_M
    rise = i.arch_rise_ft * FT_TO_M

    wall_volume = L * H * T

    # Approx arch opening area as 0.5 * span * rise
    arch_area = 0.5 * span * rise
    arch_volume = arch_area * T

    net_volume = max(wall_volume - arch_volume, 0.0)

    bricks_raw = net_volume / BRICK_WITH_MORTAR_M3
    bricks = bricks_raw * (1.0 + i.waste_percent / 100.0)

    mortar_m3 = max(net_volume - bricks_raw * BRICK_SOLID_M3, 0.0)
    total_cost = bricks * i.brick_cost if i.brick_cost > 0 else 0.0

    return ArchWallBricksOutput(
        bricks=bricks,
        mortar_m3=mortar_m3,
        total_cost=total_cost,
    )
