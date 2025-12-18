# ui/rcc/one_way_slab_page.py

import streamlit as st
from calculators.rcc.slabs.slab_design import (
    SlabDesignInput,
    design_slab_flexure,
    one_way_slab_mu_kNm_per_m,
)


def render():
    st.header("One-Way Slab Design")

    st.subheader("Geometry & Loading")
    c1, c2, c3 = st.columns(3)
    with c1:
        L = st.number_input("Short span Lx (m)", min_value=0.0, value=3.5)
    with c2:
        w = st.number_input("Factored load w (kN/m²)", min_value=0.0, value=7.0)
    with c3:
        t = st.number_input("Slab thickness (mm)", min_value=0.0, value=130.0)

    st.subheader("Support condition (moment coefficient)")
    coeff_option = st.selectbox(
        "Select condition",
        ["Simply supported (~wL²/8)", "Continuous (~wL²/12)"],
    )
    coeff = 1/8 if "Simply" in coeff_option else 1/12

    st.subheader("Materials & Reinforcement")
    c4, c5, c6 = st.columns(3)
    with c4:
        fck = st.number_input("Concrete fck (MPa)", min_value=10.0, value=25.0)
    with c5:
        fy = st.number_input("Steel fy (MPa)", min_value=250.0, value=415.0)
    with c6:
        bar_dia = st.number_input("Main bar dia (mm)", min_value=6.0, value=10.0)

    cover = st.number_input("Effective cover (mm)", min_value=10.0, value=20.0)

    if st.button("Design one-way slab"):
        mu = one_way_slab_mu_kNm_per_m(span_m=L, w_kN_m2=w, coeff=coeff)

        inp = SlabDesignInput(
            mu_kNm_per_m=mu,
            thickness_mm=t,
            effective_cover_mm=cover,
            fck_MPa=fck,
            fy_MPa=fy,
            bar_dia_mm=bar_dia,
        )
        out = design_slab_flexure(inp)

        st.subheader("Results")
        st.write(f"Mu: **{out.mu_kNm_per_m:.2f} kNm/m** ({coeff_option})")
        st.write(f"Effective depth d: **{out.effective_depth_mm:.1f} mm**")
        st.write(f"Ast required: **{out.ast_required_mm2_per_m:.1f} mm²/m**")
        st.write(f"Ast min: **{out.ast_min_mm2_per_m:.1f} mm²/m**")
        st.success(f"Provide {bar_dia:.0f} mm @ **{out.spacing_mm:.0f} mm c/c** along short span")
