import streamlit as st
from calculators.advanced_utilities.hydraulics.pump_horsepower import (
    PumpHorsepowerInput,
    calculate_pump_horsepower,
)

def render():
    st.header("Pump Horsepower Calculation")

    flow_rate_gpm = st.number_input("Flow Rate (GPM)", min_value=0.0, value=50.0)
    head_ft = st.number_input("Pump Head (ft)", min_value=0.0, value=50.0)
    efficiency = st.number_input("Efficiency (%)", min_value=0.0, value=75.0)

    if st.button("Calculate Pump Horsepower"):
        inp = PumpHorsepowerInput(flow_rate_gpm=flow_rate_gpm, head_ft=head_ft, efficiency=efficiency)
        horsepower = calculate_pump_horsepower(inp)

        st.subheader("Results")
        st.write(f"Pump Horsepower: **{horsepower:.2f} HP**")
