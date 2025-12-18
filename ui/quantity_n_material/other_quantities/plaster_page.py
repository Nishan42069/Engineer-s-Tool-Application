import streamlit as st
from calculators.quantity_n_material.other_quantities.plaster import (
    PlasterInput,
    calculate_plaster,
)


def render():
    st.header("Plaster Quantity Calculator")

    st.subheader("Area & Thickness")
    c1, c2 = st.columns(2)
    with c1:
        area = st.number_input("Plaster area (m²)", min_value=0.0, value=50.0)
    with c2:
        t = st.number_input("Thickness (mm)", min_value=1.0, value=12.0)

    st.subheader("Mix Ratio (Cement : Sand)")
    c3, c4 = st.columns(2)
    with c3:
        c_part = st.number_input("Cement (part)", min_value=1, value=1)
    with c4:
        s_part = st.number_input("Sand (part)", min_value=1, value=4)

    if st.button("Calculate plaster quantities"):
        inp = PlasterInput(
            area_m2=area,
            thickness_mm=t,
            cement_part=c_part,
            sand_part=s_part,
        )
        out = calculate_plaster(inp)

        st.subheader("Results")
        st.write(f"Wet volume: **{out.wet_volume_m3:.3f} m³**")
        st.write(f"Dry volume (with wastage): **{out.dry_volume_m3:.3f} m³**")
        st.write(f"Cement: **{out.cement_bags:.2f} bags**")
        st.write(f"Sand: **{out.sand_volume_m3:.3f} m³**")
