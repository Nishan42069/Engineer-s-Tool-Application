from dataclasses import dataclass

@dataclass
class TotalHeadInput:
    flow_rate_gpm: float
    horsepower_hp: float
    efficiency: float

def calculate_total_head(i: TotalHeadInput) -> float:
    # Formula: Total Head (ft) = (Flow * Head) / (3960 * Efficiency)
    total_head = (i.horsepower_hp * 3960 * i.efficiency / 100) / i.flow_rate_gpm
    return total_head
