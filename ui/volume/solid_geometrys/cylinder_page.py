import streamlit as st
from calculators.volume.solid_geometrys.cylinder import CylinderInput, calculate_cylinder

def render():
    st.header("Cylinder Volume")

    st.subheader("Dimensions")
    cols = st.columns(2)
    with cols[0]:
        r = st.number_input("Radius (m)", min_value=0.0, value=0.5)
    with cols[1]:
        h = st.number_input("Height (m)", min_value=0.0, value=2.0)

    if st.button("Calculate"):
        out = calculate_cylinder(CylinderInput(radius_m=r, height_m=h))
        st.subheader("Results")
        rcols = st.columns(2)
        rcols[0].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        rcols[1].metric("Volume (L)", f"{out.volume_litre:.2f}")
