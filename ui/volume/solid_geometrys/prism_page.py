import streamlit as st
from calculators.volume.solid_geometrys.prism import PrismInput, calculate_prism

def render():
    st.header("Prism Volume (Base Area × Length)")

    st.subheader("Inputs")
    cols = st.columns(2)
    with cols[0]:
        A = st.number_input("Base area (m²)", min_value=0.0, value=1.5)
    with cols[1]:
        L = st.number_input("Length (m)", min_value=0.0, value=3.0)

    if st.button("Calculate"):
        out = calculate_prism(PrismInput(base_area_m2=A, length_m=L))
        st.subheader("Results")
        c = st.columns(2)
        c[0].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        c[1].metric("Volume (L)", f"{out.volume_litre:.2f}")
