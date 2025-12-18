import streamlit as st
from calculators.area.composite_shape.shape1_rect_plus_triangle_head import Shape1Input, calculate_shape1

def render():
    st.header("Shape 1: Rectangle + Triangle Head")

    st.subheader("Rectangle")
    r = st.columns(2)
    with r[0]:
        L = st.number_input("Rect length (m)", min_value=0.0, value=4.0)
    with r[1]:
        W = st.number_input("Rect width (m)", min_value=0.0, value=2.0)

    st.subheader("Triangle Head")
    t = st.columns(2)
    with t[0]:
        b = st.number_input("Triangle base (m)", min_value=0.0, value=2.0)
    with t[1]:
        h = st.number_input("Triangle height (m)", min_value=0.0, value=1.5)

    if st.button("Calculate"):
        out = calculate_shape1(Shape1Input(rect_length_m=L, rect_width_m=W, tri_base_m=b, tri_height_m=h))
        st.subheader("Results")
        cols = st.columns(3)
        cols[0].metric("Rect area (m²)", f"{out.rect_area_m2:.6f}")
        cols[1].metric("Tri area (m²)", f"{out.tri_area_m2:.6f}")
        cols[2].metric("Total area (m²)", f"{out.total_area_m2:.6f}")
