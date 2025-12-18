from dataclasses import dataclass

@dataclass
class PumpHorsepowerInput:
    flow_rate_gpm: float  # Flow rate in GPM
    head_ft: float
    efficiency: float

def calculate_pump_horsepower(i: PumpHorsepowerInput) -> float:
    # Formula: HP = (Flow * Head) / (3960 * Efficiency)
    horsepower = (i.flow_rate_gpm * i.head_ft) / (3960 * i.efficiency / 100)
    return horsepower
