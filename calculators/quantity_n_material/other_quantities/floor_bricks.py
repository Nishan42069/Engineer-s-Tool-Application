from dataclasses import dataclass
import math


@dataclass
class FloorBrickInput:
    floor_length_m: float
    floor_width_m: float
    brick_length_m: float
    brick_width_m: float
    wastage_percent: float = 10.0


@dataclass
class FloorBrickOutput:
    floor_area_m2: float
    brick_area_m2: float
    bricks_net: float
    bricks_with_wastage: int


def calculate_floor_bricks(i: FloorBrickInput) -> FloorBrickOutput:
    floor_area = i.floor_length_m * i.floor_width_m
    brick_area = i.brick_length_m * i.brick_width_m
    if brick_area <= 0:
        raise ValueError("Brick size must be greater than zero.")

    bricks_net = floor_area / brick_area
    factor = 1.0 + i.wastage_percent / 100.0
    bricks_needed = math.ceil(bricks_net * factor)

    return FloorBrickOutput(
        floor_area_m2=floor_area,
        brick_area_m2=brick_area,
        bricks_net=bricks_net,
        bricks_with_wastage=bricks_needed,
    )
