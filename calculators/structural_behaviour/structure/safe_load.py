from dataclasses import dataclass
import math

FT_TO_M = 0.3048

@dataclass
class ColumnBucklingInput:
    length_ft: float
    diameter_ft: float
    E_gpa: float = 200.0          # Steel default. Use 25–30 for RCC if you want.
    k_factor: float = 1.0         # 1.0 pinned-pinned, 0.5 fixed-fixed, 2.0 cantilever, 0.7 fixed-pinned

@dataclass
class ColumnBucklingOutput:
    Pcr_kN: float

def calculate_column_buckling(i: ColumnBucklingInput) -> ColumnBucklingOutput:
    L = i.length_ft * FT_TO_M
    d = i.diameter_ft * FT_TO_M

    if L <= 0 or d <= 0:
        raise ValueError("Length and diameter must be > 0.")

    E = i.E_gpa * 1e9  # Pa
    I = (math.pi * d**4) / 64.0
    Le = i.k_factor * L

    Pcr_N = (math.pi**2 * E * I) / (Le**2)
    return ColumnBucklingOutput(Pcr_kN=Pcr_N / 1000.0)
