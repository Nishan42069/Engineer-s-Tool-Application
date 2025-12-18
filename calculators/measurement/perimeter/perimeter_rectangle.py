from dataclasses import dataclass

FT_TO_M = 0.3048


@dataclass
class RectanglePerimeterInput:
    length_ft: float
    width_ft: float


@dataclass
class RectanglePerimeterOutput:
    perimeter_ft: float
    perimeter_m: float


def calculate_rectangle_perimeter(i: RectanglePerimeterInput) -> RectanglePerimeterOutput:
    if i.length_ft < 0 or i.width_ft < 0:
        raise ValueError("Length and width must be non-negative.")

    p_ft = 2.0 * (i.length_ft + i.width_ft)
    p_m = p_ft * FT_TO_M

    return RectanglePerimeterOutput(perimeter_ft=p_ft, perimeter_m=p_m)
