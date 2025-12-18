from dataclasses import dataclass


@dataclass
class SlopeFillingInput:
    embankment_height_m: float
    top_width_m: float
    side_slope_H_over_V: float   # z
    length_m: float


@dataclass
class SlopeFillingOutput:
    cross_section_area_m2: float
    volume_m3: float


def calculate_slope_filling(i: SlopeFillingInput) -> SlopeFillingOutput:
    h = i.embankment_height_m
    b = i.top_width_m
    z = i.side_slope_H_over_V

    A = h * (b + z * h)
    V = A * i.length_m

    return SlopeFillingOutput(
        cross_section_area_m2=A,
        volume_m3=V,
    )
