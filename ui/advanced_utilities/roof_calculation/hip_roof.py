import streamlit as st
from calculators.advanced_utilities.roof_calculation.hip_roof import (
    HipRoofInput,
    calculate_hip_roof,
)

def render():
    st.header("Hip Roof Calculation")

    length_ft = st.number_input("Roof Length (ft)", min_value=0.0, value=20.0)
    width_ft = st.number_input("Roof Width (ft)", min_value=0.0, value=10.0)
    slope_angle_deg = st.number_input("Roof Slope Angle (°)", min_value=0.0, value=30.0)

    if st.button("Calculate Hip Roof Area"):
        inp = HipRoofInput(length_ft=length_ft, width_ft=width_ft, slope_angle_deg=slope_angle_deg)
        area = calculate_hip_roof(inp)

        st.subheader("Results")
        st.write(f"Roof Area: **{area:.2f} ft²**")
