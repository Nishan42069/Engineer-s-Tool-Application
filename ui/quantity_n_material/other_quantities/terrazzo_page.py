import streamlit as st
from calculators.quantity_n_material.other_quantities.terrazzo import (
    TerrazzoInput,
    calculate_terrazzo,
)


def render():
    st.header("Terrazzo / Chips Flooring Calculator")

    c1, c2 = st.columns(2)
    with c1:
        area = st.number_input("Floor area (m²)", min_value=0.0, value=50.0)
    with c2:
        cement_rate = st.number_input("Cement consumption (kg/m²)", min_value=0.0, value=2.5)

    chips_rate = st.number_input("Chips consumption (kg/m²)", min_value=0.0, value=12.0)

    if st.button("Calculate terrazzo materials"):
        inp = TerrazzoInput(
            area_m2=area,
            cement_consumption_kg_m2=cement_rate,
            chips_consumption_kg_m2=chips_rate,
        )
        out = calculate_terrazzo(inp)

        st.subheader("Results")
        st.write(f"Cement required: **{out.cement_kg:.1f} kg**")
        st.success(f"Chips required: **{out.chips_kg:.1f} kg**")
