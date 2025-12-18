from dataclasses import dataclass


@dataclass
class TerrazzoInput:
    area_m2: float
    cement_consumption_kg_m2: float
    chips_consumption_kg_m2: float


@dataclass
class TerrazzoOutput:
    cement_kg: float
    chips_kg: float


def calculate_terrazzo(i: TerrazzoInput) -> TerrazzoOutput:
    cement = i.area_m2 * i.cement_consumption_kg_m2
    chips = i.area_m2 * i.chips_consumption_kg_m2
    return TerrazzoOutput(cement_kg=cement, chips_kg=chips)
