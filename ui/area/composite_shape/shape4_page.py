import streamlit as st
from calculators.area.composite_shape.shape4_tapering_rectangle import Shape4Input, calculate_shape4

def render():
    st.header("Shape 4: Tapering Rectangle")

    st.subheader("Inputs")
    cols = st.columns(3)
    with cols[0]:
        w1 = st.number_input("Width at end 1 (m)", min_value=0.0, value=2.0)
    with cols[1]:
        w2 = st.number_input("Width at end 2 (m)", min_value=0.0, value=1.0)
    with cols[2]:
        L = st.number_input("Length (m)", min_value=0.0, value=5.0)

    if st.button("Calculate"):
        out = calculate_shape4(Shape4Input(width_end1_m=w1, width_end2_m=w2, length_m=L))
        st.subheader("Results")
        st.metric("Area (m²)", f"{out.area_m2:.6f}")
