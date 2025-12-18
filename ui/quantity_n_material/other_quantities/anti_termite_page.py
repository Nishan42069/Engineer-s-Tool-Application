import streamlit as st
from calculators.quantity_n_material.other_quantities.anti_termite import (
    AntiTermiteInput,
    calculate_anti_termite,
)


def render():
    st.header("Anti-Termite Chemical Calculator")

    c1, c2 = st.columns(2)
    with c1:
        area = st.number_input("Treatment area (m²)", min_value=0.0, value=80.0)
    with c2:
        rate = st.number_input("Application rate (L/m²)", min_value=0.0, value=0.5)

    if st.button("Calculate chemical quantity"):
        inp = AntiTermiteInput(
            area_m2=area,
            application_rate_L_m2=rate,
        )
        out = calculate_anti_termite(inp)

        st.subheader("Result")
        st.success(f"Required chemical: **{out.chemical_litres:.2f} L**")
