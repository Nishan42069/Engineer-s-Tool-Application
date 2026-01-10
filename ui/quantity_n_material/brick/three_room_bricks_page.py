import streamlit as st
from calculators.quantity_n_material.brick.three_room_bricks import (
    ThreeRoomBricksInput,
    calculate_three_room_bricks,
)

FT_TO_M = 0.3048
IN_TO_M = 0.0254


def render():
    st.header("Three-Room Brick Quantity Calculator")

    # ---- UNIT SYSTEM ----
    unit_system = st.selectbox(
        "Unit system",
        ["Imperial (ft / in)", "Metric (m / mm)"],
    )

    is_metric = unit_system.startswith("Metric")

    length_unit = "m" if is_metric else "ft"
    thickness_unit = "mm" if is_metric else "in"
    volume_unit = "m³" if is_metric else "ft³"

    # -------------------------
    # ROOM DIMENSIONS
    # -------------------------
    st.subheader("Room Dimensions")

    r1 = st.columns(2)
    with r1[0]:
        L1 = st.number_input(f"Room 1 length ({length_unit})", min_value=0.0, value=12.0)
    with r1[1]:
        B1 = st.number_input(f"Room 1 width ({length_unit})", min_value=0.0, value=10.0)

    r2 = st.columns(2)
    with r2[0]:
        L2 = st.number_input(f"Room 2 length ({length_unit})", min_value=0.0, value=10.0)
    with r2[1]:
        B2 = st.number_input(f"Room 2 width ({length_unit})", min_value=0.0, value=10.0)

    r3 = st.columns(2)
    with r3[0]:
        L3 = st.number_input(f"Room 3 length ({length_unit})", min_value=0.0, value=10.0)
    with r3[1]:
        B3 = st.number_input(f"Room 3 width ({length_unit})", min_value=0.0, value=10.0)

    # -------------------------
    # WALL & COST PARAMETERS
    # -------------------------
    st.subheader("Wall & Material Parameters")

    w = st.columns(4)
    with w[0]:
        H = st.number_input(f"Wall height ({length_unit})", min_value=0.0, value=10.0)
    with w[1]:
        T = st.number_input(
            f"Wall thickness ({thickness_unit})",
            min_value=0.0,
            value=150.0 if is_metric else 6.0,
        )
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
        if is_metric:
            L1_m, B1_m = L1, B1
            L2_m, B2_m = L2, B2
            L3_m, B3_m = L3, B3
            H_m = H
            T_m = T / 1000
        else:
            L1_m, B1_m = L1 * FT_TO_M, B1 * FT_TO_M
            L2_m, B2_m = L2 * FT_TO_M, B2 * FT_TO_M
            L3_m, B3_m = L3 * FT_TO_M, B3 * FT_TO_M
            H_m = H * FT_TO_M
            T_m = T * IN_TO_M

        inp = ThreeRoomBricksInput(
            room1_length_m=L1_m,
            room1_width_m=B1_m,
            room2_length_m=L2_m,
            room2_width_m=B2_m,
            room3_length_m=L3_m,
            room3_width_m=B3_m,
            wall_height_m=H_m,
            wall_thickness_m=T_m,
            waste_percent=waste,
            brick_unit_cost=brick_cost,
            mortar_unit_cost=mortar_cost,
        )

        out = calculate_three_room_bricks(inp)

        mortar_qty = (
            out.mortar.quantity
            if is_metric
            else out.mortar.quantity / (FT_TO_M ** 3)
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
