import streamlit as st
from calculators.advanced_utilities.road_drainage.box_culvert import (
    BoxCulvertInput,
    calculate_box_culvert,
)

def render():
    st.header("Box Culvert Volume Calculation")

    length_ft = st.number_input("Length of Box Culvert (ft)", min_value=0.0, value=10.0)
    width_ft = st.number_input("Width of Box Culvert (ft)", min_value=0.0, value=5.0)
    height_ft = st.number_input("Height of Box Culvert (ft)", min_value=0.0, value=6.0)

    if st.button("Calculate Box Culvert Volume"):
        inp = BoxCulvertInput(length_ft=length_ft, width_ft=width_ft, height_ft=height_ft)
        volume = calculate_box_culvert(inp)

        st.subheader("Results")
        st.write(f"Box Culvert Volume: **{volume:.3f} ft³**")
