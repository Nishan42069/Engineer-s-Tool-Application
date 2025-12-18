import streamlit as st
from calculators.conversion.unit_conversion.voltage import VOLTAGE_UNITS, VoltageInput, convert_voltage

def render():
    st.header("Voltage Converter")

    units = list(VOLTAGE_UNITS.keys())

    c = st.columns(3)
    with c[0]:
        value = st.number_input("Value", value=230.0)
    with c[1]:
        from_unit = st.selectbox("From", units, index=units.index("V"))
    with c[2]:
        to_unit = st.selectbox("To", units, index=units.index("kV") if "kV" in units else 0)

    if st.button("Convert"):
        try:
            out = convert_voltage(VoltageInput(value=value, from_unit=from_unit, to_unit=to_unit))
            st.success(f"{value:g} {from_unit} = {out.value_out:.6g} {to_unit}")
        except Exception as e:
            st.error(str(e))
