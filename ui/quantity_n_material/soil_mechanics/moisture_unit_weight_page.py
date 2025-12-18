import streamlit as st
from calculators.quantity_n_material.soil_mechanics.moisture_unit_weight import (
    MoistureUnitWeightInput,
    calculate_moisture_unit_weight,
)


def render():
    st.header("Moisture (Bulk) Unit Weight of Soil")

    st.subheader("Inputs")
    c = st.columns(2)
    with c[0]:
        gamma_d = st.number_input(
            "Dry unit weight γd (kN/m³)", min_value=0.0, value=16.0
        )
    with c[1]:
        w_percent = st.number_input(
            "Water content w (%)", min_value=0.0, value=15.0
        )

    if st.button("Calculate bulk unit weight"):
        inp = MoistureUnitWeightInput(
            dry_unit_weight_kN_m3=gamma_d,
            water_content_percent=w_percent,
        )
        out = calculate_moisture_unit_weight(inp)

        st.subheader("Result")
        st.metric("Bulk unit weight γ (kN/m³)", f"{out.bulk_unit_weight_kN_m3:.2f}")
