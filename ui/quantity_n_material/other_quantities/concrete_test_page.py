import streamlit as st
from calculators.quantity_n_material.other_quantities.concrete_test import (
    ConcreteCubeTestInput,
    calculate_concrete_cube_test,
)


def render():
    st.header("Concrete Cube Test")

    c1, c2, c3 = st.columns(3)
    with c1:
        load = st.number_input("Failure load (kN)", min_value=0.0, value=750.0)
    with c2:
        size = st.number_input("Cube size (mm)", min_value=1.0, value=150.0)
    with c3:
        fck = st.number_input("Characteristic strength fck (MPa)", min_value=0.0, value=25.0)

    if st.button("Calculate cube strength"):
        inp = ConcreteCubeTestInput(
            load_at_failure_kN=load,
            cube_size_mm=size,
            characteristic_strength_MPa=fck,
        )
        out = calculate_concrete_cube_test(inp)

        st.subheader("Results")
        st.write(f"Cube strength: **{out.cube_strength_MPa:.2f} MPa**")
        if out.passes:
            st.success("Result: PASS (cube strength ≥ fck)")
        else:
            st.error("Result: FAIL (cube strength < fck)")
