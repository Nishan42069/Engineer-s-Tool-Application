from dataclasses import dataclass

@dataclass
class Shape4Input:
    width_end1_m: float
    width_end2_m: float
    length_m: float

@dataclass
class Shape4Output:
    area_m2: float

def calculate_shape4(i: Shape4Input) -> Shape4Output:
    area = 0.5 * (i.width_end1_m + i.width_end2_m) * i.length_m
    return Shape4Output(area_m2=area)
