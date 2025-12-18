import math
from dataclasses import dataclass

FT2_TO_M2 = 0.09290304


@dataclass
class ColumnShutteringInput:
    column_type: str  # "Square" or "Round"
    height_ft: float
    quantity: int = 1

    # square/rect
    width_ft: float = 0.0
    depth_ft: float = 0.0

    # round
    diameter_ft: float = 0.0


@dataclass
class ColumnShutteringOutput:
    area_ft2: float
    area_m2: float


def calculate_column_shuttering(i: ColumnShutteringInput) -> ColumnShutteringOutput:
    if i.height_ft < 0:
        raise ValueError("Height must be non-negative.")
    if i.quantity < 1:
        raise ValueError("Quantity must be at least 1.")

    t = i.column_type.strip().lower()

    if t == "square":
        if i.width_ft < 0 or i.depth_ft < 0:
            raise ValueError("Width/depth must be non-negative.")
        perimeter_ft = 2.0 * (i.width_ft + i.depth_ft)
        area_ft2 = perimeter_ft * i.height_ft

    elif t == "round":
        if i.diameter_ft < 0:
            raise ValueError("Diameter must be non-negative.")
        circumference_ft = math.pi * i.diameter_ft
        area_ft2 = circumference_ft * i.height_ft

    else:
        raise ValueError("column_type must be 'Square' or 'Round'.")

    total_ft2 = area_ft2 * i.quantity
    total_m2 = total_ft2 * FT2_TO_M2
    return ColumnShutteringOutput(area_ft2=total_ft2, area_m2=total_m2)
