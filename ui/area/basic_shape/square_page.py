import streamlit as st
from calculators.area.basic_shape.square import SquareInput, calculate_square

def render():
    st.header("Square Area")

    st.subheader("Inputs")
    s = st.number_input("Side (m)", min_value=0.0, value=1.0)

    if st.button("Calculate"):
        out = calculate_square(SquareInput(side_m=s))
        st.subheader("Results")
        st.metric("Area (m²)", f"{out.area_m2:.6f}")
