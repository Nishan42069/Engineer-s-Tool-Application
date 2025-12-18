# calculators/rcc/slab_design.py

from dataclasses import dataclass
import math


@dataclass
class SlabDesignInput:
    mu_kNm_per_m: float         # design bending moment (kNm/m strip)
    thickness_mm: float         # overall slab thickness
    effective_cover_mm: float   # cover + 0.5 * bar dia
    fck_MPa: float = 25.0
    fy_MPa: float = 415.0
    bar_dia_mm: float = 10.0    # main bar dia


@dataclass
class SlabDesignOutput:
    effective_depth_mm: float
    mu_kNm_per_m: float
    ast_required_mm2_per_m: float
    ast_min_mm2_per_m: float
    ast_provided_mm2_per_m: float
    spacing_mm: float


def design_slab_flexure(i: SlabDesignInput) -> SlabDesignOutput:
    d = i.thickness_mm - i.effective_cover_mm
    if d <= 0:
        raise ValueError("Effective depth d is non-positive. Check thickness/cover.")

    # simple assumption: j ≈ 0.9 d
    j = 0.9 * d

    # Mu in kNm/m → Nmm/m
    mu_Nmm = i.mu_kNm_per_m * 1e6

    # Required Ast (IS 456 style simplified)
    ast_req = mu_Nmm / (0.87 * i.fy_MPa * j)

    # Minimum steel (for slabs IS456 ~0.12% of b*d for Fe415) → for 1m width: b = 1000 mm
    ast_min = 0.0012 * 1000.0 * d

    ast_req_final = max(ast_req, ast_min)

    # Provided steel per meter with bar dia and spacing 's'
    # ast_per_meter = (π φ² / 4) * (1000 / s)
    # → s = (π φ² / 4) * 1000 / Ast_req
    phi = i.bar_dia_mm
    area_bar = math.pi * phi * phi / 4.0
    spacing = (area_bar * 1000.0) / ast_req_final

    ast_prov = area_bar * (1000.0 / spacing)

    return SlabDesignOutput(
        effective_depth_mm=d,
        mu_kNm_per_m=i.mu_kNm_per_m,
        ast_required_mm2_per_m=ast_req,
        ast_min_mm2_per_m=ast_min,
        ast_provided_mm2_per_m=ast_prov,
        spacing_mm=spacing,
    )


# Helper: calculate Mu for 1-way slab with UDL
def one_way_slab_mu_kNm_per_m(span_m: float, w_kN_m2: float, strip_width_m: float = 1.0,
                              coeff: float = 1/8) -> float:
    """
    span_m: clear span (m)
    w_kN_m2: factored load per m²
    strip_width_m: usually 1 m
    coeff: bending moment coefficient (simply supported ≈ 1/8, continuous ≈ 1/12)
    """
    w_kN_m = w_kN_m2 * strip_width_m
    mu = coeff * w_kN_m * span_m * span_m
    return mu


@dataclass
class TwoWaySlabInput:
    lx_m: float
    ly_m: float
    w_kN_m2: float
    alpha_x: float   # moment coef in short span
    alpha_y: float   # moment coef in long span


@dataclass
class TwoWaySlabMomentOutput:
    mu_x_kNm_per_m: float
    mu_y_kNm_per_m: float


def two_way_slab_moments(i: TwoWaySlabInput) -> TwoWaySlabMomentOutput:
    # For 1 m strip
    w = i.w_kN_m2
    mu_x = i.alpha_x * w * i.lx_m * i.lx_m
    mu_y = i.alpha_y * w * i.ly_m * i.ly_m
    return TwoWaySlabMomentOutput(mu_x_kNm_per_m=mu_x, mu_y_kNm_per_m=mu_y)
