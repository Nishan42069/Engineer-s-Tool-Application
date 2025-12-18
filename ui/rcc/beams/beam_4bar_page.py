# ui/rcc/beam_4bar_page.py

import streamlit as st
from calculators.rcc.beams.beam_flexure import BeamDesignInput, design_beam_flexure


def render():
    st.header("4-Bar Beam Design (Flexure)")

    st.subheader("Section & Moment")
    c1, c2, c3 = st.columns(3)
    with c1:
        b = st.number_input("Beam width b (mm)", min_value=0.0, value=230.0)
    with c2:
        d = st.number_input("Effective depth d (mm)", min_value=0.0, value=450.0)
    with c3:
        Mu = st.number_input("Factored moment Mu (kNm)", min_value=0.0, value=100.0)

    st.subheader("Materials & Steel")
    c4, c5, c6 = st.columns(3)
    with c4:
        fck = st.number_input("fck (MPa)", min_value=10.0, value=25.0)
    with c5:
        fy = st.number_input("fy (MPa)", min_value=250.0, value=415.0)
    with c6:
        bar_dia = st.number_input("Main bar dia (mm)", min_value=8.0, value=20.0)

    n_bars = st.number_input("Number of bars", min_value=1, value=4)

    if st.button("Check 4-bar beam"):
        inp = BeamDesignInput(
            mu_kNm=Mu,
            b_mm=b,
            d_mm=d,
            fck_MPa=fck,
            fy_MPa=fy,
            n_bars=n_bars,
            bar_dia_mm=bar_dia,
        )
        out = design_beam_flexure(inp)

        st.subheader("Results")
        st.write(f"Ast required (incl. min): **{out.ast_required_mm2:.0f} mm²**")
        st.write(f"Ast provided: **{out.ast_provided_mm2:.0f} mm²**")
        st.write(f"Beam capacity Mu,cap: **{out.mu_capacity_kNm:.1f} kNm**")
        st.write(f"Utilization: **{out.utilization*100:.1f}%**")
        if out.utilization <= 1.0:
            st.success("OK: Provided reinforcement is adequate for given Mu.")
        else:
            st.error("NOT OK: Increase bar size/number or beam depth/width.")
