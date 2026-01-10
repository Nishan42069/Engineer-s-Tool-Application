from dataclasses import dataclass
from core.materials import MaterialQuantity

BRICK_WITH_MORTAR_M3 = 0.20 * 0.10 * 0.10
BRICK_SOLID_M3 = 0.19 * 0.09 * 0.09


@dataclass
class ArchWallBricksInput:
    wall_length_m: float
    wall_height_m: float
    wall_thickness_m: float
    arch_span_m: float
    arch_rise_m: float
    waste_percent: float = 5.0
    brick_unit_cost: float = 0.0
    mortar_unit_cost: float = 0.0


@dataclass
class ArchWallBricksOutput:
    bricks: MaterialQuantity
    mortar: MaterialQuantity
    total_cost: float


def calculate_arch_wall_bricks(i: ArchWallBricksInput) -> ArchWallBricksOutput:
    wall_volume = i.wall_length_m * i.wall_height_m * i.wall_thickness_m
    arch_area = 0.5 * i.arch_span_m * i.arch_rise_m
    arch_volume = arch_area * i.wall_thickness_m
    net_volume = max(wall_volume - arch_volume, 0.0)

    bricks_raw = net_volume / BRICK_WITH_MORTAR_M3
    bricks_qty = bricks_raw * (1 + i.waste_percent / 100)

    mortar_m3 = max(net_volume - bricks_raw * BRICK_SOLID_M3, 0.0)

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

    return ArchWallBricksOutput(
        bricks=bricks,
        mortar=mortar,
        total_cost=total_cost,
    )
