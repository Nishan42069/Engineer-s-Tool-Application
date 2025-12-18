from dataclasses import dataclass

@dataclass
class StairGeometryInput:
    tread_inch: float
    riser_inch: float
    steps_count: int

def calculate_stair_geometry(i: StairGeometryInput) -> float:
    # Stair geometry calculation: Total stair area = number of steps * (tread * riser)
    total_area = i.steps_count * (i.tread_inch * i.riser_inch)
    return total_area
