from dataclasses import dataclass


@dataclass
class WaterTankRectInput:
    inner_length_m: float
    inner_width_m: float
    water_height_m: float


@dataclass
class WaterTankRectOutput:
    volume_m3: float
    capacity_litres: float


def calculate_water_tank_rect(i: WaterTankRectInput) -> WaterTankRectOutput:
    V = i.inner_length_m * i.inner_width_m * i.water_height_m
    litres = V * 1000.0
    return WaterTankRectOutput(volume_m3=V, capacity_litres=litres)
