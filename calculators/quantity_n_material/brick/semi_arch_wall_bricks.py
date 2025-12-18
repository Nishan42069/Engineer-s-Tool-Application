from dataclasses import dataclass
from .arch_wall_bricks import (
    ArchWallBricksInput,
    ArchWallBricksOutput,
    calculate_arch_wall_bricks,
)


@dataclass
class SemiArchWallBricksInput(ArchWallBricksInput):
    pass


def calculate_semi_arch_wall_bricks(
    i: SemiArchWallBricksInput,
) -> ArchWallBricksOutput:
    # Currently same approximation as full arch.
    return calculate_arch_wall_bricks(i)
