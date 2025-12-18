# ui/concrete_page.py

import streamlit as st
from calculators.quantity_n_material.concrete.concrete_v import (
    ConcreteInput,
    calculate_concrete,
)

def render():
    st.header("Concrete by Volume")

    # ---------------------------
    # Mix & Volume (full-width row)
    # ---------------------------
    st.subheader("Mix & Volume")

    mix_cols = st.columns(4)  # 4 equal-width inputs
    with mix_cols[0]:
        vol = st.number_input(
            "Concrete volume (m³)",
            min_value=0.0,
            value=5.0,
        )
    with mix_cols[1]:
        cement = st.number_input(
            "Cement (parts)",
            min_value=1,
            value=1,
        )
    with mix_cols[2]:
        sand = st.number_input(
            "Sand (parts)",
            min_value=1,
            value=2,
        )
    with mix_cols[3]:
        agg = st.number_input(
            "Aggregate (parts)",
            min_value=1,
            value=4,
        )

    # ---------------------------
    # Factors (next full-width row)
    # ---------------------------
    st.subheader("Factors")

    factor_cols = st.columns(2)  # 2 equal-width inputs
    with factor_cols[0]:
        dry_factor = st.number_input(
            "Dry volume factor",
            value=1.54,
        )
    with factor_cols[1]:
        bag_weight = st.number_input(
            "Cement bag weight (kg)",
            value=50.0,
        )

    # ---------------------------
    # Action button
    # ---------------------------
    if st.button("Calculate"):
        inp = ConcreteInput(
            volume_m3=vol,
            cement=cement,
            sand=sand,
            aggregate=agg,
            dry_factor=dry_factor,
            cement_bag_weight=bag_weight,
        )
        out = calculate_concrete(inp)

        # ---------------------------
        # Results
        # ---------------------------
        st.subheader("Results")

        r_cols = st.columns(3)
        with r_cols[0]:
            st.metric("Dry volume (m³)", f"{out.dry_volume:.3f}")
            st.metric("Cement (bags)", f"{out.cement_bags:.2f}")
        with r_cols[1]:
            st.metric("Sand (m³)", f"{out.sand_m3:.3f}")
        with r_cols[2]:
            st.metric("Aggregate (m³)", f"{out.aggregate_m3:.3f}")
