from dataclasses import dataclass

GRAVITY = 9.81          # m/s²
WATER_DENSITY = 1000.0 # kg/m³


@dataclass
class PumpFlowRateInput:
    power_w: float          # pump input power in W
    head_m: float           # pump head in meters
    efficiency: float       # efficiency in %


def calculate_pump_flow_rate(i: PumpFlowRateInput) -> float:
    """
    Returns flow rate in m³/s

    Formula:
    P = ρ g Q H / η
    Q = (P * η) / (ρ g H)
    """

    if i.head_m <= 0 or i.efficiency <= 0:
        raise ValueError("Head and efficiency must be greater than zero.")

    efficiency_frac = i.efficiency / 100.0

    flow_m3_s = (
        i.power_w * efficiency_frac
        / (WATER_DENSITY * GRAVITY * i.head_m)
    )

    return flow_m3_s
