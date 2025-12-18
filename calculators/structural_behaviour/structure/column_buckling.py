from dataclasses import dataclass

@dataclass
class ColumnBucklingInput:
    length_ft: float
    diameter_ft: float  # Diameter of column

def calculate_column_buckling(i: ColumnBucklingInput) -> float:
    # Use formula for critical load (P_cr) for buckling
    E = 210000  # Young's Modulus for Steel in MPa
    I = (3.1415 * (i.diameter_ft ** 4)) / 64
    P_cr = (3.1415 ** 2 * E * I) / (i.length_ft ** 2)  # Critical load
    return P_cr
