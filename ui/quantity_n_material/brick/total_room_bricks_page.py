import streamlit as st
from calculators.quantity_n_material.brick.total_room_bricks import (
    TotalRoomBricksInput,
    calculate_total_room_bricks,
)

FT_TO_M = 0.3048
IN_TO_M = 0.0254


def render():
    st.header("Total Room Brick Quantity Calculator")

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
    # ROOM GEOMETRY
    # -------------------------
    st.subheader("Room Dimensions")

    g = st.columns(4)
    with g[0]:
        L = st.number_input(
            f"Room length ({length_unit})",
            min_value=0.0,
            value=12.0,
        )
    with g[1]:
        B = st.number_input(
            f"Room width ({length_unit})",
            min_value=0.0,
            value=10.0,
        )
    with g[2]:
        H = st.number_input(
            f"Wall height ({length_unit})",
            min_value=0.0,
            value=10.0,
        )
    with g[3]:
        T = st.number_input(
            f"Wall thickness ({thickness_unit})",
            min_value=0.0,
            value=150.0 if is_metric else 6.0,
        )

    # -------------------------
    # WASTE & COST
    # -------------------------
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

    # -------------------------
    # CALCULATE
    # -------------------------
    if st.button("Calculate Room Bricks"):
        if is_metric:
            L_m = L
            B_m = B
            H_m = H
            T_m = T / 1000
        else:
            L_m = L * FT_TO_M
            B_m = B * FT_TO_M
            H_m = H * FT_TO_M
            T_m = T * IN_TO_M

        inp = TotalRoomBricksInput(
            room_length_m=L_m,
            room_width_m=B_m,
            wall_height_m=H_m,
            wall_thickness_m=T_m,
            waste_percent=waste,
            brick_unit_cost=brick_cost,
            mortar_unit_cost=mortar_cost,
        )

        out = calculate_total_room_bricks(inp)

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
import streamlit as st
from calculators.quantity_n_material.brick.total_room_bricks import (
    TotalRoomBricksInput,
    calculate_total_room_bricks,
)

FT_TO_M = 0.3048
IN_TO_M = 0.0254


def render():
    st.header("Total Room Brick Quantity Calculator")

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
    # ROOM GEOMETRY
    # -------------------------
    st.subheader("Room Dimensions")

    g = st.columns(4)
    with g[0]:
        L = st.number_input(
            f"Room length ({length_unit})",
            min_value=0.0,
            value=12.0,
        )
    with g[1]:
        B = st.number_input(
            f"Room width ({length_unit})",
            min_value=0.0,
            value=10.0,
        )
    with g[2]:
        H = st.number_input(
            f"Wall height ({length_unit})",
            min_value=0.0,
            value=10.0,
        )
    with g[3]:
        T = st.number_input(
            f"Wall thickness ({thickness_unit})",
            min_value=0.0,
            value=150.0 if is_metric else 6.0,
        )

    # -------------------------
    # WASTE & COST
    # -------------------------
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

    # -------------------------
    # CALCULATE
    # -------------------------
    if st.button("Calculate Room Bricks"):
        if is_metric:
            L_m = L
            B_m = B
            H_m = H
            T_m = T / 1000
        else:
            L_m = L * FT_TO_M
            B_m = B * FT_TO_M
            H_m = H * FT_TO_M
            T_m = T * IN_TO_M

        inp = TotalRoomBricksInput(
            room_length_m=L_m,
            room_width_m=B_m,
            wall_height_m=H_m,
            wall_thickness_m=T_m,
            waste_percent=waste,
            brick_unit_cost=brick_cost,
            mortar_unit_cost=mortar_cost,
        )

        out = calculate_total_room_bricks(inp)

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
