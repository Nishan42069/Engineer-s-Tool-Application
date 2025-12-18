import streamlit as st
from calculators.volume.solid_geometrys.triangle_dumper import TriangleDumperInput, calculate_triangle_dumper

def render():
    st.header("Triangle Dumper Volume")

    st.subheader("Dimensions")
    cols = st.columns(3)
    with cols[0]:
        L = st.number_input("Length (m)", min_value=0.0, value=3.0)
    with cols[1]:
        b = st.number_input("Triangle base (m)", min_value=0.0, value=2.0)
    with cols[2]:
        h = st.number_input("Triangle height (m)", min_value=0.0, value=1.0)

    if st.button("Calculate"):
        out = calculate_triangle_dumper(TriangleDumperInput(length_m=L, base_m=b, height_m=h))
        st.subheader("Results")
        r = st.columns(3)
        r[0].metric("Area (m²)", f"{out.cross_area_m2:.6f}")
        r[1].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        r[2].metric("Volume (L)", f"{out.volume_litre:.2f}")
