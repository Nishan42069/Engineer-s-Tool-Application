import streamlit as st
from calculators.quantity_n_material.other_quantities.water_tank_capacity import (
    WaterTankRectInput,
    calculate_water_tank_rect,
)


def render():
    st.header("Water Tank Capacity – Rectangular")

    c1, c2, c3 = st.columns(3)
    with c1:
        L = st.number_input("Inner length (m)", min_value=0.0, value=2.0)
    with c2:
        B = st.number_input("Inner width (m)", min_value=0.0, value=1.5)
    with c3:
        H = st.number_input("Water depth (m)", min_value=0.0, value=1.5)

    if st.button("Calculate tank capacity"):
        inp = WaterTankRectInput(
            inner_length_m=L,
            inner_width_m=B,
            water_height_m=H,
        )
        out = calculate_water_tank_rect(inp)

        st.subheader("Results")
        st.write(f"Volume: **{out.volume_m3:.3f} m³**")
        st.success(f"Capacity: **{out.capacity_litres:.0f} litres**")
