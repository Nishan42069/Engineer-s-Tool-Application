# ui/concrete/square_column_page.py

import streamlit as st
from calculators.quantity_n_material.concrete.square_column import (
    SquareColumnInput,
    calculate_square_column_concrete,
)


def render():
    st.header("Square / Rectangular Column Concrete")

    # --------------------------------
    # GEOMETRY
    # --------------------------------
    st.subheader("Geometry")

    g_cols = st.columns(3)
    with g_cols[0]:
        height_ft = st.number_input(
            "Column height (ft)",
            min_value=0.0,
            value=10.0
        )
    with g_cols[1]:
        width_ft = st.number_input(
            "Column width (ft)",
            min_value=0.0,
            value=1.0
        )
    with g_cols[2]:
        depth_ft = st.number_input(
            "Column depth (ft)",
            min_value=0.0,
            value=1.0
        )

    # --------------------------------
    # MIX & MATERIAL PROPERTIES
    # --------------------------------
    st.subheader("Mix & Material Properties")

    mix_cols = st.columns(3)
    with mix_cols[0]:
        cement_part = st.number_input("Cement (part)", min_value=1, value=1)
    with mix_cols[1]:
        sand_part = st.number_input("Sand (part)", min_value=1, value=2)
    with mix_cols[2]:
        aggregate_part = st.number_input("Aggregate (part)", min_value=1, value=4)

    prop_cols = st.columns(2)
    with prop_cols[0]:
        density_kgm3 = st.number_input(
            "Concrete density (kg/m³)",
            min_value=1000.0,
            max_value=3000.0,
            value=2400.0
        )
    with prop_cols[1]:
        cost_per_m3 = st.number_input(
            "Concrete cost per m³ (Rs.)",
            min_value=0.0,
            value=0.0
        )

    # --------------------------------
    # CALCULATE
    # --------------------------------
    if st.button("Calculate Column Concrete"):
        inp = SquareColumnInput(
            length_ft=height_ft,
            width_ft=width_ft,
            depth_ft=depth_ft,
            cement_part=cement_part,
            sand_part=sand_part,
            aggregate_part=aggregate_part,
            density_kgm3=density_kgm3,
            cost_per_m3=cost_per_m3,
        )

        out = calculate_square_column_concrete(inp)

        # --------------------------------
        # RESULTS
        # --------------------------------
        st.subheader("Results")

        top_cols = st.columns(2)
        with top_cols[0]:
            st.metric("Concrete volume (m³)", f"{out.volume_m3:.3f}")
        with top_cols[1]:
            st.metric("Estimated cost (Rs.)", f"{out.total_cost:,.2f}")

        m_cols = st.columns(3)
        with m_cols[0]:
            st.metric("Cement weight (kg)", f"{out.cement_weight_kg:.1f}")
        with m_cols[1]:
            st.metric("Sand weight (kg)", f"{out.sand_weight_kg:.1f}")
        with m_cols[2]:
            st.metric("Aggregate weight (kg)", f"{out.aggregate_weight_kg:.1f}")
