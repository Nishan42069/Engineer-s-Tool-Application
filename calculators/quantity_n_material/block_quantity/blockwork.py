from dataclasses import dataclass
from core.materials import MaterialQuantity


@dataclass
class BlockworkInput:
    wall_length_m: float
    wall_height_m: float
    wall_thickness_m: float

    block_length_m: float
    block_height_m: float
    block_thickness_m: float

    waste_percent: float = 5.0
    mortar_ratio_percent: float = 25.0
    block_unit_cost: float = 0.0
    mortar_unit_cost: float = 0.0


@dataclass
class BlockworkOutput:
    blocks: MaterialQuantity
    mortar: MaterialQuantity
    total_cost: float


def calculate_blockwork(i: BlockworkInput) -> BlockworkOutput:
    wall_volume = (
        i.wall_length_m *
        i.wall_height_m *
        i.wall_thickness_m
    )

    block_volume = (
        i.block_length_m *
        i.block_height_m *
        i.block_thickness_m
    )

    if block_volume <= 0:
        raise ValueError("Block dimensions must be greater than zero.")

    blocks_raw = wall_volume / block_volume
    blocks_qty = blocks_raw * (1 + i.waste_percent / 100)

    mortar_m3 = wall_volume * (i.mortar_ratio_percent / 100)

    blocks = MaterialQuantity(
        quantity=blocks_qty,
        unit="nos",
        unit_cost=i.block_unit_cost,
    )

    mortar = MaterialQuantity(
        quantity=mortar_m3,
        unit="m³",
        unit_cost=i.mortar_unit_cost,
    )

    total_cost = blocks.total_cost + mortar.total_cost

    return BlockworkOutput(
        blocks=blocks,
        mortar=mortar,
        total_cost=total_cost,
    )
