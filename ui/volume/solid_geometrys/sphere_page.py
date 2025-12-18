import streamlit as st
from calculators.volume.solid_geometrys.sphere import SphereInput, calculate_sphere

def render():
    st.header("Sphere Volume")

    st.subheader("Dimensions")
    r = st.number_input("Radius (m)", min_value=0.0, value=0.5)

    if st.button("Calculate"):
        out = calculate_sphere(SphereInput(radius_m=r))
        st.subheader("Results")
        cols = st.columns(2)
        cols[0].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        cols[1].metric("Volume (L)", f"{out.volume_litre:.2f}")
