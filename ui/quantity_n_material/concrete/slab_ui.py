import streamlit as st
from calculators.quantity_n_material.concrete.slab import (
    SlabInput,
    calculate_slab_concrete,
)

# -------------------------
# UNIT TABLES
# -------------------------
AREA_TO_M2 = {
    "Imperial (sq ft)": 0.092903,
    "Imperial (sq in)": 0.00064516,
    "Metric (m²)": 1.0,
    "Metric (cm²)": 0.0001,
}

LENGTH_TO_M = {
    "Imperial (ft)": 0.3048,
    "Imperial (in)": 0.0254,
    "Metric (m)": 1.0,
    "Metric (cm)": 0.01,
    "Metric (mm)": 0.001,
}

VOLUME_FROM_M3 = {
    "Imperial (ft³)": 35.3147,
    "Metric (m³)": 1.0,
}


def render():
    st.header("Slab Concrete Calculator")

    # -------------------------
    # UNIT SYSTEM
    # -------------------------
    area_unit = st.selectbox(
        "Area unit",
        list(AREA_TO_M2.keys()),
    )

    thickness_unit = st.selectbox(
        "Thickness unit",
        list(LENGTH_TO_M.keys()),
    )

    volume_unit = st.selectbox(
        "Result volume unit",
        list(VOLUME_FROM_M3.keys()),
    )

    # -------------------------
    # GEOMETRY
    # -------------------------
    st.subheader("Slab Geometry")

    g = st.columns(2)
    with g[0]:
        area = st.number_input(
            f"Slab area ({area_unit.split('(')[1].replace(')', '')})",
            min_value=0.0,
            value=100.0,
        )
    with g[1]:
        thickness = st.number_input(
            f"Slab thickness ({thickness_unit.split('(')[1].replace(')', '')})",
            min_value=0.0,
            value=0.15,
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
    if st.button("Calculate Slab Concrete"):
        area_m2 = area * AREA_TO_M2[area_unit]
        thickness_m = thickness * LENGTH_TO_M[thickness_unit]

        inp = SlabInput(
            area_m2=area_m2,
            thickness_m=thickness_m,
            cement_part=cement,
            sand_part=sand,
            aggregate_part=aggregate,
            density_kgm3=density,
            cost_per_m3=cost,
        )

        out = calculate_slab_concrete(inp)

        volume_display = out.volume_m3 * VOLUME_FROM_M3[volume_unit]

        # -------------------------
        # RESULTS
        # -------------------------
        st.subheader("Results")

        st.metric(
            f"Concrete volume ({volume_unit.split('(')[1].replace(')', '')})",
            f"{volume_display:.3f}",
        )

        m = st.columns(3)
        with m[0]:
            st.metric("Cement weight (kg)", f"{out.cement_weight_kg:.1f}")
        with m[1]:
            st.metric("Sand weight (kg)", f"{out.sand_weight_kg:.1f}")
        with m[2]:
            st.metric("Aggregate weight (kg)", f"{out.aggregate_weight_kg:.1f}")

        if out.total_cost > 0:
            st.success(f"Estimated cost: Rs. {out.total_cost:,.2f}")
