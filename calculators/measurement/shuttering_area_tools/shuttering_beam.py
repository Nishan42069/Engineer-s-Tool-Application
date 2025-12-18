from dataclasses import dataclass

FT2_TO_M2 = 0.09290304


@dataclass
class BeamShutteringInput:
    length_ft: float
    width_ft: float
    depth_ft: float
    quantity: int = 1
    include_end_faces: bool = False


@dataclass
class BeamShutteringOutput:
    area_ft2: float
    area_m2: float


def calculate_beam_shuttering(i: BeamShutteringInput) -> BeamShutteringOutput:
    if i.length_ft < 0 or i.width_ft < 0 or i.depth_ft < 0:
        raise ValueError("All dimensions must be non-negative.")
    if i.quantity < 1:
        raise ValueError("Quantity must be at least 1.")

    # Bottom + 2 sides
    bottom = i.length_ft * i.width_ft
    sides = 2.0 * i.length_ft * i.depth_ft

    ends = 0.0
    if i.include_end_faces:
        ends = 2.0 * i.width_ft * i.depth_ft

    total_ft2 = (bottom + sides + ends) * i.quantity
    total_m2 = total_ft2 * FT2_TO_M2
    return BeamShutteringOutput(area_ft2=total_ft2, area_m2=total_m2)
