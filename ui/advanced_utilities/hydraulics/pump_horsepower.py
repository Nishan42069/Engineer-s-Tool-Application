import streamlit as st
from calculators.advanced_utilities.hydraulics.pump_horsepower import (
    PumpPowerInput,
    calculate_pump_power,
)

# -------------------------
# UNIT CONVERSIONS
# -------------------------
FLOW_TO_M3S = {
    "GPM": 0.00006309,
    "m³/hr": 1 / 3600,
}

HEAD_TO_M = {
    "Meter (m)": 1.0,
    "Feet (ft)": 0.3048,
}


def render():
    st.header("Pump Power (Horsepower) Calculator")

    # -------------------------
    # UNIT SELECTION
    # -------------------------
    u = st.columns(2)
    with u[0]:
        flow_unit = st.selectbox(
            "Flow rate unit",
            list(FLOW_TO_M3S.keys()),
        )
    with u[1]:
        head_unit = st.selectbox(
            "Pump head unit",
            list(HEAD_TO_M.keys()),
        )

    # -------------------------
    # INPUTS
    # -------------------------
    st.subheader("Pump Parameters")

    i = st.columns(3)
    with i[0]:
        flow = st.number_input(
            f"Flow rate ({flow_unit})",
            min_value=0.0,
            value=50.0,
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
    if st.button("Calculate Pump Power"):
        flow_m3_s = flow * FLOW_TO_M3S[flow_unit]
        head_m = head * HEAD_TO_M[head_unit]

        inp = PumpPowerInput(
            flow_m3_s=flow_m3_s,
            head_m=head_m,
            efficiency=efficiency,
        )

        out = calculate_pump_power(inp)

        # -------------------------
        # RESULTS
        # -------------------------
        st.subheader("Results")

        r = st.columns(3)
        with r[0]:
            st.metric("Power (W)", f"{out.power_w:,.1f}")
        with r[1]:
            st.metric("Power (kW)", f"{out.power_kw:.3f}")
        with r[2]:
            st.metric("Power (HP)", f"{out.power_hp:.2f}")
