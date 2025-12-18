import streamlit as st
from calculators.advanced_utilities.road_drainage.pipe_culvert import (
    PipeCulvertInput,
    calculate_pipe_culvert,
)

def render():
    st.header("Pipe Culvert Volume Calculation")

    diameter_ft = st.number_input("Pipe Diameter (ft)", min_value=0.0, value=3.0)
    length_ft = st.number_input("Pipe Length (ft)", min_value=0.0, value=20.0)

    if st.button("Calculate Pipe Culvert Volume"):
        inp = PipeCulvertInput(diameter_ft=diameter_ft, length_ft=length_ft)
        volume = calculate_pipe_culvert(inp)

        st.subheader("Results")
        st.write(f"Pipe Culvert Volume: **{volume:.3f} ft³**")
