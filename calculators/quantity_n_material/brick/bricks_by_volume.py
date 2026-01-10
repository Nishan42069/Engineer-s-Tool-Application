from dataclasses import dataclass
from core.materials import MaterialQuantity


@dataclass
class BricksByVolumeInput:
    wall_length_m: float
    wall_height_m: float
    wall_thickness_m: float

    brick_length_m: float = 0.229
    brick_width_m: float = 0.114
    brick_height_m: float = 0.076

    waste_percent: float = 5.0
    brick_unit_cost: float = 0.0
    mortar_unit_cost: float = 0.0


@dataclass
class BricksByVolumeOutput:
    bricks: MaterialQuantity
    mortar: MaterialQuantity
    total_cost: float


def calculate_bricks_by_volume(i: BricksByVolumeInput) -> BricksByVolumeOutput:
    wall_volume = (
        i.wall_length_m *
        i.wall_height_m *
        i.wall_thickness_m
    )

    brick_volume = (
        i.brick_length_m *
        i.brick_width_m *
        i.brick_height_m
    )

    bricks_raw = wall_volume / brick_volume
    bricks_qty = bricks_raw * (1 + i.waste_percent / 100)

    # Mortar approx 25% of wall volume (industry rule)
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

    return BricksByVolumeOutput(
        bricks=bricks,
        mortar=mortar,
        total_cost=total_cost,
    )
