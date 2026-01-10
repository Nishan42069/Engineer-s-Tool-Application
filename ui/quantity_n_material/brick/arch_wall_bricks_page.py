import streamlit as st
from calculators.quantity_n_material.brick.arch_wall_bricks import (
    ArchWallBricksInput,
    calculate_arch_wall_bricks,
)

FT_TO_M = 0.3048
IN_TO_M = 0.0254


def render():
    st.header("Arch Wall Bricks Calculator")

    unit_system = st.selectbox(
        "Unit system",
        ["Imperial (ft / in)", "Metric (m / mm)"],
    )

    is_metric = unit_system.startswith("Metric")
    length_unit = "m" if is_metric else "ft"
    thickness_unit = "mm" if is_metric else "in"
    volume_unit = "m³" if is_metric else "ft³"

    st.subheader("Wall & Arch Geometry")

    c = st.columns(4)
    with c[0]:
        L = st.number_input(f"Wall length ({length_unit})", min_value=0.0)
    with c[1]:
        H = st.number_input(f"Wall height ({length_unit})", min_value=0.0)
    with c[2]:
        T = st.number_input(f"Wall thickness ({thickness_unit})", min_value=0.0)
    with c[3]:
        span = st.number_input(f"Arch span ({length_unit})", min_value=0.0)

    r = st.columns(2)
    with r[0]:
        rise = st.number_input(f"Arch rise ({length_unit})", min_value=0.0)
    with r[1]:
        waste = st.number_input("Waste (%)", min_value=0.0, value=5.0)

    st.subheader("Material Costs (optional)")

    cc = st.columns(2)
    with cc[0]:
        brick_cost = st.number_input("Brick cost (Rs./brick)", min_value=0.0)
    with cc[1]:
        mortar_cost = st.number_input("Mortar cost (Rs./m³)", min_value=0.0)

    if st.button("Calculate"):
        if is_metric:
            L_m, H_m, span_m, rise_m = L, H, span, rise
            T_m = T / 1000
        else:
            L_m = L * FT_TO_M
            H_m = H * FT_TO_M
            span_m = span * FT_TO_M
            rise_m = rise * FT_TO_M
            T_m = T * IN_TO_M

        inp = ArchWallBricksInput(
            wall_length_m=L_m,
            wall_height_m=H_m,
            wall_thickness_m=T_m,
            arch_span_m=span_m,
            arch_rise_m=rise_m,
            waste_percent=waste,
            brick_unit_cost=brick_cost,
            mortar_unit_cost=mortar_cost,
        )

        out = calculate_arch_wall_bricks(inp)

        mortar_qty = (
            out.mortar.quantity
            if is_metric
            else out.mortar.quantity / (FT_TO_M ** 3)
        )

        st.subheader("Results")

        st.metric("Bricks required", f"{out.bricks.quantity:,.0f} nos")

        st.metric(
            f"Mortar volume ({volume_unit})",
            f"{mortar_qty:.3f}",
        )

        if out.total_cost > 0:
            st.success(f"Total material cost: Rs. {out.total_cost:,.2f}")
