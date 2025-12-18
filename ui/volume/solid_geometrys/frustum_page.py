import streamlit as st
from calculators.volume.solid_geometrys.frustum import FrustumInput, calculate_frustum

def render():
    st.header("Frustum Volume (Cone)")

    st.subheader("Dimensions")
    cols = st.columns(3)
    with cols[0]:
        r_top = st.number_input("Top radius (m)", min_value=0.0, value=0.3)
    with cols[1]:
        r_bot = st.number_input("Bottom radius (m)", min_value=0.0, value=0.6)
    with cols[2]:
        h = st.number_input("Height (m)", min_value=0.0, value=1.0)

    if st.button("Calculate"):
        out = calculate_frustum(FrustumInput(radius_top_m=r_top, radius_bottom_m=r_bot, height_m=h))
        st.subheader("Results")
        c = st.columns(2)
        c[0].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        c[1].metric("Volume (L)", f"{out.volume_litre:.2f}")
