from dataclasses import dataclass


@dataclass
class ConcreteCubeTestInput:
    load_at_failure_kN: float
    cube_size_mm: float
    characteristic_strength_MPa: float


@dataclass
class ConcreteCubeTestOutput:
    cube_strength_MPa: float
    passes: bool


def calculate_concrete_cube_test(i: ConcreteCubeTestInput) -> ConcreteCubeTestOutput:
    side_m = i.cube_size_mm / 1000.0
    area_m2 = side_m * side_m
    if area_m2 <= 0:
        raise ValueError("Cube size must be > 0.")

    stress_kPa = i.load_at_failure_kN / area_m2   # kPa
    stress_MPa = stress_kPa / 1000.0

    passes = stress_MPa >= i.characteristic_strength_MPa
    return ConcreteCubeTestOutput(
        cube_strength_MPa=stress_MPa,
        passes=passes,
    )
