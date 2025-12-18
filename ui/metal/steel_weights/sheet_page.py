import streamlit as st
from calculators.metal.steel_weights.sheet import SheetInput, calculate_sheet

def render():
    st.header("Sheet Weight")

    st.subheader("Dimensions")
    cols = st.columns(3)
    with cols[0]:
        L = st.number_input("Length (m)", min_value=0.0, value=2.44)
    with cols[1]:
        W = st.number_input("Width (m)", min_value=0.0, value=1.22)
    with cols[2]:
        t_mm = st.number_input("Thickness (mm)", min_value=0.0, value=1.0)

    st.subheader("Material")
    density = st.number_input("Steel density (kg/m³)", min_value=0.0, value=7850.0)

    if st.button("Calculate"):
        out = calculate_sheet(SheetInput(length_m=L, width_m=W, thickness_mm=t_mm, density_kgm3=density))

        st.subheader("Results")
        r = st.columns(3)
        r[0].metric("Area (m²)", f"{out.area_m2:.6f}")
        r[1].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        r[2].metric("Weight (kg)", f"{out.weight_kg:.3f}")
