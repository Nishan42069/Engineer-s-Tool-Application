from dataclasses import dataclass

@dataclass
class ShadeRoofInput:
    length_ft: float
    width_ft: float
    slope_angle_deg: float  # Slope of the roof in degrees

def calculate_shade_roof(i: ShadeRoofInput) -> float:
    import math

    # Calculate the roof area with slope
    slope_length = i.length_ft / math.cos(math.radians(i.slope_angle_deg))
    roof_area = slope_length * i.width_ft
    return roof_area
