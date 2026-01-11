from dataclasses import dataclass
import math

# =========================
# RECTANGULAR HOLLOW
# =========================
@dataclass
class HollowRectangularInput:
    outer_length_m: float
    outer_width_m: float
    outer_height_m: float
    inner_length_m: float
    inner_width_m: float
    inner_height_m: float


@dataclass
class HollowRectangularOutput:
    outer_area_m2: float
    inner_area_m2: float
    hollow_area_m2: float
    outer_volume_m3: float
    inner_volume_m3: float
    hollow_volume_m3: float


def calculate_hollow_rectangular(i: HollowRectangularInput) -> HollowRectangularOutput:
    outer_area = i.outer_length_m * i.outer_width_m
    inner_area = i.inner_length_m * i.inner_width_m
    hollow_area = max(outer_area - inner_area, 0.0)

    outer_volume = outer_area * i.outer_height_m
    inner_volume = inner_area * i.inner_height_m
    hollow_volume = max(outer_volume - inner_volume, 0.0)

    return HollowRectangularOutput(
        outer_area_m2=outer_area,
        inner_area_m2=inner_area,
        hollow_area_m2=hollow_area,
        outer_volume_m3=outer_volume,
        inner_volume_m3=inner_volume,
        hollow_volume_m3=hollow_volume,
    )


# =========================
# CYLINDRICAL HOLLOW
# =========================
@dataclass
class HollowCylindricalInput:
    outer_diameter_m: float
    inner_diameter_m: float
    height_m: float


@dataclass
class HollowCylindricalOutput:
    outer_area_m2: float
    inner_area_m2: float
    hollow_area_m2: float
    outer_volume_m3: float
    inner_volume_m3: float
    hollow_volume_m3: float


def calculate_hollow_cylindrical(i: HollowCylindricalInput) -> HollowCylindricalOutput:
    r_o = i.outer_diameter_m / 2
    r_i = i.inner_diameter_m / 2

    outer_area = math.pi * r_o**2
    inner_area = math.pi * r_i**2
    hollow_area = max(outer_area - inner_area, 0.0)

    outer_volume = outer_area * i.height_m
    inner_volume = inner_area * i.height_m
    hollow_volume = max(outer_volume - inner_volume, 0.0)

    return HollowCylindricalOutput(
        outer_area_m2=outer_area,
        inner_area_m2=inner_area,
        hollow_area_m2=hollow_area,
        outer_volume_m3=outer_volume,
        inner_volume_m3=inner_volume,
        hollow_volume_m3=hollow_volume,
    )
