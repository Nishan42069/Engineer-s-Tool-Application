import streamlit as st
from calculators.area.basic_shape.triangle import TriangleInput, calculate_triangle

def render():
    st.header("Triangle Area")

    st.subheader("Inputs")
    cols = st.columns(2)
    with cols[0]:
        b = st.number_input("Base (m)", min_value=0.0, value=2.0)
    with cols[1]:
        h = st.number_input("Height (m)", min_value=0.0, value=1.0)

    if st.button("Calculate"):
        out = calculate_triangle(TriangleInput(base_m=b, height_m=h))
        st.subheader("Results")
        st.metric("Area (m²)", f"{out.area_m2:.6f}")
