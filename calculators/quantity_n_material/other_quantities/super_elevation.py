from dataclasses import dataclass


@dataclass
class SuperElevationInput:
    speed_kmph: float         # V
    radius_m: float           # R
    side_friction: float      # f
    max_super_elevation: float = 0.07  # typical 7%


@dataclass
class SuperElevationOutput:
    required_e: float         # required super-elevation (decimal)
    limited_e: float          # actual provided, clipped at max
    is_within_limit: bool


def calculate_super_elevation(i: SuperElevationInput) -> SuperElevationOutput:
    if i.radius_m <= 0:
        raise ValueError("Radius must be greater than zero.")

    rhs = (i.speed_kmph ** 2) / (127.0 * i.radius_m)
    e_req = rhs - i.side_friction
    e_req = max(e_req, 0.0)

    e_limited = min(e_req, i.max_super_elevation)
    within = e_req <= i.max_super_elevation

    return SuperElevationOutput(
        required_e=e_req,
        limited_e=e_limited,
        is_within_limit=within,
    )
