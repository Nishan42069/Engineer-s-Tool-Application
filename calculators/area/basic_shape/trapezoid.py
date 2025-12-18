from dataclasses import dataclass

@dataclass
class TrapezoidInput:
    top_width_m: float
    bottom_width_m: float
    height_m: float

@dataclass
class TrapezoidOutput:
    area_m2: float

def calculate_trapezoid(i: TrapezoidInput) -> TrapezoidOutput:
    area = 0.5 * (i.top_width_m + i.bottom_width_m) * i.height_m
    return TrapezoidOutput(area_m2=area)
