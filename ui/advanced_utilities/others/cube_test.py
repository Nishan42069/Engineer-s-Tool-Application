import streamlit as st
from calculators.advanced_utilities.others.cube_test import (
    CubeTestInput,
    calculate_cube_test,
)

def render():
    st.header("Cube Test Calculation")

    load_kn = st.number_input("Load (kN)", min_value=0.0, value=50.0)
    area_cm2 = st.number_input("Area (cm²)", min_value=0.0, value=100.0)

    if st.button("Calculate Cube Test Strength"):
        inp = CubeTestInput(load_kn=load_kn, area_cm2=area_cm2)
        strength = calculate_cube_test(inp)

        st.subheader("Results")
        st.write(f"Cube Strength: **{strength:.2f} MPa**")
