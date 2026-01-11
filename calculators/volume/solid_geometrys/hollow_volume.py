from dataclasses import dataclass
import math


# -------------------------
# RECTANGULAR HOLLOW SPACE
# -------------------------
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
    outer_volume_m3: float
    inner_volume_m3: float
    hollow_volume_m3: float


def calculate_hollow_rectangular_volume(
    i: HollowRectangularInput,
) -> HollowRectangularOutput:
    outer_vol = (
        i.outer_length_m
        * i.outer_width_m
        * i.outer_height_m
    )

    inner_vol = (
        i.inner_length_m
        * i.inner_width_m
        * i.inner_height_m
    )

    hollow_vol = max(outer_vol - inner_vol, 0.0)

    return HollowRectangularOutput(
        outer_volume_m3=outer_vol,
        inner_volume_m3=inner_vol,
        hollow_volume_m3=hollow_vol,
    )


# -------------------------
# CYLINDRICAL HOLLOW SPACE
# -------------------------
@dataclass
class HollowCylindricalInput:
    outer_diameter_m: float
    inner_diameter_m: float
    height_m: float


@dataclass
class HollowCylindricalOutput:
    outer_volume_m3: float
    inner_volume_m3: float
    hollow_volume_m3: float


def calculate_hollow_cylindrical_volume(
    i: HollowCylindricalInput,
) -> HollowCylindricalOutput:
    r_outer = i.outer_diameter_m / 2
    r_inner = i.inner_diameter_m / 2

    outer_vol = math.pi * r_outer**2 * i.height_m
    inner_vol = math.pi * r_inner**2 * i.height_m

    hollow_vol = max(outer_vol - inner_vol, 0.0)

    return HollowCylindricalOutput(
        outer_volume_m3=outer_vol,
        inner_volume_m3=inner_vol,
        hollow_volume_m3=hollow_vol,
    )
