import streamlit as st
from calculators.volume.solid_geometrys.cube import CubeInput, calculate_cube

def render():
    st.header("Cube Volume")

    st.subheader("Dimensions")
    s = st.number_input("Side (m)", min_value=0.0, value=1.0)

    if st.button("Calculate"):
        out = calculate_cube(CubeInput(side_m=s))
        st.subheader("Results")
        c = st.columns(2)
        c[0].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        c[1].metric("Volume (L)", f"{out.volume_litre:.2f}")
