import streamlit as st
from calculators.metal.steel_weights.angle import AngleInput, calculate_angle

def render():
    st.header("Angle Weight (L-Section)")

    st.subheader("Dimensions")
    cols = st.columns(4)
    with cols[0]:
        a_mm = st.number_input("Leg a (mm)", min_value=0.0, value=50.0)
    with cols[1]:
        b_mm = st.number_input("Leg b (mm)", min_value=0.0, value=50.0)
    with cols[2]:
        t_mm = st.number_input("Thickness t (mm)", min_value=0.0, value=6.0)
    with cols[3]:
        length_m = st.number_input("Length (m)", min_value=0.0, value=6.0)

    st.subheader("Material")
    density = st.number_input("Steel density (kg/m³)", min_value=0.0, value=7850.0)

    if st.button("Calculate"):
        out = calculate_angle(AngleInput(leg_a_mm=a_mm, leg_b_mm=b_mm, thickness_mm=t_mm, length_m=length_m, density_kgm3=density))

        st.subheader("Results")
        r = st.columns(3)
        r[0].metric("Area (m²)", f"{out.area_m2:.6f}")
        r[1].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        r[2].metric("Weight (kg)", f"{out.weight_kg:.3f}")
