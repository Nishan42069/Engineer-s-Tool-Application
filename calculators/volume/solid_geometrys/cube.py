from dataclasses import dataclass

@dataclass
class CubeInput:
    side_m: float

@dataclass
class CubeOutput:
    volume_m3: float
    volume_litre: float

def calculate_cube(i: CubeInput) -> CubeOutput:
    v = i.side_m ** 3
    return CubeOutput(volume_m3=v, volume_litre=v * 1000.0)
