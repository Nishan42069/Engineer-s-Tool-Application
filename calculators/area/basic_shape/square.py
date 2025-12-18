from dataclasses import dataclass

@dataclass
class SquareInput:
    side_m: float

@dataclass
class SquareOutput:
    area_m2: float

def calculate_square(i: SquareInput) -> SquareOutput:
    return SquareOutput(area_m2=i.side_m * i.side_m)
