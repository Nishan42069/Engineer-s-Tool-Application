from dataclasses import dataclass


@dataclass
class AntiTermiteInput:
    area_m2: float
    application_rate_L_m2: float


@dataclass
class AntiTermiteOutput:
    chemical_litres: float


def calculate_anti_termite(i: AntiTermiteInput) -> AntiTermiteOutput:
    litres = i.area_m2 * i.application_rate_L_m2
    return AntiTermiteOutput(chemical_litres=litres)
