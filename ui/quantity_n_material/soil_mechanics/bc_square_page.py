import streamlit as st
from calculators.quantity_n_material.soil_mechanics.bc_square import (
    BearingCapacitySquareInput,
    calculate_bearing_capacity_square,
)


def render():
    st.header("Bearing Capacity – Square Footing")

    st.subheader("Soil & Footing Parameters")
    c1, c2, c3 = st.columns(3)
    with c1:
        cohesion = st.number_input("Cohesion c (kPa)", min_value=0.0, value=25.0)
    with c2:
        phi = st.number_input("Friction angle φ (deg)", min_value=0.0, max_value=45.0, value=30.0)
    with c3:
        gamma = st.number_input("Unit weight γ (kN/m³)", min_value=0.0, value=18.0)

    c4, c5, c6 = st.columns(3)
    with c4:
        B = st.number_input("Footing width B (m)", min_value=0.0, value=2.0)
    with c5:
        Df = st.number_input("Depth of foundation Df (m)", min_value=0.0, value=1.5)
    with c6:
        fs = st.number_input("Factor of safety", min_value=1.0, value=3.0)

    if st.button("Calculate bearing capacity (square)"):
        inp = BearingCapacitySquareInput(
            cohesion_kPa=cohesion,
            phi_deg=phi,
            unit_weight_kN_m3=gamma,
            footing_width_m=B,
            depth_foundation_m=Df,
            factor_of_safety=fs,
        )
        out = calculate_bearing_capacity_square(inp)

        st.subheader("Results")
        st.metric("Ultimate bearing capacity qult (kPa)", f"{out.q_ult_kPa:.1f}")
        st.success(f"Allowable bearing capacity qall (kPa): **{out.q_allow_kPa:.1f}**")
