from dataclasses import dataclass
import math


@dataclass
class ModulusElasticityConcreteInput:
    fck_MPa: float
    coefficient: float = 5000.0  # IS: Ec = 5000√fck


@dataclass
class ModulusElasticityConcreteOutput:
    Ec_MPa: float


def calculate_modulus_elasticity_concrete(i: ModulusElasticityConcreteInput) -> ModulusElasticityConcreteOutput:
    if i.fck_MPa < 0:
        raise ValueError("fck cannot be negative.")
    Ec = i.coefficient * math.sqrt(i.fck_MPa)
    return ModulusElasticityConcreteOutput(Ec_MPa=Ec)
