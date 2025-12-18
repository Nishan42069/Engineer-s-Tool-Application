import streamlit as st
from calculators.quantity_n_material.soil_mechanics.thermal_diffusivity import (
    ThermalDiffusivityInput,
    calculate_thermal_diffusivity,
)


def render():
    st.header("Thermal Diffusivity of Soil")

    st.subheader("Inputs")
    c1, c2, c3 = st.columns(3)
    with c1:
        k = st.number_input("Thermal conductivity k (W/m·K)", min_value=0.0, value=1.5)
    with c2:
        rho = st.number_input("Density ρ (kg/m³)", min_value=0.0, value=1800.0)
    with c3:
        c_kJ = st.number_input("Specific heat c (kJ/kg·K)", min_value=0.0, value=0.9)

    if st.button("Calculate α"):
        inp = ThermalDiffusivityInput(
            thermal_conductivity_W_mK=k,
            density_kg_m3=rho,
            specific_heat_kJ_kgK=c_kJ,
        )
        out = calculate_thermal_diffusivity(inp)

        st.subheader("Result")
        st.metric("Thermal diffusivity α (m²/s)", f"{out.alpha_m2_s:.3e}")
