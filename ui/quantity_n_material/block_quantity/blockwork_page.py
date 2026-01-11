import streamlit as st
from calculators.quantity_n_material.block_quantity.blockwork import (
    BlockworkInput,
    calculate_blockwork,
)

# --- unit config ---
UNIT_CONFIG = {
    "Imperial (ft)": {"unit": "ft", "to_m": 0.3048, "vol_unit": "ft³"},
    "Imperial (in)": {"unit": "in", "to_m": 0.0254, "vol_unit": "ft³"},
    "Metric (m)":    {"unit": "m",  "to_m": 1.0,    "vol_unit": "m³"},
    "Metric (mm)":   {"unit": "mm", "to_m": 0.001,  "vol_unit": "m³"},
    "Metric (cm)":   {"unit": "cm", "to_m": 0.01,   "vol_unit": "m³"},
}


def render():
    st.header("Blockwork Quantity Calculator")

    # -------------------------
    # GLOBAL UNIT SELECTOR
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
    # WALL DIMENSIONS
    # -------------------------
    st.subheader("Wall Dimensions")

    w = st.columns(3)
    with w[0]:
        L = st.number_input(f"Wall length ({u})", min_value=0.0, value=10.0)
    with w[1]:
        H = st.number_input(f"Wall height ({u})", min_value=0.0, value=10.0)
    with w[2]:
        T = st.number_input(f"Wall thickness ({u})", min_value=0.0, value=0.5)

    # -------------------------
    # BLOCK SIZE
    # -------------------------
    st.subheader("Block Size (including mortar joint)")

    b = st.columns(3)
    with b[0]:
        bL = st.number_input(f"Block length ({u})", min_value=0.0, value=400.0)
    with b[1]:
        bH = st.number_input(f"Block height ({u})", min_value=0.0, value=200.0)
    with b[2]:
        bT = st.number_input(f"Block thickness ({u})", min_value=0.0, value=200.0)

    # -------------------------
    # WASTE, MORTAR & COST
    # -------------------------
    st.subheader("Waste, Mortar & Cost")

    p = st.columns(4)
    with p[0]:
        waste = st.number_input("Waste (%)", min_value=0.0, value=5.0)
    with p[1]:
        mortar_ratio = st.number_input(
            "Mortar volume (% of wall volume)",
            min_value=0.0,
            value=25.0,
        )
    with p[2]:
        block_cost = st.number_input(
            "Block cost (Rs./block)",
            min_value=0.0,
            value=0.0,
        )
    with p[3]:
        mortar_cost = st.number_input(
            "Mortar cost (Rs./m³)",
            min_value=0.0,
            value=0.0,
        )

    # -------------------------
    # CALCULATE
    # -------------------------
    if st.button("Calculate blockwork"):
        inp = BlockworkInput(
            wall_length_m=L * to_m,
            wall_height_m=H * to_m,
            wall_thickness_m=T * to_m,
            block_length_m=bL * to_m,
            block_height_m=bH * to_m,
            block_thickness_m=bT * to_m,
            waste_percent=waste,
            mortar_ratio_percent=mortar_ratio,
            block_unit_cost=block_cost,
            mortar_unit_cost=mortar_cost,
        )

        out = calculate_blockwork(inp)

        mortar_qty = (
            out.mortar.quantity
            if volume_unit == "m³"
            else out.mortar.quantity / (0.3048 ** 3)
        )

        # -------------------------
        # RESULTS
        # -------------------------
        st.subheader("Results")

        r = st.columns(2)
        with r[0]:
            st.metric("Total blocks", f"{out.blocks.quantity:,.0f} nos")
        with r[1]:
            st.metric(
                f"Mortar volume ({volume_unit})",
                f"{mortar_qty:.3f}",
            )

        if out.total_cost > 0:
            st.success(f"Total cost: Rs. {out.total_cost:,.2f}")
