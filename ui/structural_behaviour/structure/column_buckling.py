import streamlit as st
from calculators.structural_behaviour.structure.column_buckling import (
    ColumnBucklingInput,
    calculate_column_buckling,
)

def render():
    st.header("Column Buckling")

    length_ft = st.number_input("Column Length (ft)", min_value=1.0, value=10.0)
    diameter_ft = st.number_input("Column Diameter (ft)", min_value=0.0, value=1.0)

    if st.button("Calculate Column Buckling"):
        inp = ColumnBucklingInput(length_ft=length_ft, diameter_ft=diameter_ft)
        P_cr = calculate_column_buckling(inp)

        st.subheader("Results")
        st.write(f"Critical Load: **{P_cr:.2f} kN**")
