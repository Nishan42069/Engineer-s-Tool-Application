import streamlit as st
from calculators.metal.steel_weights.channel import ChannelInput, calculate_channel

def render():
    st.header("Channel Weight (C-Section)")

    st.subheader("Dimensions")
    cols = st.columns(4)
    with cols[0]:
        depth_mm = st.number_input("Depth h (mm)", min_value=0.0, value=200.0)
    with cols[1]:
        flange_mm = st.number_input("Flange width b (mm)", min_value=0.0, value=75.0)
    with cols[2]:
        t_mm = st.number_input("Thickness t (mm)", min_value=0.0, value=8.0)
    with cols[3]:
        length_m = st.number_input("Length (m)", min_value=0.0, value=6.0)

    st.subheader("Material")
    density = st.number_input("Steel density (kg/m³)", min_value=0.0, value=7850.0)

    if st.button("Calculate"):
        out = calculate_channel(ChannelInput(depth_mm=depth_mm, flange_width_mm=flange_mm, thickness_mm=t_mm, length_m=length_m, density_kgm3=density))

        st.subheader("Results")
        r = st.columns(3)
        r[0].metric("Area (m²)", f"{out.area_m2:.6f}")
        r[1].metric("Volume (m³)", f"{out.volume_m3:.6f}")
        r[2].metric("Weight (kg)", f"{out.weight_kg:.3f}")
