# ui/rcc/round_column_rcc_page.py

import streamlit as st
from calculators.rcc.columns.column_design import RoundColumnInput, design_round_column


def render():
    st.header("Round RCC Column")

    c1, c2, c3 = st.columns(3)
    with c1:
        dia = st.number_input("Column diameter (mm)", min_value=0.0, value=300.0)
    with c2:
        n = st.number_input("Number of bars", min_value=3, value=6)
    with c3:
        bar_dia = st.number_input("Bar dia (mm)", min_value=8.0, value=16.0)

    c4, c5 = st.columns(2)
    with c4:
        fck = st.number_input("fck (MPa)", min_value=10.0, value=25.0)
    with c5:
        fy = st.number_input("fy (MPa)", min_value=250.0, value=415.0)

    if st.button("Design round column"):
        inp = RoundColumnInput(
            dia_mm=dia,
            n_bars=n,
            bar_dia_mm=bar_dia,
            fck_MPa=fck,
            fy_MPa=fy,
        )
        out = design_round_column(inp)

        st.subheader("Section & Steel")
        st.write(f"Gross area Ag: **{out.gross_area_mm2:.0f} mm²**")
        st.write(f"Steel area Asc: **{out.steel_area_mm2:.0f} mm²**")
        st.write(f"Concrete area Ac: **{out.concrete_area_mm2:.0f} mm²**")
        st.write(f"Steel ratio: **{out.steel_ratio_percent:.2f}%**")

        st.subheader("Axial Capacity")
        st.success(f"Approximate axial capacity Pu ≈ **{out.axial_capacity_kN:.0f} kN**")
