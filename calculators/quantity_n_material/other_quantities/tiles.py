from dataclasses import dataclass
import math


@dataclass
class TileInput:
    room_length_m: float
    room_width_m: float
    tile_length_m: float
    tile_width_m: float
    wastage_percent: float = 10.0


@dataclass
class TileOutput:
    room_area_m2: float
    tile_area_m2: float
    tiles_net: float
    tiles_with_wastage: int


def calculate_tiles(i: TileInput) -> TileOutput:
    room_area = i.room_length_m * i.room_width_m
    tile_area = i.tile_length_m * i.tile_width_m
    if tile_area <= 0:
        raise ValueError("Tile size must be greater than zero.")

    tiles_net = room_area / tile_area
    factor = 1.0 + i.wastage_percent / 100.0
    tiles_needed = math.ceil(tiles_net * factor)

    return TileOutput(
        room_area_m2=room_area,
        tile_area_m2=tile_area,
        tiles_net=tiles_net,
        tiles_with_wastage=tiles_needed,
    )
