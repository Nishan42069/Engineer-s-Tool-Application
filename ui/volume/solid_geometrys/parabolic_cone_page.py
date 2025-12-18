import streamlit as st
from calculators.volume.solid_geometrys.parabolic_cone import ParabolicConeInput, calculate_parabolic_cone

def render():
    st.header("Parabolic Cone Volume (Paraboloid)")

    st.subheader("Dimensions")
    cols = st.columns(2)
    with cols[0]:
        r = st.number_input("Radius (m)", min_value=0.0, value=0.5)
    with cols[1]:
        h = st.number_input("Height (m)", min_value=0.0, value=1.0)

    if st.button("Calculate"):
        out = calculate_parabolic_cone(ParabolicConeInput(radius_m=r, height_m=h))
        st.subheader("Results")
        c = st.columns(2)
        c[0].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        c[1].metric("Volume (L)", f"{out.volume_litre:.2f}")
