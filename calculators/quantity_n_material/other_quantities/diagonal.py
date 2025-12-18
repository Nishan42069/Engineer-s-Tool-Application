from dataclasses import dataclass
import math


@dataclass
class DiagonalInput:
    length: float
    width: float


@dataclass
class DiagonalOutput:
    diagonal: float


def calculate_diagonal(i: DiagonalInput) -> DiagonalOutput:
    d = math.sqrt(i.length ** 2 + i.width ** 2)
    return DiagonalOutput(diagonal=d)
