from dataclasses import dataclass


@dataclass
class FormworkSlabInput:
    slab_length_m: float
    slab_width_m: float
    slab_thickness_m: float
    include_edges: bool = True


@dataclass
class FormworkSlabOutput:
    soffit_area_m2: float
    edge_area_m2: float
    total_formwork_area_m2: float


def calculate_formwork_slab(i: FormworkSlabInput) -> FormworkSlabOutput:
    soffit = i.slab_length_m * i.slab_width_m
    edge = 0.0
    if i.include_edges:
        perimeter = 2.0 * (i.slab_length_m + i.slab_width_m)
        edge = perimeter * i.slab_thickness_m
    total = soffit + edge
    return FormworkSlabOutput(
        soffit_area_m2=soffit,
        edge_area_m2=edge,
        total_formwork_area_m2=total,
    )
