import streamlit as st
from calculators.area.basic_shape.rectangle import RectangleInput, calculate_rectangle

def render():
    st.header("Rectangle Area")

    st.subheader("Inputs")
    cols = st.columns(2)
    with cols[0]:
        L = st.number_input("Length (m)", min_value=0.0, value=2.0)
    with cols[1]:
        B = st.number_input("Width (m)", min_value=0.0, value=1.5)

    if st.button("Calculate"):
        out = calculate_rectangle(RectangleInput(length_m=L, width_m=B))
        st.subheader("Results")
        st.metric("Area (m²)", f"{out.area_m2:.6f}")
