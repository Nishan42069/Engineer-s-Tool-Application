import streamlit as st
from calculators.advanced_utilities.road_drainage.curve_asphalt import (
    CurveAsphaltInput,
    calculate_curve_asphalt,
)

def render():
    st.header("Curve Asphalt Calculation")

    curve_length_ft = st.number_input("Curve Length (ft)", min_value=0.0, value=100.0)
    curve_radius_ft = st.number_input("Curve Radius (ft)", min_value=0.0, value=20.0)
    thickness_ft = st.number_input("Asphalt Thickness (ft)", min_value=0.0, value=0.25)

    if st.button("Calculate Curve Asphalt Volume"):
        inp = CurveAsphaltInput(curve_length_ft=curve_length_ft, curve_radius_ft=curve_radius_ft, thickness_ft=thickness_ft)
        volume = calculate_curve_asphalt(inp)

        st.subheader("Results")
        st.write(f"Asphalt Volume: **{volume:.3f} ft³**")
