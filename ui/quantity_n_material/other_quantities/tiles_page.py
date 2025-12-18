import streamlit as st
from calculators.quantity_n_material.other_quantities.tiles import (
    TileInput,
    calculate_tiles,
)


def render():
    st.header("Tile Quantity Calculator")

    st.subheader("Room size")
    c1, c2 = st.columns(2)
    with c1:
        L = st.number_input("Room length (m)", min_value=0.0, value=4.0)
    with c2:
        B = st.number_input("Room width (m)", min_value=0.0, value=3.0)

    st.subheader("Tile size")
    c3, c4 = st.columns(2)
    with c3:
        tL = st.number_input("Tile length (m)", min_value=0.0, value=0.6)
    with c4:
        tB = st.number_input("Tile width (m)", min_value=0.0, value=0.6)

    wastage = st.number_input("Wastage (%)", min_value=0.0, value=10.0)

    if st.button("Calculate tiles"):
        inp = TileInput(
            room_length_m=L,
            room_width_m=B,
            tile_length_m=tL,
            tile_width_m=tB,
            wastage_percent=wastage,
        )
        out = calculate_tiles(inp)

        st.subheader("Results")
        st.write(f"Room area: **{out.room_area_m2:.2f} m²**")
        st.write(f"Tile area: **{out.tile_area_m2:.3f} m²**")
        st.write(f"Net tiles (no wastage): **{out.tiles_net:.2f}**")
        st.success(f"Recommended tiles (with wastage): **{out.tiles_with_wastage} pcs**")
