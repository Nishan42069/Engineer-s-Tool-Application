import streamlit as st
from calculators.area.basic_shape.trapezoid import TrapezoidInput, calculate_trapezoid

def render():
    st.header("Trapezoid Area")

    st.subheader("Inputs")
    cols = st.columns(3)
    with cols[0]:
        a = st.number_input("Top width a (m)", min_value=0.0, value=1.5)
    with cols[1]:
        b = st.number_input("Bottom width b (m)", min_value=0.0, value=2.5)
    with cols[2]:
        h = st.number_input("Height (m)", min_value=0.0, value=1.0)

    if st.button("Calculate"):
        out = calculate_trapezoid(TrapezoidInput(top_width_m=a, bottom_width_m=b, height_m=h))
        st.subheader("Results")
        st.metric("Area (m²)", f"{out.area_m2:.6f}")
