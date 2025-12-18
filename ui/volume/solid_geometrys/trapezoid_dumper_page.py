import streamlit as st
from calculators.volume.solid_geometrys.trapezoid_dumper import TrapezoidDumperInput, calculate_trapezoid_dumper

def render():
    st.header("Trapezoid Dumper Volume")

    st.subheader("Dimensions")
    cols = st.columns(4)
    with cols[0]:
        L = st.number_input("Length (m)", min_value=0.0, value=3.0)
    with cols[1]:
        a = st.number_input("Top width (m)", min_value=0.0, value=1.5)
    with cols[2]:
        b = st.number_input("Bottom width (m)", min_value=0.0, value=2.5)
    with cols[3]:
        h = st.number_input("Height (m)", min_value=0.0, value=1.0)

    if st.button("Calculate"):
        out = calculate_trapezoid_dumper(TrapezoidDumperInput(length_m=L, top_width_m=a, bottom_width_m=b, height_m=h))
        st.subheader("Results")
        r = st.columns(3)
        r[0].metric("Area (m²)", f"{out.cross_area_m2:.6f}")
        r[1].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        r[2].metric("Volume (L)", f"{out.volume_litre:.2f}")
