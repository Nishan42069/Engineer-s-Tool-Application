import streamlit as st
from calculators.quantity_n_material.soil_mechanics.modulus_elasticity_concrete import (
    ModulusElasticityConcreteInput,
    calculate_modulus_elasticity_concrete,
)


def render():
    st.header("Modulus of Elasticity of Concrete")

    st.subheader("Inputs")
    c1, c2 = st.columns(2)
    with c1:
        fck = st.number_input("Characteristic strength fck (MPa)", min_value=0.0, value=25.0)
    with c2:
        coeff = st.number_input("Coefficient k (Ec = k√fck)", min_value=0.0, value=5000.0)

    if st.button("Calculate Ec"):
        inp = ModulusElasticityConcreteInput(
            fck_MPa=fck,
            coefficient=coeff,
        )
        out = calculate_modulus_elasticity_concrete(inp)

        st.subheader("Result")
        st.metric("Ec (MPa)", f"{out.Ec_MPa:.0f}")
