from dataclasses import dataclass

@dataclass
class RectangleTankInput:
    length_m: float
    width_m: float
    water_height_m: float

@dataclass
class RectangleTankOutput:
    volume_m3: float
    capacity_litre: float

def calculate_rectangle_tank(i: RectangleTankInput) -> RectangleTankOutput:
    v = i.length_m * i.width_m * i.water_height_m
    return RectangleTankOutput(volume_m3=v, capacity_litre=v * 1000.0)
