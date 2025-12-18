# ui/concrete/retaining_wall_page.py

import streamlit as st
from calculators.quantity_n_material.concrete.retaining_wall import (
    RetainingWallInput,
    calculate_retaining_wall_concrete,
)


def render():
    st.header("Retaining Wall Concrete")

    # ---------------------------
    # Geometry
    # ---------------------------
    st.subheader("Geometry")

    g_cols = st.columns(5)
    with g_cols[0]:
        wall_length_ft = st.number_input(
            "Wall length (ft)",
            min_value=0.0,
            value=20.0,
        )
    with g_cols[1]:
        stem_thickness_ft = st.number_input(
            "Stem thickness (ft)",
            min_value=0.0,
            value=0.75,
        )
    with g_cols[2]:
        stem_height_ft = st.number_input(
            "Stem height (ft)",
            min_value=0.0,
            value=8.0,
        )
    with g_cols[3]:
        base_width_ft = st.number_input(
            "Base slab width (ft)",
            min_value=0.0,
            value=6.0,
        )
    with g_cols[4]:
        base_thickness_ft = st.number_input(
            "Base slab thickness (ft)",
            min_value=0.0,
            value=0.75,
        )

    # ---------------------------
    # Mix & Material Properties
    # ---------------------------
    st.subheader("Mix & Material Properties")

    # Mix ratio row (C : S : A)
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
    if st.button("Calculate retaining wall concrete"):
        inp = RetainingWallInput(
            wall_length_ft=wall_length_ft,
            stem_thickness_ft=stem_thickness_ft,
            stem_height_ft=stem_height_ft,
            base_width_ft=base_width_ft,
            base_thickness_ft=base_thickness_ft,
            cement_part=cement_part,
            sand_part=sand_part,
            aggregate_part=aggregate_part,
            density_kgm3=density_kgm3,
            cost_per_m3=cost_per_m3,
        )
        out = calculate_retaining_wall_concrete(inp)

        # ---------------------------
        # Results
        # ---------------------------
        st.subheader("Results")

        top_cols = st.columns(3)
        with top_cols[0]:
            st.metric("Stem volume (m³)", f"{out.stem_volume_m3:.3f}")
        with top_cols[1]:
            st.metric("Base volume (m³)", f"{out.base_volume_m3:.3f}")
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
