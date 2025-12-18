import streamlit as st
from calculators.volume.solid_geometrys.rectangular_prism import RectPrismInput, calculate_rectangular_prism

def render():
    st.header("Rectangular Prism Volume")

    st.subheader("Dimensions")
    cols = st.columns(3)
    with cols[0]:
        L = st.number_input("Length (m)", min_value=0.0, value=2.0)
    with cols[1]:
        B = st.number_input("Width (m)", min_value=0.0, value=1.5)
    with cols[2]:
        H = st.number_input("Height (m)", min_value=0.0, value=1.0)

    if st.button("Calculate"):
        out = calculate_rectangular_prism(RectPrismInput(length_m=L, width_m=B, height_m=H))
        st.subheader("Results")
        r = st.columns(2)
        r[0].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        r[1].metric("Volume (L)", f"{out.volume_litre:.2f}")
