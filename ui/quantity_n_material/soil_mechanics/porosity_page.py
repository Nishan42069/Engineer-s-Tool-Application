import streamlit as st
from calculators.quantity_n_material.soil_mechanics.porosity import (
    PorosityInput,
    calculate_porosity,
)


def render():
    st.header("Porosity of Soil")

    st.subheader("Input")
    e = st.number_input("Void ratio e", min_value=0.0, value=0.7)

    if st.button("Calculate porosity"):
        inp = PorosityInput(void_ratio=e)
        out = calculate_porosity(inp)

        st.subheader("Result")
        st.metric("Porosity n (decimal)", f"{out.porosity_decimal:.3f}")
        st.metric("Porosity n (%)", f"{out.porosity_percent:.1f} %")
