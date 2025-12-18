import streamlit as st
from calculators.quantity_n_material.soil_mechanics.saturated_unit_weight import (
    SaturatedUnitWeightInput,
    calculate_saturated_unit_weight,
)


def render():
    st.header("Saturated Unit Weight of Soil")

    st.subheader("Inputs")
    c = st.columns(3)
    with c[0]:
        Gs = st.number_input("Specific gravity Gs", min_value=1.0, value=2.65)
    with c[1]:
        e = st.number_input("Void ratio e", min_value=0.0, value=0.7)
    with c[2]:
        gamma_w = st.number_input(
            "γw (kN/m³)", min_value=0.0, value=9.81
        )

    if st.button("Calculate γsat"):
        inp = SaturatedUnitWeightInput(
            specific_gravity=Gs,
            void_ratio=e,
            gamma_w_kN_m3=gamma_w,
        )
        out = calculate_saturated_unit_weight(inp)

        st.subheader("Result")
        st.metric("Saturated unit weight γsat (kN/m³)", f"{out.saturated_unit_weight_kN_m3:.2f}")
