import streamlit as st
from calculators.quantity_n_material.other_quantities.rebar_straight import (
    RebarStraightInput,
    calculate_rebar_straight,
)


def render():
    st.header("Reinforcement Steel (Straight Bars)")

    c1, c2, c3 = st.columns(3)
    with c1:
        dia = st.number_input("Bar diameter (mm)", min_value=4.0, value=12.0)
    with c2:
        length = st.number_input("Bar length (m)", min_value=0.0, value=6.0)
    with c3:
        n = st.number_input("Number of bars", min_value=1, value=10)

    if st.button("Calculate steel weight"):
        inp = RebarStraightInput(
            bar_diameter_mm=dia,
            bar_length_m=length,
            number_of_bars=n,
        )
        out = calculate_rebar_straight(inp)

        st.subheader("Results")
        st.write(f"Total length: **{out.total_length_m:.2f} m**")
        st.write(f"Unit weight: **{out.unit_weight_kg_m:.3f} kg/m**")
        st.success(f"Total steel weight: **{out.total_weight_kg:.2f} kg**")
