from dataclasses import dataclass
from calculators.structural_behaviour.structure.column_buckling import ColumnBucklingInput, calculate_column_buckling

@dataclass
class SafeLoadInput:
    length_ft: float
    diameter_ft: float
    E_gpa: float = 200.0
    k_factor: float = 1.0
    safety_factor: float = 1.5

@dataclass
class SafeLoadOutput:
    Pcr_kN: float
    Psafe_kN: float
    safety_factor: float

def calculate_safe_load(i: SafeLoadInput) -> SafeLoadOutput:
    if i.safety_factor <= 0:
        raise ValueError("Safety factor must be > 0.")

    buckling_out = calculate_column_buckling(
        ColumnBucklingInput(
            length_ft=i.length_ft,
            diameter_ft=i.diameter_ft,
            E_gpa=i.E_gpa,
            k_factor=i.k_factor,
        )
    )

    psafe = buckling_out.Pcr_kN / i.safety_factor
    return SafeLoadOutput(
        Pcr_kN=buckling_out.Pcr_kN,
        Psafe_kN=psafe,
        safety_factor=i.safety_factor,
    )
