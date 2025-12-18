import streamlit as st
from calculators.quantity_n_material.soil_mechanics.specific_weight import (
    SpecificWeightInput,
    calculate_specific_weight,
)


def render():
    st.header("Specific (Unit) Weight")

    st.subheader("Inputs")
    c1, c2 = st.columns(2)
    with c1:
        W = st.number_input("Weight W (kN)", min_value=0.0, value=180.0)
    with c2:
        V = st.number_input("Volume V (m³)", min_value=0.0, value=10.0)

    if st.button("Calculate γ"):
        inp = SpecificWeightInput(weight_kN=W, volume_m3=V)
        out = calculate_specific_weight(inp)

        st.subheader("Result")
        st.metric("Unit weight γ (kN/m³)", f"{out.unit_weight_kN_m3:.2f}")
