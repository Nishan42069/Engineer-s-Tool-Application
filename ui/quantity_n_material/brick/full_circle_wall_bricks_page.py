import streamlit as st
from calculators.quantity_n_material.brick.full_circle_wall_bricks import (
    FullCircleWallInput,
    calculate_full_circle_wall_bricks,
)

# -------------------------
# GLOBAL UNIT CONFIG
# -------------------------
UNIT_CONFIG = {
    "Imperial (ft)": {"unit": "ft", "to_m": 0.3048, "vol_unit": "ft³"},
    "Imperial (in)": {"unit": "in", "to_m": 0.0254, "vol_unit": "ft³"},
    "Metric (m)":    {"unit": "m",  "to_m": 1.0,    "vol_unit": "m³"},
    "Metric (mm)":   {"unit": "mm", "to_m": 0.001,  "vol_unit": "m³"},
    "Metric (cm)":   {"unit": "cm", "to_m": 0.01,   "vol_unit": "m³"},
}


def render():
    st.header("Full Circular Wall Bricks Calculator")

    # -------------------------
    # UNIT SYSTEM (ONE PLACE)
    # -------------------------
    unit_choice = st.selectbox(
        "Unit system",
        list(UNIT_CONFIG.keys()),
    )

    cfg = UNIT_CONFIG[unit_choice]
    u = cfg["unit"]
    to_m = cfg["to_m"]
    volume_unit = cfg["vol_unit"]

    # -------------------------
    # WALL GEOMETRY
    # -------------------------
    st.subheader("Wall Geometry")

    g = st.columns(3)
    with g[0]:
        d = st.number_input(
            f"Inner diameter ({u})",
            min_value=0.0,
            value=10.0,
        )
    with g[1]:
        t = st.number_input(
            f"Wall thickness ({u})",
            min_value=0.0,
            value=0.5,
        )
    with g[2]:
        h = st.number_input(
            f"Wall height ({u})",
            min_value=0.0,
            value=10.0,
        )

    # -------------------------
    # WASTE & COST
    # -------------------------
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

    # -------------------------
    # CALCULATE
    # -------------------------
    if st.button("Calculate Full Circular Wall Bricks"):
        inp = FullCircleWallInput(
            inner_diameter_m=d * to_m,
            wall_thickness_m=t * to_m,
            wall_height_m=h * to_m,
            waste_percent=waste,
            brick_unit_cost=brick_cost,
            mortar_unit_cost=mortar_cost,
        )

        out = calculate_full_circle_wall_bricks(inp)

        mortar_qty = (
            out.mortar.quantity
            if volume_unit == "m³"
            else out.mortar.quantity / (0.3048 ** 3)
        )

        # -------------------------
        # RESULTS
        # -------------------------
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
