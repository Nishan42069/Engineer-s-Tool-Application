import streamlit as st
from calculators.area.basic_shape.circle import CircleInput, calculate_circle

def render():
    st.header("Circle Area")

    st.subheader("Inputs")
    r = st.number_input("Radius (m)", min_value=0.0, value=1.0)

    if st.button("Calculate"):
        out = calculate_circle(CircleInput(radius_m=r))
        st.subheader("Results")
        st.metric("Area (m²)", f"{out.area_m2:.6f}")
