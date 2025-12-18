import streamlit as st
from calculators.quantity_n_material.brick.full_circle_wall_bricks import (
    FullCircleWallInput,
    calculate_full_circle_wall_bricks,
)


def render():
    st.header("Full Circle Wall Bricks")

    st.subheader("Wall Geometry")

    g_cols = st.columns(3)
    with g_cols[0]:
        d = st.number_input("Inner diameter (ft)", min_value=0.0, value=10.0)
    with g_cols[1]:
        t = st.number_input("Wall thickness (ft)", min_value=0.0, value=0.75)
    with g_cols[2]:
        h = st.number_input("Wall height (ft)", min_value=0.0, value=10.0)

    c_cols = st.columns(2)
    with c_cols[0]:
        waste = st.number_input("Waste (%)", min_value=0.0, value=5.0)
    with c_cols[1]:
        cost = st.number_input("Brick cost (Rs./brick)", min_value=0.0, value=0.0)

    if st.button("Calculate full circle wall bricks"):
        inp = FullCircleWallInput(
            inner_diameter_ft=d,
            wall_thickness_ft=t,
            wall_height_ft=h,
            waste_percent=waste,
            brick_cost=cost,
        )
        out = calculate_full_circle_wall_bricks(inp)

        st.subheader("Results")
        r_cols = st.columns(2)
        with r_cols[0]:
            st.metric("Bricks needed", f"{out.bricks:,.0f}")
        with r_cols[1]:
            st.metric("Mortar volume (m³)", f"{out.mortar_m3:.3f}")

        if out.total_cost > 0:
            st.success(f"Total brick cost: Rs. {out.total_cost:,.2f}")
