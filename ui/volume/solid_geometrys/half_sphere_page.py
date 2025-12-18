import streamlit as st
from calculators.volume.solid_geometrys.half_sphere import HalfSphereInput, calculate_half_sphere

def render():
    st.header("Half Sphere Volume (Hemisphere)")

    st.subheader("Dimensions")
    r = st.number_input("Radius (m)", min_value=0.0, value=0.5)

    if st.button("Calculate"):
        out = calculate_half_sphere(HalfSphereInput(radius_m=r))
        st.subheader("Results")
        c = st.columns(2)
        c[0].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        c[1].metric("Volume (L)", f"{out.volume_litre:.2f}")
