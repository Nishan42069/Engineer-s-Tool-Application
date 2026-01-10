import streamlit as st
from calculators.quantity_n_material.brick.brick_wall_support import (
    BrickWallSupportInput,
    calculate_brick_wall_support,
)

FT_TO_M = 0.3048
IN_TO_M = 0.0254


def render():
    st.header("Brick Wall Support Calculator")

    # ---- UNIT SYSTEM ----
    unit_system = st.selectbox(
        "Unit system",
        ["Imperial (ft / in)", "Metric (m / mm)"],
    )

    is_metric = unit_system.startswith("Metric")

    length_unit = "m" if is_metric else "ft"
    projection_unit = length_unit
    height_unit = length_unit
    volume_unit = "m³" if is_metric else "ft³"

    st.subheader("Support Geometry")

    g = st.columns(4)
    with g[0]:
        w = st.number_input(
            f"Support width along wall ({length_unit})",
            min_value=0.0,
            value=2.0,
        )
    with g[1]:
        p = st.number_input(
            f"Projection from wall ({projection_unit})",
            min_value=0.0,
            value=1.0,
        )
    with g[2]:
        h = st.number_input(
            f"Support height ({height_unit})",
            min_value=0.0,
            value=6.0,
        )
    with g[3]:
        n = st.number_input(
            "Number of supports",
            min_value=0,
            value=3,
            step=1,
        )

    st.subheader("Waste & Material Costs (optional)")

    c = st.columns(3)
    with c[0]:
        waste = st.number_input("Waste (%)", min_value=0.0, value=5.0)
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

    if st.button("Calculate"):
        # ---- CONVERT TO METERS ----
        if is_metric:
            w_m = w
            p_m = p
            h_m = h
        else:
            w_m = w * FT_TO_M
            p_m = p * FT_TO_M
            h_m = h * FT_TO_M

        inp = BrickWallSupportInput(
            support_width_m=w_m,
            support_projection_m=p_m,
            support_height_m=h_m,
            number_of_supports=n,
            waste_percent=waste,
            brick_unit_cost=brick_cost,
            mortar_unit_cost=mortar_cost,
        )

        out = calculate_brick_wall_support(inp)

        mortar_qty = (
            out.mortar.quantity
            if is_metric
            else out.mortar.quantity / (FT_TO_M ** 3)
        )

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
