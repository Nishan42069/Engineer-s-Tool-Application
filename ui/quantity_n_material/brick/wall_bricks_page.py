# ui/brick/wall_bricks_page.py

import streamlit as st
from calculators.quantity_n_material.brick.wall_bricks import (
    WallBricksInput,
    calculate_wall_bricks,
)

FT_TO_M = 0.3048
IN_TO_M = 0.0254


def render():
    st.header("Wall Bricks Calculator")

    # ---- UNIT SYSTEM ----
    unit_system = st.selectbox(
        "Unit system",
        ["Imperial (ft / in)", "Metric (m / mm)"],
    )

    is_metric = unit_system.startswith("Metric")

    length_unit = "m" if is_metric else "ft"
    thickness_unit = "mm" if is_metric else "in"
    volume_unit = "m³" if is_metric else "ft³"

    # --------------------------------
    # GEOMETRY INPUTS
    # --------------------------------
    st.subheader("Wall Dimensions")

    g = st.columns(3)
    with g[0]:
        L = st.number_input(
            f"Length ({length_unit})",
            min_value=0.0,
            value=10.0,
        )
    with g[1]:
        H = st.number_input(
            f"Height ({length_unit})",
            min_value=0.0,
            value=10.0,
        )
    with g[2]:
        T = st.number_input(
            f"Thickness ({thickness_unit})",
            min_value=0.0,
            value=150.0 if is_metric else 6.0,
        )

    # --------------------------------
    # COST & PARAMETERS
    # --------------------------------
    st.subheader("Waste & Material Costs (optional)")

    c = st.columns(3)
    with c[0]:
        waste = st.number_input(
            "Waste (%)",
            min_value=0.0,
            value=5.0,
        )
    with c[1]:
        brick_cost = st.number_input(
            "Brick cost (Rs./brick)",
            min_value=0.0,
            value=0.0,
        )
    with c[2]:
        mortar_cost = st.number_input(
            "Mortar cost (Rs./m³)",
            min_value=0.0,
            value=0.0,
        )

    # --------------------------------
    # CALCULATE
    # --------------------------------
    if st.button("Calculate Wall Bricks"):
        if is_metric:
            L_m = L
            H_m = H
            T_m = T / 1000
        else:
            L_m = L * FT_TO_M
            H_m = H * FT_TO_M
            T_m = T * IN_TO_M

        inp = WallBricksInput(
            length_m=L_m,
            height_m=H_m,
            thickness_m=T_m,
            waste_percent=waste,
            brick_unit_cost=brick_cost,
            mortar_unit_cost=mortar_cost,
        )

        out = calculate_wall_bricks(inp)

        mortar_qty = (
            out.mortar.quantity
            if is_metric
            else out.mortar.quantity / (FT_TO_M ** 3)
        )

        # --------------------------------
        # RESULTS
        # --------------------------------
        st.subheader("Results")

        r1, r2 = st.columns(2)
        with r1:
            st.metric(
                "Bricks required",
                f"{out.bricks.quantity:,.0f} nos",
            )
        with r2:
            st.metric(
                f"Mortar volume ({volume_unit})",
                f"{mortar_qty:.3f}",
            )

        if out.total_cost > 0:
            st.success(
                f"Total material cost: Rs. {out.total_cost:,.2f}"
            )
