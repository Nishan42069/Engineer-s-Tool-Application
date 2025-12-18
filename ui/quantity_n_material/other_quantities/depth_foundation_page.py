import streamlit as st
from calculators.quantity_n_material.other_quantities.depth_foundation import (
    DepthFoundationInput,
    calculate_depth_foundation,
)


def render():
    st.header("Approximate Safe Depth of Foundation")

    c1, c2, c3 = st.columns(3)
    with c1:
        qall = st.number_input("Allowable bearing capacity qall (kPa)", min_value=0.0, value=150.0)
    with c2:
        gamma = st.number_input("Soil unit weight γ (kN/m³)", min_value=0.0, value=18.0)
    with c3:
        fs = st.number_input("Factor of safety", min_value=1.0, value=1.0)

    if st.button("Estimate depth"):
        inp = DepthFoundationInput(
            allowable_bearing_kPa=qall,
            unit_weight_kN_m3=gamma,
            factor_of_safety=fs,
        )
        out = calculate_depth_foundation(inp)

        st.subheader("Result")
        st.success(f"Estimated minimum depth: **{out.depth_m:.2f} m**")
        st.caption("This is a rough check only. Final depth must follow detailed design and local codes.")
