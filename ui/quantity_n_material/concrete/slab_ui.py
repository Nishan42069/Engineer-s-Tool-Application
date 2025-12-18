# ui/concrete/slab_concrete.py

import streamlit as st
from calculators.quantity_n_material.concrete.slab import (
    SlabInput,
    calculate_slab_concrete,
)


def render():
    st.header("Slab Concrete")

    # ---------------------------
    # Geometry
    # ---------------------------
    st.subheader("Geometry")

    g_cols = st.columns(2)
    with g_cols[0]:
        area_sqft = st.number_input(
            "Slab area (sq.ft)",
            min_value=0.0,
            value=100.0,
        )
    with g_cols[1]:
        thickness_ft = st.number_input(
            "Slab thickness (ft)",
            min_value=0.0,
            value=0.5,
        )

    # ---------------------------
    # Mix & Material Properties
    # ---------------------------
    st.subheader("Mix & Material Properties")

    # Mix ratio row (C : S : A)
    mix_cols = st.columns(3)
    with mix_cols[0]:
        cement_ratio = st.number_input(
            "Cement (part)",
            min_value=0,
            value=1,
        )
    with mix_cols[1]:
        sand_ratio = st.number_input(
            "Sand (part)",
            min_value=0,
            value=2,
        )
    with mix_cols[2]:
        aggregate_ratio = st.number_input(
            "Aggregate (part)",
            min_value=0,
            value=4,
        )

    # Density & cost row
    prop_cols = st.columns(2)
    with prop_cols[0]:
        density_kgm3 = st.number_input(
            "Concrete density (kg/m³)",
            min_value=1000.0,
            max_value=3000.0,
            value=2400.0,
        )
    with prop_cols[1]:
        cost_per_cubic_meter = st.number_input(
            "Concrete cost per m³ (Rs.)",
            min_value=0.0,
            value=5000.0,
        )

    # ---------------------------
    # Calculate
    # ---------------------------
    if st.button("Calculate slab concrete"):
        inp = SlabInput(
            area_sqft=area_sqft,
            thickness_ft=thickness_ft,
            cement_part=cement_ratio,
            sand_part=sand_ratio,
            aggregate_part=aggregate_ratio,
            density_kgm3=density_kgm3,
            cost_per_m3=cost_per_cubic_meter,
        )
        result = calculate_slab_concrete(inp)

        # ---------------------------
        # Results
        # ---------------------------
        st.subheader("Results")

        top_cols = st.columns(2)
        with top_cols[0]:
            st.metric("Slab volume (m³)", f"{result.volume_m3:.3f}")
        with top_cols[1]:
            st.metric("Total cost (Rs.)", f"{result.total_cost:,.2f}")

        m_cols = st.columns(3)
        with m_cols[0]:
            st.metric("Cement weight (kg)", f"{result.cement_weight_kg:.2f}")
        with m_cols[1]:
            st.metric("Sand weight (kg)", f"{result.sand_weight_kg:.2f}")
        with m_cols[2]:
            st.metric("Aggregate weight (kg)", f"{result.aggregate_weight_kg:.2f}")
