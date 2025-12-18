import streamlit as st
from calculators.advanced_utilities.hydraulics.total_head import (
    TotalHeadInput,
    calculate_total_head,
)

def render():
    st.header("Total Head Calculation")

    flow_rate_gpm = st.number_input("Flow Rate (GPM)", min_value=0.0, value=50.0)
    horsepower_hp = st.number_input("Horsepower (HP)", min_value=0.0, value=10.0)
    efficiency = st.number_input("Efficiency (%)", min_value=0.0, value=75.0)

    if st.button("Calculate Total Head"):
        inp = TotalHeadInput(flow_rate_gpm=flow_rate_gpm, horsepower_hp=horsepower_hp, efficiency=efficiency)
        total_head = calculate_total_head(inp)

        st.subheader("Results")
        st.write(f"Total Head: **{total_head:.2f} ft**")
