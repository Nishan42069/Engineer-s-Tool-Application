from dataclasses import dataclass
import math

@dataclass
class Shape3Input:
    rect_length_m: float
    rect_width_m: float
    radius_m: float

@dataclass
class Shape3Output:
    rect_area_m2: float
    circle_area_m2: float
    total_area_m2: float

def calculate_shape3(i: Shape3Input) -> Shape3Output:
    rect_area = i.rect_length_m * i.rect_width_m
    circle_area = math.pi * (i.radius_m ** 2)  # two semicircles = one full circle
    return Shape3Output(rect_area_m2=rect_area, circle_area_m2=circle_area, total_area_m2=rect_area + circle_area)
