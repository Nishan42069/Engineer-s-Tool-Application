from dataclasses import dataclass
import math

@dataclass
class Shape2Input:
    rect_length_m: float
    rect_width_m: float
    radius_m: float

@dataclass
class Shape2Output:
    rect_area_m2: float
    semicircle_area_m2: float
    total_area_m2: float

def calculate_shape2(i: Shape2Input) -> Shape2Output:
    rect_area = i.rect_length_m * i.rect_width_m
    semicircle_area = 0.5 * math.pi * (i.radius_m ** 2)
    return Shape2Output(rect_area_m2=rect_area, semicircle_area_m2=semicircle_area, total_area_m2=rect_area + semicircle_area)
