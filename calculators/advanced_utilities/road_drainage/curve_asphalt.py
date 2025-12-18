from dataclasses import dataclass

@dataclass
class CurveAsphaltInput:
    curve_length_ft: float
    curve_radius_ft: float
    thickness_ft: float

def calculate_curve_asphalt(i: CurveAsphaltInput) -> float:
    # Formula: Asphalt volume = curve length * width * thickness
    area = i.curve_length_ft * i.curve_radius_ft  # This will be the curved area for the road
    volume = area * i.thickness_ft
    return volume
