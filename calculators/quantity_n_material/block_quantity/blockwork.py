from dataclasses import dataclass

FT_TO_M = 0.3048
MM_TO_M = 0.001


@dataclass
class BlockworkInput:
    wall_length_ft: float
    wall_height_ft: float
    wall_thickness_ft: float

    block_length_mm: float
    block_height_mm: float
    block_thickness_mm: float

    waste_percent: float = 5.0          # extra blocks for breakage, cutting
    mortar_ratio_percent: float = 25.0  # % of wall volume as mortar (approx)
    block_cost: float = 0.0             # Rs per block


@dataclass
class BlockworkOutput:
    total_blocks: float
    mortar_volume_m3: float
    total_cost: float


def calculate_blockwork(i: BlockworkInput) -> BlockworkOutput:
    # Convert wall dimensions to meters
    L = i.wall_length_ft * FT_TO_M
    H = i.wall_height_ft * FT_TO_M
    T = i.wall_thickness_ft * FT_TO_M

    wall_volume_m3 = L * H * T

    # Block volume (assuming size includes mortar joint)
    bL = i.block_length_mm * MM_TO_M
    bH = i.block_height_mm * MM_TO_M
    bT = i.block_thickness_mm * MM_TO_M

    block_volume_m3 = bL * bH * bT
    if block_volume_m3 <= 0:
        raise ValueError("Block dimensions must be greater than zero.")

    # Raw block count without waste
    blocks_raw = wall_volume_m3 / block_volume_m3

    # Add waste
    total_blocks = blocks_raw * (1.0 + i.waste_percent / 100.0)

    # Approx mortar volume as % of wall volume
    mortar_volume_m3 = wall_volume_m3 * (i.mortar_ratio_percent / 100.0)

    # Cost
    total_cost = total_blocks * i.block_cost if i.block_cost > 0 else 0.0

    return BlockworkOutput(
        total_blocks=total_blocks,
        mortar_volume_m3=mortar_volume_m3,
        total_cost=total_cost,
    )
