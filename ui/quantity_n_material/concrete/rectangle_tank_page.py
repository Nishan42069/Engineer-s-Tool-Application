# ui/concrete/rectangle_tank_page.py

import streamlit as st
from calculators.quantity_n_material.concrete.rectangle_tank import (
    RectangleTankInput,
    calculate_rectangle_tank_concrete,
)


def render():
    st.header("Rectangle Tank Concrete")

    # ---------------------------
    # Geometry
    # ---------------------------
    st.subheader("Geometry")

    g_cols = st.columns(5)
    with g_cols[0]:
        length_ft = st.number_input(
            "Inner length (ft)",
            min_value=0.0,
            value=10.0,
        )
    with g_cols[1]:
        width_ft = st.number_input(
            "Inner width (ft)",
            min_value=0.0,
            value=8.0,
        )
    with g_cols[2]:
        inner_height_ft = st.number_input(
            "Inner water height (ft)",
            min_value=0.0,
            value=8.0,
        )
    with g_cols[3]:
        wall_thickness_ft = st.number_input(
            "Wall thickness (ft)",
            min_value=0.0,
            value=0.5,
        )
    with g_cols[4]:
        base_thickness_ft = st.number_input(
            "Base slab thickness (ft)",
            min_value=0.0,
            value=0.5,
        )

    # ---------------------------
    # Mix & Material Properties
    # ---------------------------
    st.subheader("Mix & Material Properties")

    # Mix ratio row
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
    if st.button("Calculate rectangle tank concrete"):
        inp = RectangleTankInput(
            length_ft=length_ft,
            width_ft=width_ft,
            inner_height_ft=inner_height_ft,
            wall_thickness_ft=wall_thickness_ft,
            base_thickness_ft=base_thickness_ft,
            cement_part=cement_part,
            sand_part=sand_part,
            aggregate_part=aggregate_part,
            density_kgm3=density_kgm3,
            cost_per_m3=cost_per_m3,
        )
        out = calculate_rectangle_tank_concrete(inp)

        # ---------------------------
        # Results
        # ---------------------------
        st.subheader("Results")

        top_cols = st.columns(3)
        with top_cols[0]:
            st.metric("Wall volume (m³)", f"{out.wall_volume_m3:.3f}")
        with top_cols[1]:
            st.metric("Base slab volume (m³)", f"{out.base_volume_m3:.3f}")
        with top_cols[2]:
            st.metric("Total volume (m³)", f"{out.total_volume_m3:.3f}")

        m_cols = st.columns(3)
        with m_cols[0]:
            st.metric("Cement weight (kg)", f"{out.cement_weight_kg:.1f}")
        with m_cols[1]:
            st.metric("Sand weight (kg)", f"{out.sand_weight_kg:.1f}")
        with m_cols[2]:
            st.metric("Aggregate weight (kg)", f"{out.aggregate_weight_kg:.1f}")

        if out.total_cost > 0:
            st.success(f"Estimated concrete cost: Rs. {out.total_cost:,.2f}")
