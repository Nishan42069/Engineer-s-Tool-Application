from dataclasses import dataclass

@dataclass
class TrapezoidDumperInput:
    length_m: float
    top_width_m: float
    bottom_width_m: float
    height_m: float

@dataclass
class TrapezoidDumperOutput:
    cross_area_m2: float
    volume_m3: float
    volume_litre: float

def calculate_trapezoid_dumper(i: TrapezoidDumperInput) -> TrapezoidDumperOutput:
    area = 0.5 * (i.top_width_m + i.bottom_width_m) * i.height_m
    v = area * i.length_m
    return TrapezoidDumperOutput(cross_area_m2=area, volume_m3=v, volume_litre=v * 1000.0)
