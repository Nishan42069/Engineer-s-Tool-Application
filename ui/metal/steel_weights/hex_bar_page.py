import streamlit as st
from calculators.metal.steel_weights.hex_bar import HexBarInput, calculate_hex_bar

def render():
    st.header("Hexagonal Bar Weight")

    st.subheader("Dimensions")
    cols = st.columns(2)
    with cols[0]:
        flats_mm = st.number_input("Across flats (mm)", min_value=0.0, value=20.0)
    with cols[1]:
        length_m = st.number_input("Length (m)", min_value=0.0, value=6.0)

    st.subheader("Material")
    density = st.number_input("Steel density (kg/m³)", min_value=0.0, value=7850.0)

    if st.button("Calculate"):
        out = calculate_hex_bar(HexBarInput(across_flats_mm=flats_mm, length_m=length_m, density_kgm3=density))

        st.subheader("Results")
        r = st.columns(3)
        r[0].metric("Area (m²)", f"{out.area_m2:.6f}")
        r[1].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        r[2].metric("Weight (kg)", f"{out.weight_kg:.3f}")
