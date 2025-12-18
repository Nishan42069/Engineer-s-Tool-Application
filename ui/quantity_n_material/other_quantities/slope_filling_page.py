import streamlit as st
from calculators.quantity_n_material.other_quantities.slope_filling import (
    SlopeFillingInput,
    calculate_slope_filling,
)


def render():
    st.header("Slope Filling Volume")

    c1, c2 = st.columns(2)
    with c1:
        h = st.number_input("Embankment height h (m)", min_value=0.0, value=2.0)
        b = st.number_input("Top width b (m)", min_value=0.0, value=3.0)
    with c2:
        z = st.number_input("Side slope (H:V) z", min_value=0.0, value=2.0)
        L = st.number_input("Length along road L (m)", min_value=0.0, value=50.0)

    if st.button("Calculate slope filling"):
        inp = SlopeFillingInput(
            embankment_height_m=h,
            top_width_m=b,
            side_slope_H_over_V=z,
            length_m=L,
        )
        out = calculate_slope_filling(inp)

        st.subheader("Results")
        st.write(f"Cross-section area: **{out.cross_section_area_m2:.3f} m²**")
        st.success(f"Total fill volume: **{out.volume_m3:.3f} m³**")
