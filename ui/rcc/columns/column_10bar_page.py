# ui/rcc/column_4bar_page.py

import streamlit as st
from calculators.rcc.columns.column_design import RectColumnInput, design_rect_column


def render():
    st.header("10-Bar Rectangular Column")

    c1, c2, c3 = st.columns(3)
    with c1:
        b = st.number_input("Column width b (mm)", min_value=0.0, value=230.0)
    with c2:
        D = st.number_input("Column depth D (mm)", min_value=0.0, value=300.0)
    with c3:
        n = st.number_input("Number of bars", min_value=1, value=10)

    c4, c5, c6 = st.columns(3)
    with c4:
        bar_dia = st.number_input("Bar dia (mm)", min_value=8.0, value=16.0)
    with c5:
        fck = st.number_input("fck (MPa)", min_value=10.0, value=25.0)
    with c6:
        fy = st.number_input("fy (MPa)", min_value=250.0, value=415.0)

    if st.button("Design 4-bar column"):
        inp = RectColumnInput(
            b_mm=b,
            D_mm=D,
            n_bars=n,
            bar_dia_mm=bar_dia,
            fck_MPa=fck,
            fy_MPa=fy,
        )
        out = design_rect_column(inp)

        st.subheader("Section & Steel")
        st.write(f"Gross area Ag: **{out.gross_area_mm2:.0f} mm²**")
        st.write(f"Steel area Asc: **{out.steel_area_mm2:.0f} mm²**")
        st.write(f"Concrete area Ac: **{out.concrete_area_mm2:.0f} mm²**")
        st.write(f"Steel ratio: **{out.steel_ratio_percent:.2f}%**")

        st.subheader("Axial Capacity (Short, Tied)")
        st.success(f"Approximate axial capacity Pu ≈ **{out.axial_capacity_kN:.0f} kN**")
