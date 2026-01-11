from dataclasses import dataclass

GRAVITY = 9.81          # m/s²
WATER_DENSITY = 1000.0 # kg/m³


@dataclass
class PumpPowerInput:
    flow_m3_s: float     # flow rate in m³/s
    head_m: float        # pump head in meters
    efficiency: float   # efficiency in %


@dataclass
class PumpPowerOutput:
    power_w: float
    power_kw: float
    power_hp: float


def calculate_pump_power(i: PumpPowerInput) -> PumpPowerOutput:
    """
    Hydraulic power:
    P = ρ g Q H / η
    """

    if i.flow_m3_s <= 0 or i.head_m <= 0 or i.efficiency <= 0:
        raise ValueError("Flow, head, and efficiency must be greater than zero.")

    eff = i.efficiency / 100.0

    power_w = (
        WATER_DENSITY
        * GRAVITY
        * i.flow_m3_s
        * i.head_m
        / eff
    )

    power_kw = power_w / 1000.0
    power_hp = power_w / 746.0

    return PumpPowerOutput(
        power_w=power_w,
        power_kw=power_kw,
        power_hp=power_hp,
    )
