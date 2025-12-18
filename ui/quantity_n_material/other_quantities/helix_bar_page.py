import streamlit as st
from calculators.quantity_n_material.other_quantities.helix_bar import (
    HelixBarInput,
    calculate_helix_bar,
)


def render():
    st.header("Helix Bar Length & Weight")

    st.subheader("Inputs")
    c1, c2, c3 = st.columns(3)
    with c1:
        D = st.number_input("Core diameter (mm)", min_value=0.0, value=300.0)
    with c2:
        pitch = st.number_input("Pitch (mm)", min_value=1.0, value=150.0)
    with c3:
        h = st.number_input("Column height (mm)", min_value=0.0, value=3000.0)

    c4, c5 = st.columns(2)
    with c4:
        dia = st.number_input("Bar diameter (mm)", min_value=4.0, value=8.0)
    with c5:
        extra = st.number_input("Extra length (hooks, mm)", min_value=0.0, value=300.0)

    if st.button("Calculate helix bar"):
        inp = HelixBarInput(
            core_diameter_mm=D,
            pitch_mm=pitch,
            column_height_mm=h,
            bar_diameter_mm=dia,
            extra_length_mm=extra,
        )
        out = calculate_helix_bar(inp)

        st.subheader("Results")
        st.write(f"Number of turns: **{out.turns:.2f}**")
        st.write(f"Total bar length: **{out.bar_length_m:.2f} m**")
        st.write(f"Unit weight: **{out.unit_weight_kg_per_m:.3f} kg/m**")
        st.success(f"Total weight: **{out.total_weight_kg:.2f} kg**")
