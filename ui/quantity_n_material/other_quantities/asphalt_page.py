import streamlit as st
from calculators.quantity_n_material.other_quantities.asphalt import (
    AsphaltInput,
    calculate_asphalt,
)


def render():
    st.header("Asphalt Quantity Calculator")

    c1, c2, c3 = st.columns(3)
    with c1:
        L = st.number_input("Length (m)", min_value=0.0, value=100.0)
    with c2:
        B = st.number_input("Width (m)", min_value=0.0, value=7.0)
    with c3:
        t = st.number_input("Thickness (mm)", min_value=0.0, value=50.0)

    density = st.number_input(
        "Density (t/m³)", min_value=0.0, value=2.35
    )

    if st.button("Calculate asphalt quantity"):
        inp = AsphaltInput(
            length_m=L,
            width_m=B,
            thickness_mm=t,
            density_t_m3=density,
        )
        out = calculate_asphalt(inp)

        st.subheader("Results")
        st.write(f"Asphalt volume: **{out.volume_m3:.3f} m³**")
        st.success(f"Asphalt tonnage: **{out.tonnage_t:.2f} t**")
