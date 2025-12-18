import math
from dataclasses import dataclass

FT_TO_M = 0.3048


@dataclass
class CirclePerimeterInput:
    radius_ft: float = 0.0
    diameter_ft: float = 0.0
    use_diameter: bool = True


@dataclass
class CirclePerimeterOutput:
    circumference_ft: float
    circumference_m: float


def calculate_circle_perimeter(i: CirclePerimeterInput) -> CirclePerimeterOutput:
    if i.use_diameter:
        if i.diameter_ft < 0:
            raise ValueError("Diameter must be non-negative.")
        d = i.diameter_ft
    else:
        if i.radius_ft < 0:
            raise ValueError("Radius must be non-negative.")
        d = 2.0 * i.radius_ft

    c_ft = math.pi * d
    c_m = c_ft * FT_TO_M
    return CirclePerimeterOutput(circumference_ft=c_ft, circumference_m=c_m)
