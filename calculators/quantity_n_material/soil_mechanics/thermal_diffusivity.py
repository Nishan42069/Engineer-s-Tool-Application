from dataclasses import dataclass


@dataclass
class ThermalDiffusivityInput:
    thermal_conductivity_W_mK: float  # k
    density_kg_m3: float              # ρ
    specific_heat_kJ_kgK: float       # c (kJ/kgK)


@dataclass
class ThermalDiffusivityOutput:
    alpha_m2_s: float


def calculate_thermal_diffusivity(i: ThermalDiffusivityInput) -> ThermalDiffusivityOutput:
    if i.density_kg_m3 <= 0:
        raise ValueError("Density must be greater than zero.")
    if i.specific_heat_kJ_kgK <= 0:
        raise ValueError("Specific heat must be greater than zero.")

    c_J_kgK = i.specific_heat_kJ_kgK * 1000.0  # convert kJ/kgK → J/kgK
    alpha = i.thermal_conductivity_W_mK / (i.density_kg_m3 * c_J_kgK)
    return ThermalDiffusivityOutput(alpha_m2_s=alpha)
