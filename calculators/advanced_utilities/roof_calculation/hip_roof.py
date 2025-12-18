from dataclasses import dataclass

@dataclass
class HipRoofInput:
    length_ft: float
    width_ft: float
    slope_angle_deg: float  # Slope of the roof in degrees

def calculate_hip_roof(i: HipRoofInput) -> float:
    import math

    # Calculate the roof area with slope for hip roof
    slope_length = i.length_ft / math.cos(math.radians(i.slope_angle_deg))
    roof_area = slope_length * i.width_ft
    return roof_area
