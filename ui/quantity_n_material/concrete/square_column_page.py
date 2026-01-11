import streamlit as st
from calculators.quantity_n_material.concrete.square_column import (
    SquareColumnInput,
    calculate_square_column_concrete,
)

# -------------------------
# UNIT CONVERSION TABLES
# -------------------------
LENGTH_TO_M = {
    "Imperial (ft)": 0.3048,
    "Imperial (in)": 0.0254,
    "Metric (m)": 1.0,
    "Metric (cm)": 0.01,
    "Metric (mm)": 0.001,
}

VOLUME_FROM_M3 = {
    "Metric (m³)": 1.0,
    "Imperial (ft³)": 35.3147,
}


def render():
    st.header("Square / Rectangular Column Concrete")

    # -------------------------
    # UNIT SYSTEM
    # -------------------------
    length_unit = st.selectbox(
        "Length unit",
        list(LENGTH_TO_M.keys()),
    )

    volume_unit = st.selectbox(
        "Result volume unit",
        list(VOLUME_FROM_M3.keys()),
    )

    # -------------------------
    # GEOMETRY
    # -------------------------
    st.subheader("Column Geometry")

    g = st.columns(3)
    with g[0]:
        height = st.number_input(
            f"Column height ({length_unit.split('(')[1].replace(')', '')})",
            min_value=0.0,
            value=3.0,
        )
    with g[1]:
        width = st.number_input(
            f"Column width ({length_unit.split('(')[1].replace(')', '')})",
            min_value=0.0,
            value=0.3,
        )
    with g[2]:
        depth = st.number_input(
            f"Column depth ({length_unit.split('(')[1].replace(')', '')})",
            min_value=0.0,
            value=0.3,
        )

    # -------------------------
    # MIX & MATERIAL
    # -------------------------
    st.subheader("Concrete Mix")

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
    if st.button("Calculate Column Concrete"):
        factor = LENGTH_TO_M[length_unit]

        inp = SquareColumnInput(
            height_m=height * factor,
            width_m=width * factor,
            depth_m=depth * factor,
            cement_part=cement,
            sand_part=sand,
            aggregate_part=aggregate,
            density_kgm3=density,
            cost_per_m3=cost,
        )

        out = calculate_square_column_concrete(inp)

        volume_display = out.volume_m3 * VOLUME_FROM_M3[volume_unit]

        # -------------------------
        # RESULTS
        # -------------------------
        st.subheader("Results")

        st.metric(
            f"Concrete volume ({volume_unit.split('(')[1].replace(')', '')})",
            f"{volume_display:.3f}",
        )

        r = st.columns(3)
        with r[0]:
            st.metric("Cement weight (kg)", f"{out.cement_weight_kg:.1f}")
        with r[1]:
            st.metric("Sand weight (kg)", f"{out.sand_weight_kg:.1f}")
        with r[2]:
            st.metric("Aggregate weight (kg)", f"{out.aggregate_weight_kg:.1f}")

        if out.total_cost > 0:
            st.success(f"Estimated cost: Rs. {out.total_cost:,.2f}")
