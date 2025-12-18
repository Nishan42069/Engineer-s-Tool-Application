import streamlit as st
from calculators.metal.steel_weights.square_tubing import SquareTubingInput, calculate_square_tubing

def render():
    st.header("Square Tubing Weight")

    st.subheader("Dimensions")
    cols = st.columns(3)
    with cols[0]:
        outer_mm = st.number_input("Outer side (mm)", min_value=0.0, value=50.0)
    with cols[1]:
        t_mm = st.number_input("Thickness (mm)", min_value=0.0, value=2.0)
    with cols[2]:
        length_m = st.number_input("Length (m)", min_value=0.0, value=6.0)

    st.subheader("Material")
    density = st.number_input("Steel density (kg/m³)", min_value=0.0, value=7850.0)

    if st.button("Calculate"):
        out = calculate_square_tubing(SquareTubingInput(outer_side_mm=outer_mm, thickness_mm=t_mm, length_m=length_m, density_kgm3=density))

        st.subheader("Results")
        r = st.columns(3)
        r[0].metric("Area (m²)", f"{out.area_m2:.6f}")
        r[1].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        r[2].metric("Weight (kg)", f"{out.weight_kg:.3f}")
