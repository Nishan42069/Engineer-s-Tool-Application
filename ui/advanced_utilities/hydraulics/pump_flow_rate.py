import streamlit as st
from calculators.advanced_utilities.hydraulics.pump_flow_rate import (
    PumpFlowRateInput,
    calculate_pump_flow_rate,
)

# -------------------------
# UNIT CONVERSIONS
# -------------------------
POWER_TO_WATT = {
    "Watt (W)": 1.0,
    "Kilowatt (kW)": 1000.0,
}

HEAD_TO_METER = {
    "Meter (m)": 1.0,
    "Feet (ft)": 0.3048,
}

FLOW_FROM_M3S = {
    "m³/s": 1.0,
    "m³/hr": 3600.0,
    "L/s": 1000.0,
}


def render():
    st.header("Pump Flow Rate Calculator")

    # -------------------------
    # UNIT SELECTION
    # -------------------------
    u = st.columns(3)
    with u[0]:
        power_unit = st.selectbox(
            "Pump power unit",
            list(POWER_TO_WATT.keys()),
        )
    with u[1]:
        head_unit = st.selectbox(
            "Pump head unit",
            list(HEAD_TO_METER.keys()),
        )
    with u[2]:
        flow_unit = st.selectbox(
            "Output flow unit",
            list(FLOW_FROM_M3S.keys()),
        )

    # -------------------------
    # INPUTS
    # -------------------------
    st.subheader("Pump Parameters")

    i = st.columns(3)
    with i[0]:
        power = st.number_input(
            f"Pump power ({power_unit.split()[0]})",
            min_value=0.0,
            value=7.5,
        )
    with i[1]:
        head = st.number_input(
            f"Pump head ({head_unit.split()[0]})",
            min_value=0.0,
            value=30.0,
        )
    with i[2]:
        efficiency = st.number_input(
            "Pump efficiency (%)",
            min_value=0.0,
            value=75.0,
        )

    # -------------------------
    # CALCULATE
    # -------------------------
    if st.button("Calculate Flow Rate"):
        power_w = power * POWER_TO_WATT[power_unit]
        head_m = head * HEAD_TO_METER[head_unit]

        inp = PumpFlowRateInput(
            power_w=power_w,
            head_m=head_m,
            efficiency=efficiency,
        )

        flow_m3_s = calculate_pump_flow_rate(inp)
        flow_display = flow_m3_s * FLOW_FROM_M3S[flow_unit]

        # -------------------------
        # RESULTS
        # -------------------------
        st.subheader("Results")

        st.metric(
            f"Pump flow rate ({flow_unit})",
            f"{flow_display:.3f}",
        )
