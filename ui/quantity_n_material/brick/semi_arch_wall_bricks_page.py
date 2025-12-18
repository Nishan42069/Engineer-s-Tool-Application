import streamlit as st
from calculators.quantity_n_material.brick.semi_arch_wall_bricks import (
    SemiArchWallBricksInput,
    calculate_semi_arch_wall_bricks,
)


def render():
    st.header("Semi Arch Wall Bricks")

    st.subheader("Wall & Semi-Arch Geometry")

    g_cols = st.columns(4)
    with g_cols[0]:
        L = st.number_input("Wall length (ft)", min_value=0.0, value=10.0)
    with g_cols[1]:
        H = st.number_input("Wall height (ft)", min_value=0.0, value=10.0)
    with g_cols[2]:
        T = st.number_input("Wall thickness (ft)", min_value=0.0, value=0.75)
    with g_cols[3]:
        span = st.number_input("Semi-arch span (ft)", min_value=0.0, value=4.0)

    arch_cols = st.columns(2)
    with arch_cols[0]:
        rise = st.number_input("Semi-arch rise (ft)", min_value=0.0, value=1.5)
    with arch_cols[1]:
        waste = st.number_input("Waste (%)", min_value=0.0, value=5.0)

    cost = st.number_input("Brick cost (Rs./brick)", min_value=0.0, value=0.0)

    if st.button("Calculate semi arch wall bricks"):
        inp = SemiArchWallBricksInput(
            wall_length_ft=L,
            wall_height_ft=H,
            wall_thickness_ft=T,
            arch_span_ft=span,
            arch_rise_ft=rise,
            waste_percent=waste,
            brick_cost=cost,
        )
        out = calculate_semi_arch_wall_bricks(inp)

        st.subheader("Results")
        r_cols = st.columns(2)
        with r_cols[0]:
            st.metric("Bricks needed", f"{out.bricks:,.0f}")
        with r_cols[1]:
            st.metric("Mortar volume (m³)", f"{out.mortar_m3:.3f}")

        if out.total_cost > 0:
            st.success(f"Total brick cost: Rs. {out.total_cost:,.2f}")
