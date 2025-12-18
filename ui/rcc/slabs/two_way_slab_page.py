# ui/rcc/two_way_slab_page.py

import streamlit as st
from calculators.rcc.slabs.slab_design import (
    SlabDesignInput,
    design_slab_flexure,
    TwoWaySlabInput,
    two_way_slab_moments,
)


def render():
    st.header("Two-Way Slab Design (Coefficient Method)")

    st.subheader("Geometry & Loading")
    c1, c2, c3 = st.columns(3)
    with c1:
        lx = st.number_input("Short span Lx (m)", min_value=0.0, value=4.0)
    with c2:
        ly = st.number_input("Long span Ly (m)", min_value=0.0, value=5.0)
    with c3:
        w = st.number_input("Factored load w (kN/m²)", min_value=0.0, value=7.0)

    st.subheader("Moment Coefficients αx, αy")
    st.caption("Typical simply supported two-way slab ~ αx=0.047, αy=0.036 (IS456 tables).")
    c4, c5 = st.columns(2)
    with c4:
        alpha_x = st.number_input("αx", min_value=0.0, value=0.047)
    with c5:
        alpha_y = st.number_input("αy", min_value=0.0, value=0.036)

    st.subheader("Thickness & Materials")
    c6, c7, c8 = st.columns(3)
    with c6:
        t = st.number_input("Slab thickness (mm)", min_value=0.0, value=140.0)
    with c7:
        fck = st.number_input("Concrete fck (MPa)", min_value=10.0, value=25.0)
    with c8:
        fy = st.number_input("Steel fy (MPa)", min_value=250.0, value=415.0)

    cover = st.number_input("Effective cover (mm)", min_value=10.0, value=20.0)
    bar_dia_x = st.number_input("Main bar dia in short span (mm)", min_value=6.0, value=10.0)
    bar_dia_y = st.number_input("Main bar dia in long span (mm)", min_value=6.0, value=8.0)

    if st.button("Design two-way slab"):
        m_in = TwoWaySlabInput(
            lx_m=lx,
            ly_m=ly,
            w_kN_m2=w,
            alpha_x=alpha_x,
            alpha_y=alpha_y,
        )
        m_out = two_way_slab_moments(m_in)

        inp_x = SlabDesignInput(
            mu_kNm_per_m=m_out.mu_x_kNm_per_m,
            thickness_mm=t,
            effective_cover_mm=cover,
            fck_MPa=fck,
            fy_MPa=fy,
            bar_dia_mm=bar_dia_x,
        )
        out_x = design_slab_flexure(inp_x)

        inp_y = SlabDesignInput(
            mu_kNm_per_m=m_out.mu_y_kNm_per_m,
            thickness_mm=t,
            effective_cover_mm=cover,
            fck_MPa=fck,
            fy_MPa=fy,
            bar_dia_mm=bar_dia_y,
        )
        out_y = design_slab_flexure(inp_y)

        st.subheader("Moments")
        st.write(f"Mu,x (short span): **{m_out.mu_x_kNm_per_m:.2f} kNm/m**")
        st.write(f"Mu,y (long span): **{m_out.mu_y_kNm_per_m:.2f} kNm/m**")

        st.subheader("Steel – Short Span (X-direction)")
        st.write(f"Ast req: **{out_x.ast_required_mm2_per_m:.1f} mm²/m**")
        st.write(f"Ast min: **{out_x.ast_min_mm2_per_m:.1f} mm²/m**")
        st.success(f"Provide {bar_dia_x:.0f} mm @ **{out_x.spacing_mm:.0f} mm c/c**")

        st.subheader("Steel – Long Span (Y-direction)")
        st.write(f"Ast req: **{out_y.ast_required_mm2_per_m:.1f} mm²/m**")
        st.write(f"Ast min: **{out_y.ast_min_mm2_per_m:.1f} mm²/m**")
        st.success(f"Provide {bar_dia_y:.0f} mm @ **{out_y.spacing_mm:.0f} mm c/c**")
