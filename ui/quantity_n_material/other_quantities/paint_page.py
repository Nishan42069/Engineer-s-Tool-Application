# ui/paint_page.py

import math
import streamlit as st
import pandas as pd  # keeping this for future use

from calculators.quantity_n_material.other_quantities.paint import PaintInput, calculate_paint
from pricing.paint_materials_db import get_paint_materials_table

def render():
    st.title("🎨 Painting Cost Estimator")

    st.write("We’ll use:")
    st.code(
        "Total paintable area = (Wall area [+ Ceiling area]) − Openings area\n"
        "Estimated Paint (L) = (Total paintable area × Coats) / Coverage (sq.ft/L/coat)",
        language="text",
    )

    # ----------------------------
    # Areas (Wall, Ceiling, Openings)
    # ----------------------------
    st.subheader("Areas (sq.ft)")
    wall_area = st.number_input("Wall area (sq.ft)", value=480.0)
    include_ceiling = st.checkbox("Include ceiling painting", value=True)
    ceiling_area = st.number_input("Ceiling area (sq.ft)", value=120.0) if include_ceiling else 0.0
    openings_area = st.number_input("Openings area (sq.ft)", value=37.0)

    # ----------------------------
    # Coverage & Coats
    # ----------------------------
    st.subheader("Coverage & Coats")
    coverage = st.number_input("Coverage (sq.ft per litre per coat)", value=90.0)
    coats = st.number_input("Number of coats", min_value=1, value=2)

    # ----------------------------
    # Labour & Margin
    # ----------------------------
    st.subheader("Labour & Margin")
    labour_rate = st.number_input("Labour cost per sq.ft (Rs.)", value=0.8)
    margin_percent = st.number_input("Margin (%)", value=10.0)

    # ----------------------------
    # Core Paint Calculation
    # ----------------------------
    inp = PaintInput(
        wall_area_sqft=wall_area,
        ceiling_area_sqft=ceiling_area,
        include_ceiling=include_ceiling,
        openings_area_sqft=openings_area,
        coverage_sqft_per_litre=coverage,
        coats=coats,
        labour_rate_sqft=labour_rate,
        margin_percent=margin_percent,
    )
    result = calculate_paint(inp)

    st.subheader("📏 Areas (sq.ft)")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total area", f"{result.total_area_sqft:,.2f}")
    c2.metric("Openings", f"{openings_area:,.2f}")
    c3.metric("Paintable area", f"{result.paintable_area_sqft:,.2f}")

    st.subheader("🧪 Paint Requirement")
    st.success(f"Estimated Paint Required: **{result.litres_needed:,.2f} L**")

    st.subheader("🧾 Labour Cost Summary")
    st.write(f"**Base Labour Cost:** Rs. {result.base_labour_cost:,.2f}")
    st.write(f"**Margin ({margin_percent}%):** Rs. {result.margin_amount:,.2f}")
    st.success(f"**Total Labour Cost:** Rs. {result.total_labour_cost:,.2f}")

    # ----------------------------
    # Material Pricing using DB
    # ----------------------------
    st.subheader("🎨 Paint Material Price (From Built-in Database)")

    df = get_paint_materials_table()

    # 1️⃣ Brand selection
    brand_options = sorted(df["brand_name"].unique())
    brand = st.selectbox("Brand", brand_options)

    # 2️⃣ Material name selection (filtered by brand)
    material_filter = df[df["brand_name"] == brand]
    material_name_options = sorted(material_filter["material_name"].unique())
    material_name = st.selectbox("Material Name", material_name_options)

    # 3️⃣ Type selection (filtered by brand + material_name)
    type_filter = material_filter[material_filter["material_name"] == material_name]
    type_options = sorted(type_filter["type"].unique())
    paint_type = st.selectbox("Type", type_options)

    # Filter final subset by brand + material_name + type
    subset = type_filter[type_filter["type"] == paint_type]

    if subset.empty:
        st.warning("No record found for this Brand + Material + Type.")
        return

    # ----------------------------
    # Unit / Pack size extraction from DB (automatically)
    # ----------------------------
    subset = subset.copy()
    subset["size_litre"] = (
        subset["unit"]
        .astype(str)
        .str.extract(r"(\d+(\.\d+)?)")[0]
        .astype(float)
    )

    # Allowed standard pack sizes
    allowed_sizes = [1, 5, 10, 20]

    # Show only allowed sizes that exist in database
    size_options = sorted(
        s for s in subset["size_litre"].unique().tolist() if s in allowed_sizes
    )

    if not size_options:
        st.warning("No standard pack sizes (1, 5, 10, 20 L) found for this item.")
        return

    # Pick pack size (user doesn't need to choose unit, automatically handled)
    selected_size = size_options[0]  # Select first available size automatically

    # Filter row by selected pack size (choose cheapest if multiple)
    size_rows = subset[subset["size_litre"] == selected_size].sort_values(
        "price_per_unit_npr"
    )
    row = size_rows.iloc[0]

    pack_size_litre = float(row["size_litre"])
    price_per_pack = float(row["price_per_unit_npr"])
    unit_label = str(row["unit"])

    # ----------------------------
    # Cost based on auto-calculated litres
    # ----------------------------
    litres_needed = max(result.litres_needed, 0.0)
    packs_needed = math.ceil(litres_needed / pack_size_litre) if pack_size_litre > 0 else 0
    material_cost_total = packs_needed * price_per_pack

    st.write(f"**Brand:** {brand}")
    st.write(f"**Material:** {material_name}")
    st.write(f"**Type:** {paint_type}")
    st.write(f"**Pack size:** {pack_size_litre:g} L ({unit_label})")
    st.write(f"**Price per pack:** Rs. {price_per_pack:,.2f}")
    st.write(f"**Approx packs needed:** {packs_needed}")
    st.success(f"**Material Cost:** Rs. {material_cost_total:,.2f}")

    # ----------------------------
    # Combined total
    # ----------------------------
    total_estimate = result.total_labour_cost + material_cost_total
    st.subheader("💰 Total Estimate (Labour + Material)")
    st.success(f"**Total (NPR): {total_estimate:,.2f}**")
