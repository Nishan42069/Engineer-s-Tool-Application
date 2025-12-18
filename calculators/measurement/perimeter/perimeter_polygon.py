from dataclasses import dataclass
from typing import List

FT_TO_M = 0.3048


@dataclass
class PolygonPerimeterInput:
    side_lengths_ft: List[float]


@dataclass
class PolygonPerimeterOutput:
    perimeter_ft: float
    perimeter_m: float
    sides_count: int


def calculate_polygon_perimeter(i: PolygonPerimeterInput) -> PolygonPerimeterOutput:
    if not i.side_lengths_ft:
        raise ValueError("Provide at least one side length.")
    if any(s < 0 for s in i.side_lengths_ft):
        raise ValueError("Side lengths must be non-negative.")

    p_ft = float(sum(i.side_lengths_ft))
    p_m = p_ft * FT_TO_M
    return PolygonPerimeterOutput(perimeter_ft=p_ft, perimeter_m=p_m, sides_count=len(i.side_lengths_ft))
