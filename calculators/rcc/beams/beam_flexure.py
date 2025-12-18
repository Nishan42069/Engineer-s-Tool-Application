# calculators/rcc/beam_flexure.py

from dataclasses import dataclass
import math


@dataclass
class BeamDesignInput:
    mu_kNm: float          # factored bending moment
    b_mm: float
    d_mm: float            # effective depth
    fck_MPa: float
    fy_MPa: float
    n_bars: int
    bar_dia_mm: float


@dataclass
class BeamDesignOutput:
    mu_kNm: float
    ast_required_mm2: float
    ast_min_mm2: float
    ast_provided_mm2: float
    mu_capacity_kNm: float
    utilization: float      # Mu / Mu_cap


def design_beam_flexure(i: BeamDesignInput) -> BeamDesignOutput:
    d = i.d_mm
    if d <= 0:
        raise ValueError("Effective depth d must be > 0")

    j = 0.9 * d
    Mu_Nmm = i.mu_kNm * 1e6

    ast_req = Mu_Nmm / (0.87 * i.fy_MPa * j)

    # minimum tension steel (IS456)

    ast_min = 0.002 * i.b_mm * d  # 0.2% of b*d (slightly conservative for beams)

    ast_req_final = max(ast_req, ast_min)

    area_bar = math.pi * (i.bar_dia_mm ** 2) / 4.0
    ast_prov = area_bar * i.n_bars

    # capacity with provided steel:
    Mu_cap_Nmm = 0.87 * i.fy_MPa * ast_prov * j
    Mu_cap_kNm = Mu_cap_Nmm / 1e6

    util = i.mu_kNm / Mu_cap_kNm if Mu_cap_kNm > 0 else 0.0

    return BeamDesignOutput(
        mu_kNm=i.mu_kNm,
        ast_required_mm2=ast_req_final,
        ast_min_mm2=ast_min,
        ast_provided_mm2=ast_prov,
        mu_capacity_kNm=Mu_cap_kNm,
        utilization=util,
    )
