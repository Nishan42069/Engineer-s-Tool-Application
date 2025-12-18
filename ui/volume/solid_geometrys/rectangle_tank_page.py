import streamlit as st
from calculators.volume.solid_geometrys.rectangle_tank import RectangleTankInput, calculate_rectangle_tank

def render():
    st.header("Rectangle Tank Capacity")

    st.subheader("Inner Dimensions")
    cols = st.columns(3)
    with cols[0]:
        L = st.number_input("Length (m)", min_value=0.0, value=2.0)
    with cols[1]:
        B = st.number_input("Width (m)", min_value=0.0, value=1.5)
    with cols[2]:
        H = st.number_input("Water height (m)", min_value=0.0, value=1.2)

    if st.button("Calculate"):
        out = calculate_rectangle_tank(RectangleTankInput(length_m=L, width_m=B, water_height_m=H))
        st.subheader("Results")
        r = st.columns(2)
        r[0].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        r[1].metric("Capacity (L)", f"{out.capacity_litre:.2f}")
