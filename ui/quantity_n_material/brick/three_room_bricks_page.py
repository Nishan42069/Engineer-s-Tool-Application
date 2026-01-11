import streamlit as st
from calculators.quantity_n_material.brick.three_room_bricks import (
    ThreeRoomBricksInput,
    calculate_three_room_bricks,
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
    st.header("Three-Room Brick Quantity Calculator")

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
    # ROOM DIMENSIONS
    # -------------------------
    st.subheader("Room Dimensions")

    r1 = st.columns(2)
    with r1[0]:
        L1 = st.number_input(f"Room 1 length ({u})", min_value=0.0, value=12.0)
    with r1[1]:
        B1 = st.number_input(f"Room 1 width ({u})", min_value=0.0, value=10.0)

    r2 = st.columns(2)
    with r2[0]:
        L2 = st.number_input(f"Room 2 length ({u})", min_value=0.0, value=10.0)
    with r2[1]:
        B2 = st.number_input(f"Room 2 width ({u})", min_value=0.0, value=10.0)

    r3 = st.columns(2)
    with r3[0]:
        L3 = st.number_input(f"Room 3 length ({u})", min_value=0.0, value=10.0)
    with r3[1]:
        B3 = st.number_input(f"Room 3 width ({u})", min_value=0.0, value=10.0)

    # -------------------------
    # WALL & COST PARAMETERS
    # -------------------------
    st.subheader("Wall & Material Parameters")

    w = st.columns(4)
    with w[0]:
        H = st.number_input(f"Wall height ({u})", min_value=0.0, value=10.0)
    with w[1]:
        T = st.number_input(f"Wall thickness ({u})", min_value=0.0, value=0.5)
    with w[2]:
        waste = st.number_input("Waste (%)", min_value=0.0, value=5.0)
    with w[3]:
        brick_cost = st.number_input(
            "Brick cost (Rs./brick)",
            min_value=0.0,
            value=0.0,
        )

    mortar_cost = st.number_input(
        "Mortar cost (Rs./m³)",
        min_value=0.0,
        value=0.0,
    )

    # -------------------------
    # CALCULATE
    # -------------------------
    if st.button("Calculate Bricks for Three Rooms"):
        inp = ThreeRoomBricksInput(
            room1_length_m=L1 * to_m,
            room1_width_m=B1 * to_m,
            room2_length_m=L2 * to_m,
            room2_width_m=B2 * to_m,
            room3_length_m=L3 * to_m,
            room3_width_m=B3 * to_m,
            wall_height_m=H * to_m,
            wall_thickness_m=T * to_m,
            waste_percent=waste,
            brick_unit_cost=brick_cost,
            mortar_unit_cost=mortar_cost,
        )

        out = calculate_three_room_bricks(inp)

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
                "Total bricks required",
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
