import streamlit as st
from calculators.quantity_n_material.soil_mechanics.submerged_unit_weight import (
    SubmergedUnitWeightInput,
    calculate_submerged_unit_weight,
)


def render():
    st.header("Submerged Unit Weight of Soil")

    st.subheader("Inputs")
    c1, c2 = st.columns(2)
    with c1:
        gamma_sat = st.number_input("Saturated unit weight γsat (kN/m³)", min_value=0.0, value=20.0)
    with c2:
        gamma_w = st.number_input("γw (kN/m³)", min_value=0.0, value=9.81)

    if st.button("Calculate γ'"):
        inp = SubmergedUnitWeightInput(
            saturated_unit_weight_kN_m3=gamma_sat,
            gamma_w_kN_m3=gamma_w,
        )
        out = calculate_submerged_unit_weight(inp)

        st.subheader("Result")
        st.metric("Submerged unit weight γ' (kN/m³)", f"{out.submerged_unit_weight_kN_m3:.2f}")
