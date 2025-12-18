import streamlit as st
from calculators.advanced_utilities.hydraulics.pump_flow_rate import (
    PumpFlowRateInput,
    calculate_pump_flow_rate,
)

def render():
    st.header("Pump Flow Rate Calculation")

    power_hp = st.number_input("Pump Power (HP)", min_value=0.0, value=10.0)
    head_ft = st.number_input("Pump Head (ft)", min_value=0.0, value=50.0)
    efficiency = st.number_input("Pump Efficiency (%)", min_value=0.0, value=75.0)

    if st.button("Calculate Pump Flow Rate"):
        inp = PumpFlowRateInput(power_hp=power_hp, head_ft=head_ft, efficiency=efficiency)
        flow_rate = calculate_pump_flow_rate(inp)

        st.subheader("Results")
        st.write(f"Pump Flow Rate: **{flow_rate:.2f} GPM**")
