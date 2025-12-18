import streamlit as st
from calculators.quantity_n_material.other_quantities.diagonal import (
    DiagonalInput,
    calculate_diagonal,
)


def render():
    st.header("Rectangle / Room Diagonal")

    c1, c2 = st.columns(2)
    with c1:
        L = st.number_input("Length", min_value=0.0, value=4.0)
    with c2:
        B = st.number_input("Width", min_value=0.0, value=3.0)

    if st.button("Calculate diagonal"):
        inp = DiagonalInput(length=L, width=B)
        out = calculate_diagonal(inp)

        st.subheader("Result")
        st.success(f"Diagonal: **{out.diagonal:.3f} (same units as input)**")
