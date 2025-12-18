import streamlit as st
from calculators.advanced_utilities.stair_foundation.plumb_concrete import (
    PlumbConcreteInput,
    calculate_plumb_concrete,
)

def render():
    st.header("Plumb Concrete Calculation")

    length_ft = st.number_input("Length (ft)", min_value=0.0, value=10.0)
    width_ft = st.number_input("Width (ft)", min_value=0.0, value=5.0)
    thickness_ft = st.number_input("Thickness (ft)", min_value=0.0, value=1.0)

    if st.button("Calculate Plumb Concrete Volume"):
        inp = PlumbConcreteInput(length_ft=length_ft, width_ft=width_ft, thickness_ft=thickness_ft)
        volume = calculate_plumb_concrete(inp)

        st.subheader("Results")
        st.write(f"Plumb Concrete Volume: **{volume:.3f} ft³**")
