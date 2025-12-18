# ui/brick/circle_wall_bricks_page.py

import streamlit as st
from calculators.quantity_n_material.brick.circle_wall_bricks import (
    CircleWallInput,
    calculate_circle_wall_bricks,
)


def render():
    st.header("Circular Wall Bricks Calculator")

    # -------------------------
    # GEOMETRY INPUTS
    # -------------------------
    st.subheader("Circular Wall Dimensions")

    g_cols = st.columns(3)
    with g_cols[0]:
        D = st.number_input("Diameter (ft)", min_value=0.0, value=10.0)
    with g_cols[1]:
        H = st.number_input("Height (ft)", min_value=0.0, value=10.0)
    with g_cols[2]:
        T = st.number_input("Wall Thickness (ft)", min_value=0.0, value=0.75)

    # -------------------------
    # COST & ADDITIONAL INPUTS
    # -------------------------
    st.subheader("Cost & Preferences")

    c_cols = st.columns(2)
    with c_cols[0]:
        waste = st.number_input("Waste (%)", min_value=0.0, value=5.0)
    with c_cols[1]:
        cost = st.number_input("Brick Cost (Rs.)", min_value=0.0, value=0.0)

    # -------------------------
    # CALCULATE
    # -------------------------
    if st.button("Calculate Circular Wall Bricks"):
        inp = CircleWallInput(
            diameter_ft=D,
            height_ft=H,
            thickness_ft=T,
            waste_percent=waste,
            brick_cost=cost,
        )

        out = calculate_circle_wall_bricks(inp)

        # -------------------------
        # RESULTS
        # -------------------------
        st.subheader("Results")

        r_cols = st.columns(2)
        with r_cols[0]:
            st.metric("Bricks Needed", f"{out.bricks:,.0f}")
        with r_cols[1]:
            st.metric("Mortar Volume (m³)", f"{out.mortar_m3:.3f}")

        if out.total_cost > 0:
            st.success(f"Total Cost: Rs. {out.total_cost:,.2f}")
