# ui/concrete/circle_tank_page.py

import streamlit as st
from calculators.quantity_n_material.concrete.circle_tank import (
    CircleTankInput,
    calculate_circle_tank_concrete,
)


def render():
    st.header("Circle Tank Concrete")

    # ---------------------------
    # Geometry
    # ---------------------------
    st.subheader("Geometry")

    g_cols = st.columns(4)
    with g_cols[0]:
        inner_diameter_ft = st.number_input(
            "Inner diameter (ft)",
            min_value=0.0,
            value=10.0,
        )
    with g_cols[1]:
        wall_thickness_ft = st.number_input(
            "Wall thickness (ft)",
            min_value=0.0,
            value=0.5,
        )
    with g_cols[2]:
        wall_height_ft = st.number_input(
            "Wall height (ft)",
            min_value=0.0,
            value=8.0,
        )
    with g_cols[3]:
        base_thickness_ft = st.number_input(
            "Base slab thickness (ft)",
            min_value=0.0,
            value=0.5,
        )

    # ---------------------------
    # Mix & Material Properties
    # ---------------------------
    st.subheader("Mix & Material Properties")

    # Mix ratio (C : S : A)
    mix_cols = st.columns(3)
    with mix_cols[0]:
        cement_part = st.number_input(
            "Cement (part)",
            min_value=1,
            value=1,
        )
    with mix_cols[1]:
        sand_part = st.number_input(
            "Sand (part)",
            min_value=1,
            value=2,
        )
    with mix_cols[2]:
        aggregate_part = st.number_input(
            "Aggregate (part)",
            min_value=1,
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
        cost_per_m3 = st.number_input(
            "Concrete cost per m³ (Rs.)",
            min_value=0.0,
            value=0.0,
        )

    # ---------------------------
    # Action
    # ---------------------------
    if st.button("Calculate Circle Tank Concrete"):
        inp = CircleTankInput(
            inner_diameter_ft=inner_diameter_ft,
            wall_thickness_ft=wall_thickness_ft,
            wall_height_ft=wall_height_ft,
            base_thickness_ft=base_thickness_ft,
            cement_part=cement_part,
            sand_part=sand_part,
            aggregate_part=aggregate_part,
            density_kgm3=density_kgm3,
            cost_per_m3=cost_per_m3,
        )
        out = calculate_circle_tank_concrete(inp)

        # ---------------------------
        # Results
        # ---------------------------
        st.subheader("Results")

        v_cols = st.columns(3)
        with v_cols[0]:
            st.metric("Wall volume (m³)", f"{out.wall_volume_m3:.3f}")
        with v_cols[1]:
            st.metric("Base slab volume (m³)", f"{out.base_volume_m3:.3f}")
        with v_cols[2]:
            st.metric("Total concrete volume (m³)", f"{out.total_volume_m3:.3f}")

        m_cols = st.columns(3)
        with m_cols[0]:
            st.metric("Cement weight (kg)", f"{out.cement_weight_kg:.1f}")
        with m_cols[1]:
            st.metric("Sand weight (kg)", f"{out.sand_weight_kg:.1f}")
        with m_cols[2]:
            st.metric("Aggregate weight (kg)", f"{out.aggregate_weight_kg:.1f}")

        if out.total_cost > 0:
            st.success(f"Estimated concrete cost: Rs. {out.total_cost:,.2f}")
