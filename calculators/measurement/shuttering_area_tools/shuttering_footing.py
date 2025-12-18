import math
from dataclasses import dataclass

FT2_TO_M2 = 0.09290304


@dataclass
class FootingShutteringInput:
    footing_type: str  # "Rectangular" or "Circular"
    thickness_ft: float
    quantity: int = 1

    # rectangular
    length_ft: float = 0.0
    width_ft: float = 0.0

    # circular
    diameter_ft: float = 0.0


@dataclass
class FootingShutteringOutput:
    area_ft2: float
    area_m2: float


def calculate_footing_shuttering(i: FootingShutteringInput) -> FootingShutteringOutput:
    if i.thickness_ft < 0:
        raise ValueError("Thickness must be non-negative.")
    if i.quantity < 1:
        raise ValueError("Quantity must be at least 1.")

    t = i.footing_type.strip().lower()

    if t == "rectangular":
        if i.length_ft < 0 or i.width_ft < 0:
            raise ValueError("Length/width must be non-negative.")
        perimeter_ft = 2.0 * (i.length_ft + i.width_ft)
        area_ft2 = perimeter_ft * i.thickness_ft

    elif t == "circular":
        if i.diameter_ft < 0:
            raise ValueError("Diameter must be non-negative.")
        circumference_ft = math.pi * i.diameter_ft
        area_ft2 = circumference_ft * i.thickness_ft

    else:
        raise ValueError("footing_type must be 'Rectangular' or 'Circular'.")

    total_ft2 = area_ft2 * i.quantity
    total_m2 = total_ft2 * FT2_TO_M2
    return FootingShutteringOutput(area_ft2=total_ft2, area_m2=total_m2)
