import streamlit as st
from calculators.advanced_utilities.road_drainage.gabion import (
    GabionInput,
    calculate_gabion,
)

def render():
    st.header("Gabion Wall Volume Calculation")

    length_ft = st.number_input("Length of Gabion (ft)", min_value=0.0, value=10.0)
    width_ft = st.number_input("Width of Gabion (ft)", min_value=0.0, value=5.0)
    height_ft = st.number_input("Height of Gabion (ft)", min_value=0.0, value=6.0)

    if st.button("Calculate Gabion Volume"):
        inp = GabionInput(length_ft=length_ft, width_ft=width_ft, height_ft=height_ft)
        volume = calculate_gabion(inp)

        st.subheader("Results")
        st.write(f"Gabion Volume: **{volume:.3f} ft³**")
