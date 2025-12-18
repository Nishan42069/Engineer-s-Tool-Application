import streamlit as st
from calculators.area.composite_shape.shape2_rect_plus_half_circle import Shape2Input, calculate_shape2

def render():
    st.header("Shape 2: Rectangle + Half Circle")

    st.subheader("Rectangle")
    r = st.columns(2)
    with r[0]:
        L = st.number_input("Rect length (m)", min_value=0.0, value=4.0)
    with r[1]:
        W = st.number_input("Rect width (m)", min_value=0.0, value=2.0)

    st.subheader("Half Circle")
    radius = st.number_input("Radius (m)", min_value=0.0, value=1.0)

    if st.button("Calculate"):
        out = calculate_shape2(Shape2Input(rect_length_m=L, rect_width_m=W, radius_m=radius))
        st.subheader("Results")
        cols = st.columns(3)
        cols[0].metric("Rect area (m²)", f"{out.rect_area_m2:.6f}")
        cols[1].metric("Half-circle (m²)", f"{out.semicircle_area_m2:.6f}")
        cols[2].metric("Total area (m²)", f"{out.total_area_m2:.6f}")
