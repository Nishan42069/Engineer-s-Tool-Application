from dataclasses import dataclass

FT2_TO_M2 = 0.09290304


@dataclass
class SlabShutteringInput:
    length_ft: float
    width_ft: float
    quantity: int = 1
    include_edges: bool = False
    thickness_ft: float = 0.0  # only used if include_edges=True


@dataclass
class SlabShutteringOutput:
    area_ft2: float
    area_m2: float


def calculate_slab_shuttering(i: SlabShutteringInput) -> SlabShutteringOutput:
    if i.length_ft < 0 or i.width_ft < 0 or i.thickness_ft < 0:
        raise ValueError("All dimensions must be non-negative.")
    if i.quantity < 1:
        raise ValueError("Quantity must be at least 1.")

    bottom_ft2 = i.length_ft * i.width_ft

    edges_ft2 = 0.0
    if i.include_edges and i.thickness_ft > 0:
        perimeter_ft = 2.0 * (i.length_ft + i.width_ft)
        edges_ft2 = perimeter_ft * i.thickness_ft

    total_ft2 = (bottom_ft2 + edges_ft2) * i.quantity
    total_m2 = total_ft2 * FT2_TO_M2
    return SlabShutteringOutput(area_ft2=total_ft2, area_m2=total_m2)
