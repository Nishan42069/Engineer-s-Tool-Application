import streamlit as st
from calculators.area.basic_shape.ellipse import EllipseInput, calculate_ellipse

def render():
    st.header("Ellipse Area")

    st.subheader("Inputs")
    cols = st.columns(2)
    with cols[0]:
        a = st.number_input("Semi-major a (m)", min_value=0.0, value=2.0)
    with cols[1]:
        b = st.number_input("Semi-minor b (m)", min_value=0.0, value=1.0)

    if st.button("Calculate"):
        out = calculate_ellipse(EllipseInput(semi_major_a_m=a, semi_minor_b_m=b))
        st.subheader("Results")
        st.metric("Area (m²)", f"{out.area_m2:.6f}")
