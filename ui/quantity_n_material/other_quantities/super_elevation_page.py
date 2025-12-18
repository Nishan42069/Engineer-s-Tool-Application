import streamlit as st
from calculators.quantity_n_material.other_quantities.super_elevation import (
    SuperElevationInput,
    calculate_super_elevation,
)


def render():
    st.header("Super Elevation Calculator")

    c1, c2, c3 = st.columns(3)
    with c1:
        V = st.number_input("Design speed V (km/h)", min_value=0.0, value=60.0)
    with c2:
        R = st.number_input("Curve radius R (m)", min_value=0.0, value=200.0)
    with c3:
        f = st.number_input("Side friction f", min_value=0.0, value=0.15)

    c4, _ = st.columns(2)
    with c4:
        e_max = st.number_input("Max super elevation e_max", min_value=0.0, value=0.07)

    if st.button("Calculate super elevation"):
        inp = SuperElevationInput(
            speed_kmph=V,
            radius_m=R,
            side_friction=f,
            max_super_elevation=e_max,
        )
        out = calculate_super_elevation(inp)

        st.subheader("Results")
        st.write(f"Required e (decimal): **{out.required_e:.4f}**")
        st.write(f"Required e (%): **{out.required_e*100:.2f}%**")
        st.write(f"Provided e (limited to e_max): **{out.limited_e*100:.2f}%**")
        if out.is_within_limit:
            st.success("Required super elevation is within allowable limit.")
        else:
            st.warning("Required super elevation exceeds maximum, speed or radius should be adjusted.")
