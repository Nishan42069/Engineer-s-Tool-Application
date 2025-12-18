import streamlit as st
from calculators.metal.steel_weights.round_bar import RoundBarInput, calculate_round_bar

def render():
    st.header("Round Bar Weight")

    st.subheader("Dimensions")
    cols = st.columns(2)
    with cols[0]:
        diameter_mm = st.number_input("Diameter (mm)", min_value=0.0, value=16.0)
    with cols[1]:
        length_m = st.number_input("Length (m)", min_value=0.0, value=6.0)

    st.subheader("Material")
    density_cols = st.columns(1)
    with density_cols[0]:
        density = st.number_input("Steel density (kg/m³)", min_value=0.0, value=7850.0)

    if st.button("Calculate"):
        out = calculate_round_bar(RoundBarInput(diameter_mm=diameter_mm, length_m=length_m, density_kgm3=density))

        st.subheader("Results")
        r = st.columns(3)
        r[0].metric("Area (m²)", f"{out.area_m2:.6f}")
        r[1].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        r[2].metric("Weight (kg)", f"{out.weight_kg:.3f}")
