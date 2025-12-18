import streamlit as st
from calculators.quantity_n_material.brick.total_room_bricks import (
    TotalRoomBricksInput,
    calculate_total_room_bricks,
)


def render():
    st.header("Total Room Bricks")

    # Geometry
    st.subheader("Room Dimensions")

    g_cols = st.columns(4)
    with g_cols[0]:
        L = st.number_input("Room length (ft)", min_value=0.0, value=12.0)
    with g_cols[1]:
        B = st.number_input("Room width (ft)", min_value=0.0, value=10.0)
    with g_cols[2]:
        H = st.number_input("Wall height (ft)", min_value=0.0, value=10.0)
    with g_cols[3]:
        T = st.number_input("Wall thickness (ft)", min_value=0.0, value=0.75)

    # Cost & extra
    st.subheader("Cost & Extra")

    c_cols = st.columns(2)
    with c_cols[0]:
        waste = st.number_input("Waste (%)", min_value=0.0, value=5.0)
    with c_cols[1]:
        cost = st.number_input("Brick cost (Rs./brick)", min_value=0.0, value=0.0)

    if st.button("Calculate room bricks"):
        inp = TotalRoomBricksInput(
            room_length_ft=L,
            room_width_ft=B,
            wall_height_ft=H,
            wall_thickness_ft=T,
            waste_percent=waste,
            brick_cost=cost,
        )
        out = calculate_total_room_bricks(inp)

        st.subheader("Results")
        r_cols = st.columns(2)
        with r_cols[0]:
            st.metric("Total bricks", f"{out.total_bricks:,.0f}")
        with r_cols[1]:
            st.metric("Mortar volume (m³)", f"{out.mortar_volume_m3:.3f}")

        if out.total_cost > 0:
            st.success(f"Total brick cost: Rs. {out.total_cost:,.2f}")
