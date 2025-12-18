import streamlit as st
from calculators.quantity_n_material.other_quantities.bed_volume import (
    BedVolumeInput,
    calculate_bed_volume,
)


def render():
    st.header("Bed Filling Volume")

    c1, c2, c3 = st.columns(3)
    with c1:
        L = st.number_input("Length (m)", min_value=0.0, value=5.0)
    with c2:
        B = st.number_input("Width (m)", min_value=0.0, value=1.5)
    with c3:
        D = st.number_input("Fill depth (m)", min_value=0.0, value=0.5)

    gamma = st.number_input(
        "Bulk density (kN/m³) (optional, for weight)", min_value=0.0, value=0.0
    )

    if st.button("Calculate filling volume"):
        inp = BedVolumeInput(
            length_m=L,
            width_m=B,
            depth_m=D,
            bulk_density_kN_m3=gamma,
        )
        out = calculate_bed_volume(inp)

        st.subheader("Results")
        st.write(f"Fill volume: **{out.volume_m3:.3f} m³**")
        if out.weight_kN > 0:
            st.write(f"Approximate weight: **{out.weight_kN:.2f} kN**")
