import streamlit as st
from calculators.advanced_utilities.stair_foundation.stair_geometry import (
    StairGeometryInput,
    calculate_stair_geometry,
)

def render():
    st.header("Stair Geometry Calculation")

    tread_inch = st.number_input("Tread (inches)", min_value=0.0, value=10.0)
    riser_inch = st.number_input("Riser (inches)", min_value=0.0, value=8.0)
    steps_count = st.number_input("Steps Count", min_value=1, value=10)

    if st.button("Calculate Stair Geometry Area"):
        inp = StairGeometryInput(tread_inch=tread_inch, riser_inch=riser_inch, steps_count=steps_count)
        area = calculate_stair_geometry(inp)

        st.subheader("Results")
        st.write(f"Total Stair Area: **{area:.2f} in²**")
