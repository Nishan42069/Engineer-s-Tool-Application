import streamlit as st
from calculators.quantity_n_material.other_quantities.floor_bricks import (
    FloorBrickInput,
    calculate_floor_bricks,
)


def render():
    st.header("Floor Bricks Calculator")

    st.subheader("Floor size")
    c1, c2 = st.columns(2)
    with c1:
        L = st.number_input("Floor length (m)", min_value=0.0, value=4.0)
    with c2:
        B = st.number_input("Floor width (m)", min_value=0.0, value=3.0)

    st.subheader("Brick size")
    c3, c4 = st.columns(2)
    with c3:
        bL = st.number_input("Brick length (m)", min_value=0.0, value=0.23)
    with c4:
        bB = st.number_input("Brick width (m)", min_value=0.0, value=0.115)

    wastage = st.number_input("Wastage (%)", min_value=0.0, value=10.0)

    if st.button("Calculate floor bricks"):
        inp = FloorBrickInput(
            floor_length_m=L,
            floor_width_m=B,
            brick_length_m=bL,
            brick_width_m=bB,
            wastage_percent=wastage,
        )
        out = calculate_floor_bricks(inp)

        st.subheader("Results")
        st.write(f"Floor area: **{out.floor_area_m2:.2f} m²**")
        st.write(f"Brick coverage area: **{out.brick_area_m2:.3f} m²**")
        st.write(f"Net bricks: **{out.bricks_net:.2f}**")
        st.success(f"Recommended bricks (with wastage): **{out.bricks_with_wastage} pcs**")
