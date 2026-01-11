import streamlit as st
from calculators.quantity_n_material.concrete.round_column import (
    RoundColumnInput,
    calculate_round_column_concrete,
)

# -------------------------
# UNIT TABLES
# -------------------------
UNIT_TO_M = {
    "Imperial (ft)": 0.3048,
    "Imperial (in)": 0.0254,
    "Metric (m)": 1.0,
    "Metric (cm)": 0.01,
    "Metric (mm)": 0.001,
}

VOLUME_FROM_M3 = {
    "Imperial (ft)": 35.3147,
    "Imperial (in)": 61023.7,
    "Metric (m)": 1.0,
    "Metric (cm)": 1_000_000.0,
    "Metric (mm)": 1_000_000_000.0,
}


def render():
    st.header("Round Column Concrete Calculator")

    # -------------------------
    # UNIT SYSTEM
    # -------------------------
    unit_system = st.selectbox(
        "Unit system",
        [
            "Imperial (ft)",
            "Imperial (in)",
            "Metric (m)",
            "Metric (cm)",
            "Metric (mm)",
        ],
    )

    unit_label = unit_system.split("(")[1].replace(")", "")
    to_m = UNIT_TO_M[unit_system]
    from_m3 = VOLUME_FROM_M3[unit_system]

    # -------------------------
    # GEOMETRY
    # -------------------------
    st.subheader("Column Geometry")

    g = st.columns(2)
    with g[0]:
        diameter = st.number_input(
            f"Column diameter ({unit_label})",
            min_value=0.0,
            value=1.0,
        )
    with g[1]:
        height = st.number_input(
            f"Column height ({unit_label})",
            min_value=0.0,
            value=10.0,
        )

    # -------------------------
    # MIX & MATERIAL PROPERTIES
    # -------------------------
    st.subheader("Concrete Mix & Properties")

    mix = st.columns(3)
    with mix[0]:
        cement = st.number_input("Cement (part)", min_value=1, value=1)
    with mix[1]:
        sand = st.number_input("Sand (part)", min_value=1, value=2)
    with mix[2]:
        aggregate = st.number_input("Aggregate (part)", min_value=1, value=4)

    props = st.columns(2)
    with props[0]:
        density = st.number_input(
            "Concrete density (kg/m³)",
            min_value=1000.0,
            max_value=3000.0,
            value=2400.0,
        )
    with props[1]:
        cost = st.number_input(
            "Concrete cost (Rs./m³)",
            min_value=0.0,
            value=0.0,
        )

    # -------------------------
    # CALCULATE
    # -------------------------
    if st.button("Calculate Round Column Concrete"):
        inp = RoundColumnInput(
            diameter_m=diameter * to_m,
            height_m=height * to_m,
            cement_part=cement,
            sand_part=sand,
            aggregate_part=aggregate,
            density_kgm3=density,
            cost_per_m3=cost,
        )

        out = calculate_round_column_concrete(inp)

        volume_disp = out.volume_m3 * from_m3

        # -------------------------
        # RESULTS
        # -------------------------
        st.subheader("Results")

        st.metric(
            f"Concrete volume ({unit_label}³)",
            f"{volume_disp:.3f}",
        )

        m = st.columns(3)
        with m[0]:
            st.metric("Cement weight (kg)", f"{out.cement_weight_kg:.1f}")
        with m[1]:
            st.metric("Sand weight (kg)", f"{out.sand_weight_kg:.1f}")
        with m[2]:
            st.metric("Aggregate weight (kg)", f"{out.aggregate_weight_kg:.1f}")

        if out.total_cost > 0:
            st.success(f"Estimated concrete cost: Rs. {out.total_cost:,.2f}")
