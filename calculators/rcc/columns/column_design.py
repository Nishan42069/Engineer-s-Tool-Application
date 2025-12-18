# calculators/rcc/column_design.py

from dataclasses import dataclass
import math


@dataclass
class RectColumnInput:
    b_mm: float
    D_mm: float
    n_bars: int
    bar_dia_mm: float
    fck_MPa: float = 25.0
    fy_MPa: float = 415.0


@dataclass
class RectColumnOutput:
    gross_area_mm2: float
    steel_area_mm2: float
    concrete_area_mm2: float
    steel_ratio_percent: float
    axial_capacity_kN: float


def design_rect_column(i: RectColumnInput) -> RectColumnOutput:
    Ag = i.b_mm * i.D_mm
    area_bar = math.pi * (i.bar_dia_mm ** 2) / 4.0
    Asc = i.n_bars * area_bar
    Ac = Ag - Asc

    # Pu in N: fck / fy in N/mm² × area mm²
    Pu_conc = 0.4 * i.fck_MPa * Ac
    Pu_steel = 0.67 * i.fy_MPa * Asc
    Pu_kN = (Pu_conc + Pu_steel) / 1000.0

    rho = Asc / Ag * 100.0

    return RectColumnOutput(
        gross_area_mm2=Ag,
        steel_area_mm2=Asc,
        concrete_area_mm2=Ac,
        steel_ratio_percent=rho,
        axial_capacity_kN=Pu_kN,
    )


@dataclass
class RoundColumnInput:
    dia_mm: float
    n_bars: int
    bar_dia_mm: float
    fck_MPa: float = 25.0
    fy_MPa: float = 415.0


@dataclass
class RoundColumnOutput:
    gross_area_mm2: float
    steel_area_mm2: float
    concrete_area_mm2: float
    steel_ratio_percent: float
    axial_capacity_kN: float


def design_round_column(i: RoundColumnInput) -> RoundColumnOutput:
    Ag = math.pi * (i.dia_mm ** 2) / 4.0
    area_bar = math.pi * (i.bar_dia_mm ** 2) / 4.0
    Asc = i.n_bars * area_bar
    Ac = Ag - Asc

    Pu_conc = 0.4 * i.fck_MPa * Ac
    Pu_steel = 0.67 * i.fy_MPa * Asc
    Pu_kN = (Pu_conc + Pu_steel) / 1000.0

    rho = Asc / Ag * 100.0

    return RoundColumnOutput(
        gross_area_mm2=Ag,
        steel_area_mm2=Asc,
        concrete_area_mm2=Ac,
        steel_ratio_percent=rho,
        axial_capacity_kN=Pu_kN,
    )
