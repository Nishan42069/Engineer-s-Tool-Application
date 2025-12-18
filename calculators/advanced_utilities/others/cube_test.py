from dataclasses import dataclass

@dataclass
class CubeTestInput:
    load_kn: float  # Load in kilonewtons
    area_cm2: float  # Area in cm²

def calculate_cube_test(i: CubeTestInput) -> float:
    # Cube test strength = load / area
    strength_mpa = i.load_kn / i.area_cm2  # Results in MPa
    return strength_mpa
