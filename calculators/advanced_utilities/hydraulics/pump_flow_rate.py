from dataclasses import dataclass

@dataclass
class PumpFlowRateInput:
    power_hp: float
    head_ft: float
    efficiency: float  # Pump efficiency as percentage

def calculate_pump_flow_rate(i: PumpFlowRateInput) -> float:
    # Flow rate (Q) = Power / (Head * Efficiency)
    flow_rate = i.power_hp * 746 / (i.head_ft * i.efficiency / 100)
    return flow_rate
