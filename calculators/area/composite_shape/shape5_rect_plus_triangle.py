from dataclasses import dataclass

@dataclass
class Shape5Input:
    rect_length_m: float
    rect_width_m: float
    tri_base_m: float
    tri_height_m: float

@dataclass
class Shape5Output:
    rect_area_m2: float
    tri_area_m2: float
    total_area_m2: float

def calculate_shape5(i: Shape5Input) -> Shape5Output:
    rect_area = i.rect_length_m * i.rect_width_m
    tri_area = 0.5 * i.tri_base_m * i.tri_height_m
    return Shape5Output(rect_area_m2=rect_area, tri_area_m2=tri_area, total_area_m2=rect_area + tri_area)
