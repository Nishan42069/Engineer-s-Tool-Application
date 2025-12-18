from dataclasses import dataclass

@dataclass
class TriangleDumperInput:
    length_m: float
    base_m: float
    height_m: float

@dataclass
class TriangleDumperOutput:
    cross_area_m2: float
    volume_m3: float
    volume_litre: float

def calculate_triangle_dumper(i: TriangleDumperInput) -> TriangleDumperOutput:
    area = 0.5 * i.base_m * i.height_m
    v = area * i.length_m
    return TriangleDumperOutput(cross_area_m2=area, volume_m3=v, volume_litre=v * 1000.0)
