from dataclasses import dataclass


@dataclass
class PorosityInput:
    void_ratio: float   # e


@dataclass
class PorosityOutput:
    porosity_decimal: float
    porosity_percent: float


def calculate_porosity(i: PorosityInput) -> PorosityOutput:
    if (1.0 + i.void_ratio) <= 0:
        raise ValueError("Void ratio + 1 must be > 0.")
    n = i.void_ratio / (1.0 + i.void_ratio)
    return PorosityOutput(
        porosity_decimal=n,
        porosity_percent=n * 100.0,
    )
