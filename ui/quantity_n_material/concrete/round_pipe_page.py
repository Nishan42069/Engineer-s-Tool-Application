# ui/concrete/round_pipe_page.py

import streamlit as st
from calculators.quantity_n_material.concrete.round_pipe import (
    RoundPipeInput,
    calculate_round_pipe_concrete,
)


def render():
    st.header("Round Pipe Concrete (Encasement)")

    # ---------------------------
    # Geometry
    # ---------------------------
    st.subheader("Geometry")

    g_cols = st.columns(3)
    with g_cols[0]:
        outer_diameter_ft = st.number_input(
            "Pipe outer diameter (ft)",
            min_value=0.0,
            value=2.0,
        )
    with g_cols[1]:
        concrete_thickness_ft = st.number_input(
            "Concrete encasement thickness (ft)",
            min_value=0.0,
            value=0.5,
        )
    with g_cols[2]:
        length_ft = st.number_input(
            "Pipe length (ft)",
            min_value=0.0,
            value=20.0,
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
    if st.button("Calculate pipe encasement concrete"):
        inp = RoundPipeInput(
            outer_diameter_ft=outer_diameter_ft,
            concrete_thickness_ft=concrete_thickness_ft,
            length_ft=length_ft,
            cement_part=cement_part,
            sand_part=sand_part,
            aggregate_part=aggregate_part,
            density_kgm3=density_kgm3,
            cost_per_m3=cost_per_m3,
        )
        out = calculate_round_pipe_concrete(inp)

        # ---------------------------
        # Results
        # ---------------------------
        st.subheader("Results")

        top_cols = st.columns(2)
        with top_cols[0]:
            st.metric("Concrete volume (m³)", f"{out.volume_m3:.3f}")
        with top_cols[1]:
            if out.total_cost > 0:
                st.metric("Estimated cost (Rs.)", f"{out.total_cost:,.2f}")
            else:
                st.metric("Estimated cost (Rs.)", "—")

        m_cols = st.columns(3)
        with m_cols[0]:
            st.metric("Cement weight (kg)", f"{out.cement_weight_kg:.1f}")
        with m_cols[1]:
            st.metric("Sand weight (kg)", f"{out.sand_weight_kg:.1f}")
        with m_cols[2]:
            st.metric("Aggregate weight (kg)", f"{out.aggregate_weight_kg:.1f}")
