import streamlit as st
from calculators.quantity_n_material.brick.three_room_bricks import (
    ThreeRoomBricksInput,
    calculate_three_room_bricks,
)


def render():
    st.header("Three Room Bricks")

    st.subheader("Room 1 Dimensions")
    r1_cols = st.columns(2)
    with r1_cols[0]:
        L1 = st.number_input("Room 1 length (ft)", min_value=0.0, value=12.0)
    with r1_cols[1]:
        B1 = st.number_input("Room 1 width (ft)", min_value=0.0, value=10.0)

    st.subheader("Room 2 Dimensions")
    r2_cols = st.columns(2)
    with r2_cols[0]:
        L2 = st.number_input("Room 2 length (ft)", min_value=0.0, value=10.0)
    with r2_cols[1]:
        B2 = st.number_input("Room 2 width (ft)", min_value=0.0, value=10.0)

    st.subheader("Room 3 Dimensions")
    r3_cols = st.columns(2)
    with r3_cols[0]:
        L3 = st.number_input("Room 3 length (ft)", min_value=0.0, value=10.0)
    with r3_cols[1]:
        B3 = st.number_input("Room 3 width (ft)", min_value=0.0, value=10.0)

    st.subheader("Wall & Cost Parameters")
    w_cols = st.columns(3)
    with w_cols[0]:
        H = st.number_input("Wall height (ft)", min_value=0.0, value=10.0)
    with w_cols[1]:
        T = st.number_input("Wall thickness (ft)", min_value=0.0, value=0.75)
    with w_cols[2]:
        waste = st.number_input("Waste (%)", min_value=0.0, value=5.0)

    cost = st.number_input("Brick cost (Rs./brick)", min_value=0.0, value=0.0)

    if st.button("Calculate three room bricks"):
        inp = ThreeRoomBricksInput(
            room1_length_ft=L1,
            room1_width_ft=B1,
            room2_length_ft=L2,
            room2_width_ft=B2,
            room3_length_ft=L3,
            room3_width_ft=B3,
            wall_height_ft=H,
            wall_thickness_ft=T,
            waste_percent=waste,
            brick_cost=cost,
        )
        out = calculate_three_room_bricks(inp)

        st.subheader("Results")
        r_cols = st.columns(2)
        with r_cols[0]:
            st.metric("Total bricks", f"{out.total_bricks:,.0f}")
        with r_cols[1]:
            st.metric("Mortar volume (m³)", f"{out.mortar_m3:.3f}")

        if out.total_cost > 0:
            st.success(f"Total brick cost: Rs. {out.total_cost:,.2f}")
