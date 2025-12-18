import streamlit as st
from calculators.quantity_n_material.block_quantity.blockwork import (
    BlockworkInput,
    calculate_blockwork,
)


def render():
    st.header("Blockwork Quantity Calculator")

    # --- Wall geometry ---
    st.subheader("Wall Dimensions")

    g_cols = st.columns(3)
    with g_cols[0]:
        L = st.number_input("Wall length (ft)", min_value=0.0, value=10.0)
    with g_cols[1]:
        H = st.number_input("Wall height (ft)", min_value=0.0, value=10.0)
    with g_cols[2]:
        T = st.number_input("Wall thickness (ft)", min_value=0.0, value=0.5)

    # --- Block size ---
    st.subheader("Block Size (including mortar joint)")

    b_cols = st.columns(3)
    with b_cols[0]:
        bL = st.number_input("Block length (mm)", min_value=0.0, value=400.0)
    with b_cols[1]:
        bH = st.number_input("Block height (mm)", min_value=0.0, value=200.0)
    with b_cols[2]:
        bT = st.number_input("Block thickness (mm)", min_value=0.0, value=200.0)

    # --- Waste, mortar, cost ---
    st.subheader("Waste, Mortar & Cost")

    p_cols = st.columns(3)
    with p_cols[0]:
        waste = st.number_input("Waste (%)", min_value=0.0, value=5.0)
    with p_cols[1]:
        mortar_ratio = st.number_input(
            "Mortar volume (% of wall volume)", min_value=0.0, value=25.0
        )
    with p_cols[2]:
        cost = st.number_input("Block cost (Rs./block)", min_value=0.0, value=0.0)

    if st.button("Calculate blockwork"):
        try:
            inp = BlockworkInput(
                wall_length_ft=L,
                wall_height_ft=H,
                wall_thickness_ft=T,
                block_length_mm=bL,
                block_height_mm=bH,
                block_thickness_mm=bT,
                waste_percent=waste,
                mortar_ratio_percent=mortar_ratio,
                block_cost=cost,
            )
            out = calculate_blockwork(inp)

            st.subheader("Results")

            r_cols = st.columns(2)
            with r_cols[0]:
                st.metric("Total blocks", f"{out.total_blocks:,.0f}")
            with r_cols[1]:
                st.metric("Mortar volume (m³)", f"{out.mortar_volume_m3:.3f}")

            if out.total_cost > 0:
                st.success(f"Total block cost: Rs. {out.total_cost:,.2f}")

        except ValueError as e:
            st.error(str(e))
