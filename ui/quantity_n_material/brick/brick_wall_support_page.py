import streamlit as st
from calculators.quantity_n_material.brick.brick_wall_support import (
    BrickWallSupportInput,
    calculate_brick_wall_support,
)


def render():
    st.header("Brick Wall Support")

    st.subheader("Support Geometry")

    g_cols = st.columns(4)
    with g_cols[0]:
        w = st.number_input("Support width along wall (ft)", min_value=0.0, value=2.0)
    with g_cols[1]:
        p = st.number_input("Projection from wall (ft)", min_value=0.0, value=1.0)
    with g_cols[2]:
        h = st.number_input("Support height (ft)", min_value=0.0, value=6.0)
    with g_cols[3]:
        n = st.number_input("Number of supports", min_value=0, value=3)

    st.subheader("Cost & Waste")
    c_cols = st.columns(2)
    with c_cols[0]:
        waste = st.number_input("Waste (%)", min_value=0.0, value=5.0)
    with c_cols[1]:
        cost = st.number_input("Brick cost (Rs./brick)", min_value=0.0, value=0.0)

    if st.button("Calculate support bricks"):
        inp = BrickWallSupportInput(
            support_width_ft=w,
            support_projection_ft=p,
            support_height_ft=h,
            number_of_supports=n,
            waste_percent=waste,
            brick_cost=cost,
        )
        out = calculate_brick_wall_support(inp)

        st.subheader("Results")
        r_cols = st.columns(2)
        with r_cols[0]:
            st.metric("Bricks needed", f"{out.bricks:,.0f}")
        with r_cols[1]:
            st.metric("Mortar volume (m³)", f"{out.mortar_m3:.3f}")

        if out.total_cost > 0:
            st.success(f"Total brick cost: Rs. {out.total_cost:,.2f}")
