import streamlit as st
from calculators.area.composite_shape.shape3_rect_plus_two_semicircles import Shape3Input, calculate_shape3

def render():
    st.header("Shape 3: Rectangle + Two Semicircles (Capsule)")

    st.subheader("Rectangle")
    r = st.columns(2)
    with r[0]:
        L = st.number_input("Rect length (m)", min_value=0.0, value=4.0)
    with r[1]:
        W = st.number_input("Rect width (m)", min_value=0.0, value=2.0)

    st.subheader("Semicircle Ends")
    radius = st.number_input("Radius (m)", min_value=0.0, value=1.0)

    if st.button("Calculate"):
        out = calculate_shape3(Shape3Input(rect_length_m=L, rect_width_m=W, radius_m=radius))
        st.subheader("Results")
        cols = st.columns(3)
        cols[0].metric("Rect area (m²)", f"{out.rect_area_m2:.6f}")
        cols[1].metric("Circle area (m²)", f"{out.circle_area_m2:.6f}")
        cols[2].metric("Total area (m²)", f"{out.total_area_m2:.6f}")
