# ui/brick/wall_bricks_page.py

import streamlit as st
from calculators.quantity_n_material.brick.wall_bricks import (
    WallBricksInput,
    calculate_wall_bricks
)


def render():
    st.header("Wall Bricks Calculator")

    # --------------------------------
    # GEOMETRY INPUTS
    # --------------------------------
    st.subheader("Wall Dimensions")

    g_cols = st.columns(3)
    with g_cols[0]:
        L = st.number_input("Length (ft)", min_value=0.0, value=10.0)
    with g_cols[1]:
        H = st.number_input("Height (ft)", min_value=0.0, value=10.0)
    with g_cols[2]:
        T = st.number_input("Thickness (ft)", min_value=0.0, value=0.75)

    # --------------------------------
    # COST & PARAMETERS
    # --------------------------------
    st.subheader("Cost & Additional Inputs")

    p_cols = st.columns(2)
    with p_cols[0]:
        waste = st.number_input("Waste (%)", min_value=0.0, value=5.0)
    with p_cols[1]:
        brick_cost = st.number_input("Brick Cost (Rs.)", min_value=0.0, value=0.0)

    # --------------------------------
    # CALCULATE
    # --------------------------------
    if st.button("Calculate Wall Bricks"):
        inp = WallBricksInput(
            wall_length_ft=L,
            wall_height_ft=H,
            wall_thickness_ft=T,
            waste_percent=waste,
            brick_cost=brick_cost,
        )

        out = calculate_wall_bricks(inp)

        # --------------------------------
        # RESULTS
        # --------------------------------
        st.subheader("Results")

        r_cols = st.columns(2)
        with r_cols[0]:
            st.metric("Bricks Needed", f"{out.bricks:,.0f}")
        with r_cols[1]:
            st.metric("Mortar Volume (m³)", f"{out.mortar_m3:.3f}")

        if out.total_cost > 0:
            st.success(f"Total Cost: Rs. {out.total_cost:,.2f}")
