import streamlit as st
from calculators.metal.steel_weights.beam_bar import BeamBarInput, calculate_beam_bar

def render():
    st.header("Beam Weight (I-Section)")

    st.subheader("Dimensions")
    cols = st.columns(5)
    with cols[0]:
        depth_mm = st.number_input("Depth h (mm)", min_value=0.0, value=200.0)
    with cols[1]:
        bf_mm = st.number_input("Flange width bf (mm)", min_value=0.0, value=100.0)
    with cols[2]:
        tf_mm = st.number_input("Flange thk tf (mm)", min_value=0.0, value=10.0)
    with cols[3]:
        tw_mm = st.number_input("Web thk tw (mm)", min_value=0.0, value=6.0)
    with cols[4]:
        length_m = st.number_input("Length (m)", min_value=0.0, value=6.0)

    st.subheader("Material")
    density = st.number_input("Steel density (kg/m³)", min_value=0.0, value=7850.0)

    if st.button("Calculate"):
        out = calculate_beam_bar(BeamBarInput(
            depth_mm=depth_mm, flange_width_mm=bf_mm, flange_thickness_mm=tf_mm,
            web_thickness_mm=tw_mm, length_m=length_m, density_kgm3=density
        ))

        st.subheader("Results")
        r = st.columns(3)
        r[0].metric("Area (m²)", f"{out.area_m2:.6f}")
        r[1].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        r[2].metric("Weight (kg)", f"{out.weight_kg:.3f}")
