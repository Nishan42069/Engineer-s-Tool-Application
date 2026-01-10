from dataclasses import dataclass
from calculators.quantity_n_material.brick.arch_wall_bricks import (
    ArchWallBricksInput,
    ArchWallBricksOutput,
    calculate_arch_wall_bricks,
)


@dataclass
class SemiArchWallBricksInput(ArchWallBricksInput):
    """
    Semi-arch wall uses the same geometric approximation
    as full arch for now.
    """
    pass


def calculate_semi_arch_wall_bricks(
    i: SemiArchWallBricksInput,
) -> ArchWallBricksOutput:
    return calculate_arch_wall_bricks(i)
