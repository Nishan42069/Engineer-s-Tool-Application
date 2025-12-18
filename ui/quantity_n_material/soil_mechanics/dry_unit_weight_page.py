import streamlit as st
from calculators.quantity_n_material.soil_mechanics.dry_unit_weight import (
    DryUnitWeightInput,
    calculate_dry_unit_weight,
)


def render():
    st.header("Dry Unit Weight of Soil")

    st.subheader("Inputs")
    c = st.columns(2)
    with c[0]:
        gamma_bulk = st.number_input(
            "Bulk unit weight γ (kN/m³)", min_value=0.0, value=18.0
        )
    with c[1]:
        w_percent = st.number_input(
            "Water content w (%)", min_value=0.0, value=15.0
        )

    if st.button("Calculate dry unit weight"):
        inp = DryUnitWeightInput(
            bulk_unit_weight_kN_m3=gamma_bulk,
            water_content_percent=w_percent,
        )
        out = calculate_dry_unit_weight(inp)

        st.subheader("Result")
        st.metric("Dry unit weight γd (kN/m³)", f"{out.dry_unit_weight_kN_m3:.2f}")
